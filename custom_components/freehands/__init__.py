"""
Custom integration to integrate freeHands with Home Assistant.
For more details about this integration, please refer to
https://github.com/riveccia/freehands
"""
import _thread
import asyncio
from datetime import timedelta, datetime
from email.mime import message
import json
import logging
from operator import is_not
import random
from sqlite3 import Timestamp
import time
import threading
from hass_frontend import where
import numpy as np


import paho.mqtt.client as mqtt
from sqlalchemy import null
import websocket
import yaml

import ssl

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed


from .api import FreehandsApiClient

from .const import Pubs
from .const import televisionPubs
from .const import Subs
from .const import EventsSub
from .const import Routes
from .const import STARTUP_MESSAGE
from .const import PLATFORMS
from .const import DOMAIN
from .const import CONF_USERNAME
from .const import CONF_PASSWORD

from .const import tenantIdentificationCode
from .const import companyIdentificationCode
from .const import gatewayTag


SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)
_LOGGER.info("Hello World freeHands!")


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)

    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)

    session = async_get_clientsession(hass)
    client = FreehandsApiClient(username, password, session)

    coordinator = FreehandsDataUpdateCoordinator(hass, client=client)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    for platform in PLATFORMS:
        if entry.options.get(platform, True):
            coordinator.platforms.append(platform)
            hass.async_add_job(
                hass.config_entries.async_forward_entry_setup(entry, platform)
            )

    entry.add_update_listener(async_reload_entry)
    return True


class FreehandsDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: FreehandsApiClient,
    ) -> None:
        """Initialize."""
        self.api = client
        self.platforms = []

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.api.async_get_data()
        except Exception as exception:
            raise UpdateFailed() from exception


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
                if platform in coordinator.platforms
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)


file = open(r"config/gateway_conf.yaml", encoding="utf8")


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


yaml.add_multi_constructor("", any_constructor, Loader=yaml.SafeLoader)
configuration = yaml.safe_load(file)

# generate client ID with pub prefix randomly
clientToFreeHands_id = f"freehands-mqtt-{random.randint(0, 1000)}"


# id for ws commands
global id

############# BROKER FUNCTIONS #############


def on_connectToFreehands(client, userdata, flags, rc):
    topicBroker = str(
        tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/#"
    )
    if rc == 0:
        _LOGGER.info("connected!")
        client.subscribe(topicBroker)
        _LOGGER.info("sottoscritto")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)
        time.sleep(60)
        client.loop_stop()
        client.loop_start()


def on_message(client, userdata, msg):
    _LOGGER.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    global id
    for x in Subs:
        if (x["Subtopic"] in msg.topic) or (x["Subtopic"] == msg.topic):
            id = id + 1
            target = {"entity_id": x["Command"]["entity_id"]}
            if (
                x["Subtopic"]
                == tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartLight_1/brightness/set"
            ):
                serviceData = {"brightness_pct": str(msg.payload.decode())}
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": x["Command"]["service"],
                    "service_data": serviceData,
                    "target": target,
                }
            elif (
                x["Subtopic"]
                == tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartLight_1/color/set"
                and msg.payload.decode() != "color_white"
                and msg.payload.decode() != "turn_on"
            ):
                target = {"entity_id": "light.smartlight_1"}
                try:
                    arrToConvert = msg.payload.decode().split(",")
                    arrColor = [int(num) for num in arrToConvert]
                    serviceData = {"rgb_color": arrColor, "brightness_pct": "100"}
                    command = {
                        "id": id,
                        "type": "call_service",
                        "domain": x["Command"]["domain"],
                        "service": x["Command"]["service"],
                        "service_data": serviceData,
                        "target": target,
                    }
                except:
                    print("command error")
            elif "Thermovalve_" in x["Subtopic"] and "temperature" in x["Subtopic"]:
                serviceData = {"value": str(msg.payload.decode())}
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": x["Command"]["service"],
                    "service_data": serviceData,
                    "target": target,
                }
            elif "Conditioner_" in x["Subtopic"] and "temperature" in x["Subtopic"]:
                serviceData = {"temperature": str(msg.payload.decode())}
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": x["Command"]["service"],
                    "service_data": serviceData,
                    "target": target,
                }
            else:
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": msg.payload.decode(),
                    "target": target,
                }
            # if msg.payload.decode() == x["Payload"]:
            message_routing(client, "#", command)


def message_routing(client, topic, msg):

    try:
        if client.url in configuration["ip_broker_gateway"]:
            if isinstance(msg, str):
                client1.publish(topic=topic, payload=msg)
            else:
                client1.publish(topic=topic, payload=json.dumps(msg))
    except:
        print("no ws")
    try:
        if client._client_id.decode("utf-8") == clientToFreeHands_id:
            ws.send(json.dumps(msg))
    except:
        print("no mqtt")


def on_publish(client, userdata, result):
    print("data published  \n" + str(result) + "RESULT \n")
    pass


############# BROKER FUNCTIONS #############

############# Functional functions #############
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def is_integer(value):
    try:
        int(value)
        return True
    except:
        return False


def offOnToTrueFalse(value):
    if value == "off":
        return "false"
    elif value == "on":
        return "true"


def trueFalseToString(value):
    if value.lower() is True:
        return "true"
    elif value.lower() is False:
        return "false"


############# /Functional functions #############

############# Funzione per state SmartPlug_1 e Smartligth_1 #############
def functionForRoutingStateCustom(sensor):
    # topicSmartPlug1 = (
    #     tenantIdentificationCode
    #     + "/"
    #     + companyIdentificationCode
    #     + "/"
    #     + gatewayTag
    #     + "/SmartPlug_1/state/get"
    # )
    # topicSmartLigth1 = (
    #     tenantIdentificationCode
    #     + "/"
    #     + companyIdentificationCode
    #     + "/"
    #     + gatewayTag
    #     + "/SmartLight_1/state/get"
    # )
    for x in Pubs:
        if (
            x["Friedly_name"]
            == sensor["event"]["data"]["new_state"]["attributes"]["friendly_name"]
        ):
            for t in x["Topic_out_custom"]:
                if t["key"] == "state":
                    topic = t["Topic_out"]
                    value = offOnToTrueFalse(
                        sensor["event"]["data"]["new_state"]["state"]
                    )
                    messageToAppend = {"key": "state", "value": str(value)}
                    messageSingleTopic = {"value": str(value)}
                    message_routing(ws, topic, messageSingleTopic)

    # value = offOnToTrueFalse(sensor["event"]["data"]["new_state"]["state"])
    # messageToAppend = {"key": "state", "value": str(value)}
    # messageSingleTopic = {"value": str(value)}
    # if "light.smartlight_1" == sensor["event"]["data"]["new_state"]["entity_id"]:
    #     message_routing(ws, topicSmartLigth1, messageSingleTopic)
    # else:
    #     message_routing(ws, topicSmartPlug1, messageSingleTopic)

    return messageToAppend


############# /Funzione per state SmartPlug_1 e Smartligth_1 #############


############# Funzione creazione battery low #############
def createButoonRouting(data):
    arrStructureJson = []
    for item in data:
        if item["key"] == "battery":
            if float(item["value"]) <= 10:
                messageToAppend = {
                    "key": "battery_low",
                    "value": "true",
                }
                arrStructureJson.append(messageToAppend)
            else:
                messageToAppend = {
                    "key": "battery_low",
                    "value": "false",
                }
                arrStructureJson.append(messageToAppend)
        elif item["key"] == "action":
            messageToAppend = {
                "key": "action",
                "value": "true",
            }
            arrStructureJson.append(messageToAppend)
        elif item["key"] == "battery":
            messageToAppend = {
                "key": "battery",
                "value": item["value"],
            }
            arrStructureJson.append(messageToAppend)
        else:
            messageToAppend = {"key": item["key"], "value": item["value"]}
            arrStructureJson.append(messageToAppend)
    return arrStructureJson


############# /Funzione creazione battery low #############

############# Funzione routing sensore letto #############
def functionRoutingWithings(ws, sensor):
    arrStructureJson = []
    filteredObject = {}
    for x in Routes:
        if x["entity_id"] in sensor["event"]["data"]["new_state"]["entity_id"]:
            if len(x["customRoute"]) > 1:
                ####
                state = offOnToTrueFalse(sensor["event"]["data"]["new_state"]["state"])
                ####
                filteredObject[x["key"]] = state
                messageToAppend = {"key": x["key"], "value": state}
                messageSingleTopic = {"value": state}
                arrStructureJson.append(messageToAppend)
                timestamp = time.time()
                dt = int(timestamp) * 1000
                print("dt", str(dt))
                dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                message_routing(ws, x["customRoute"], messageSingleTopic)
                customTopic = (
                    tenantIdentificationCode
                    + "/"
                    + companyIdentificationCode
                    + "/"
                    + gatewayTag
                    + "/SleepTracker_1/get"
                )
                message_routing(
                    ws,
                    customTopic,
                    dataToSend,
                )
            else:
                ####
                state = offOnToTrueFalse(sensor["event"]["data"]["new_state"]["state"])
                ####
                filteredObject[x["key"]] = state
                messageToAppend = {"key": x["key"], "value": state}
                arrStructureJson.append(messageToAppend)
                timestamp = time.time()
                dt = int(timestamp) * 1000
                print("dt", str(dt))
                dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                customTopic = (
                    tenantIdentificationCode
                    + "/"
                    + companyIdentificationCode
                    + "/"
                    + gatewayTag
                    + "/SleepTracker_1/get"
                )
                message_routing(
                    ws,
                    customTopic,
                    dataToSend,
                )


############# /Funzione routing sensore letto #############

############# Funzione routing television #############
def functionRoutingTelevision(ws, sensor):
    arrStructureJson = []
    filteredObject = {}
    if (
        "television_" in sensor["event"]["data"]["new_state"]["entity_id"]
        or "television_" == sensor["event"]["data"]["new_state"]["entity_id"]
    ):
        for x in televisionPubs:
            if (
                x["Name"] in sensor["event"]["data"]["new_state"]["entity_id"]
                and x["Name"] == sensor["event"]["data"]["new_state"]["entity_id"]
            ):
                ####
                state = offOnToTrueFalse(sensor["event"]["data"]["new_state"]["state"])
                ####
                messageToAppend = {"key": "state", "value": state}
                arrStructureJson.append(messageToAppend)
                timestamp = time.time()
                dt = int(timestamp) * 1000
                print("dt", str(dt))
                dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                messageSingleTopic = {"value": state}
                topicOutCustom = [d for d in x["Topic_out-custom"] == "state"]
                message_routing(
                    ws,
                    topicOutCustom,
                    messageSingleTopic,
                )
                message_routing(
                    ws,
                    x["Topic_out"],
                    dataToSend,
                )


############# /Funzione routing television #############

############# WS FUNCTIONS #############


def on_messagews(ws, message):
    data = json.loads(message)
    arrStructureJson = []
    if data["type"] == "event":
        filteredObject = {}
        customTopics = {}
        ################## Funzione routing sensore letto ##################
        if "withings" in data["event"]["data"]["new_state"]["entity_id"]:
            functionRoutingWithings(ws, data)
        ################## /Funzione routing sensore letto ##################

        ################## Funzione routing televisione ##################
        elif "television" in data["event"]["data"]["new_state"]["entity_id"]:
            functionRoutingTelevision(ws, data)
        ################## /Funzione routing televisione ##################
        else:
            for x in Pubs:
                if (
                    x["Friedly_name"]
                    in data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
                ) or (
                    x["Friedly_name"]
                    == data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
                ):
                    # if ("SmartPlug_1" in data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
                    # ):
                    #     value = trueFalseToString(
                    #         data["event"]["data"]["new_state"]["state"]
                    #     )
                    #     messageToAppend = {
                    #         "key": "state",
                    #         "value": str(value),
                    #     }
                    #     filteredObject["state"] = str(value)
                    #     arrStructureJson.append(messageToAppend)
                    for key, value in dict.items(
                        data["event"]["data"]["new_state"]["attributes"]
                    ):
                        if key in x["key"]:
                            ####
                            # if isinstance(value, str) is True:
                            #     value = trueFalseToString(value)
                            ####
                            if is_float(value):
                                value = str(value)
                            if is_integer(value):
                                value = str(float(value))

                            ############################ Sostituzione chiave "heating_stop" con "state" ############################

                            if key == "heating_stop":
                                key = "state"
                                if str(value).lower() == "off":
                                    valueToSend = "false"
                                elif str(value).lower() == "on":
                                    valueToSend = "true"
                                else:
                                    valueToSend = value
                                filteredObject["state"] = valueToSend
                                # messageToAppend = {"key": "state", "value": value}
                                # arrStructureJson.append(messageToAppend)

                            ############################ /Sostituzione chiave "heating_stop" con "state" ############################

                            else:
                                filteredObject[key] = value

                            # Controllo sensore energy
                            if (
                                "sensor.shelly_shem"
                                in data["event"]["data"]["new_state"]["entity_id"]
                            ):
                                c = (
                                    float(data["event"]["data"]["new_state"]["state"])
                                    / 1000
                                )
                                messageToAppend = {
                                    "key": "current_consumption",
                                    "value": str(c),
                                }
                                filteredObject["current_consumption"] = str(c)

                            # /Controllo sensore energy

                            if (
                                str(value).lower() == "off"
                                or str(value).lower() == "turn_off"
                                or str(value).lower() == "false"
                            ):
                                valueToSend = "false"
                            elif (
                                str(value).lower() == "on"
                                or str(value).lower() == "turn_on"
                                or str(value).lower() == "true"
                            ):
                                valueToSend = "true"
                            elif value is None:
                                continue
                            else:
                                valueToSend = value
                            messageToAppend = {"key": key, "value": valueToSend}
                            arrStructureJson.append(messageToAppend)

                    if (
                        "switch.smartplug_"
                        in data["event"]["data"]["new_state"]["entity_id"]
                        or "sensor.smartplug_"
                        == data["event"]["data"]["new_state"]["entity_id"]
                        or "light.smartlight_"
                        == data["event"]["data"]["new_state"]["entity_id"]
                        or "light.smartlight_"
                        in data["event"]["data"]["new_state"]["entity_id"]
                    ):
                        messageToAppend = functionForRoutingStateCustom(data)
                        filteredObject["state"] = str(messageToAppend["value"])
                        arrStructureJson.append(messageToAppend)
                    if (
                        "Button_"
                        in data["event"]["data"]["new_state"]["attributes"][
                            "friendly_name"
                        ]
                    ):
                        arrStructureJson = createButoonRouting(arrStructureJson)

                    #     arrStructureJson.append(messageToAppend)
                    #     value = offOnToTrueFalse(
                    #         data["event"]["data"]["new_state"]["state"]
                    #     )
                    #     messageToAppend = {
                    #         "key": "state",
                    #         "value": str(value),
                    #     }
                    #     message_routing(
                    #         ws,
                    #         "appforgood/appforgood_matera/gateway_6/SmartPlug_1/state/get",
                    #         messageToAppend,
                    #     )
                    #     filteredObject["state"] = str(value)
                    #     arrStructureJson.append(messageToAppend)
                    # if (
                    #     "light.smartlight_1"
                    #     == data["event"]["data"]["new_state"]["entity_id"]
                    # ):
                    #     value = offOnToTrueFalse(
                    #         data["event"]["data"]["new_state"]["state"]
                    #     )
                    #     messageToAppend = {"key": "state", "value": str(value)}
                    #     message_routing(
                    #         ws,
                    #         "appforgood/appforgood_matera/gateway_6/SmartLight_1/state/get",
                    #         messageToAppend,
                    #     )
                    #     filteredObject["state"] = str(value)
                    #     arrStructureJson.append(messageToAppend)

                    timestamp = time.time()
                    dt = int(timestamp) * 1000
                    print("dt", str(dt))
                    dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                    if (
                        filteredObject != {}
                        or message != null
                        or arrStructureJson != []
                    ):
                        message_routing(ws, x["Topic_out"], dataToSend)
                        try:
                            for topicCustom in x["Topic_out_custom"]:
                                for key, value in dict.items(filteredObject):

                                    if key == topicCustom["key"]:
                                        if str(filteredObject[key]).lower() == "off":
                                            valueSingletopic = "false"
                                        elif str(filteredObject[key]).lower() == "on":
                                            valueSingletopic = "true"
                                        elif (
                                            str(filteredObject[key]).lower() == "single"
                                            or str(filteredObject[key]).lower()
                                            == "double"
                                            or str(filteredObject[key]).lower()
                                            == "triple"
                                            or str(filteredObject[key]).lower()
                                            == "quadruple"
                                            or str(filteredObject[key]).lower()
                                            == "many"
                                        ):
                                            valueSingletopic = "true"
                                        elif str(filteredObject[key]).lower() == "none":
                                            valueSingletopic = "false"
                                        else:
                                            valueSingletopic = str(
                                                filteredObject[key]
                                            ).lower()
                                        msg = '{"value": "' + valueSingletopic + '"}'
                                        if (
                                            topicCustom["Topic_out"]
                                            == "over/ROMA_LAURENTINA/gw_luca/Button_1/state/get"
                                        ):
                                            print("msg:", msg)
                                        message_routing(
                                            ws, topicCustom["Topic_out"], msg
                                        )

                        except KeyError:
                            print("NO CUSTOM TOPICS")
    else:
        print("nessun evento")


def on_errorws(ws, error):
    print(error)


def on_closews(ws, close_status_code, close_msg):
    print("Reconnecting")
    if close_status_code != 1000:
        connectToBroker()


def on_openws(ws):
    global id
    ws.send(json.dumps(configuration["LoginToWs"]))
    print("Auth effettuato")
    ws.send(
        json.dumps(EventsSub)
    )  # json.dumps({"id": 1, "type": "subscribe_events", "event_type": "state_changed"})
    id = 1

    print("Sottoscrizione agli eventi effetuata")
    print("connected")


############# WS FUNCTIONS ####################

############# CONNECTIONS ####################

websocket.enableTrace(True)
ws = websocket.WebSocketApp(
    str(configuration["ip_broker_gateway"]),
    on_open=on_openws,
    on_message=on_messagews,
    on_error=on_errorws,
    on_close=on_closews,
)


def connectToBroker():
    mqttT = threading.Thread(target=HandleConnectRefusedToFreehands)
    mqttT.daemon = True
    mqttT.start()
    wst = threading.Thread(target=ws.run_forever)
    wst.daemon = True
    wst.start()


client1 = mqtt.Client(
    client_id=clientToFreeHands_id,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv31,
    transport="tcp",
)
client1.username_pw_set(
    configuration["username_broker_freehands"], configuration["password"]
)

client1.on_connect = on_connectToFreehands
client1.on_message = on_message
client1.on_publish = on_publish
client1.broker = configuration["ip_broker_freehands"]
client1.port = configuration["port_broker_freehands"]

client1.topic = "#"
client1.keepalive = 60


def HandleConnectRefusedToFreehands():
    i = 2
    while i == 2:
        try:
            _LOGGER.info("Riconnessione")
            client1.connect(client1.broker, client1.port, client1.keepalive)
            i = 1
        except:
            _LOGGER.info("NON CONNESSO....")
            i = 2


connectToBroker()

client1.loop_start()

"""
Custom integration to integrate freeHands with Home Assistant.
For more details about this integration, please refer to
https://github.com/riveccia/freehands
"""
import _thread
import asyncio
from distutils.log import error
import json
import logging
import paho.mqtt.client as mqtt
import random
import time
import threading
import numpy as np
import ssl
import websocket
import yaml
import schedule
import paho.mqtt.publish as publish
import requests
import socket
import fcntl
import struct

from datetime import timedelta, datetime
from email.mime import message
from hass_frontend import where
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from operator import is_not
from sqlalchemy import null
from sqlite3 import Timestamp

from .api import FreehandsApiClient
from .const import companyIdentificationCode
from .const import CONF_USERNAME
from .const import CONF_PASSWORD
from .const import DOMAIN
from .const import EventsSub
from .const import gatewayTag
from .const import num2words
from .const import PLATFORMS
from .const import Pubs
from .const import Routes
from .const import STARTUP_MESSAGE
from .const import Subs
from .const import televisionPubs
from .const import tenantIdentificationCode
from .const import VERSION


_LOGGER: logging.Logger = logging.getLogger(__package__)
_LOGGER.info("Hi, this is freeHands!")

configFile = open(r"/config/gateway_conf.yaml", encoding="utf8")

# flag to stop MQTT connection thread
keepConnectingMQTT = True

# generate client ID with pub prefix randomly
mqttClientId = f"freehands-mqtt-{random.randint(0, 100000)}"

SCAN_INTERVAL = timedelta(seconds=30)
TIMEOUT_CONNECTION = 10
TIMEOUT_THREAD = 30


# id for ws commands
global id

# threads to manage Web Socket and MQTT connections
mqttThread = None
wstThread = None
scheduleThread = None


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


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


############# Functional functions #############
def n2w(n):
    try:
        return num2words[int(n)]
    except:
        return ""


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


def message_routing(client, topic, msg):
    try:
        # if the client is the local Web Socket, send via MQTT
        result = isinstance(client, websocket.WebSocketApp)
        if result:
            _LOGGER.debug("client is a Web Socket")
            if client.url in configuration["ip_broker_gateway"]:
                if isinstance(msg, str):
                    mqttClient.publish(topic=topic, payload=msg)
                else:
                    mqttClient.publish(topic=topic, payload=json.dumps(msg))
        else:
            _LOGGER.debug("client is NOT a Web Socket")
    except:
        _LOGGER.exception("MQTT not available")
    try:
        # if the client is freeHands MQTT broker, send via Web Socket
        result = isinstance(client, mqtt.Client)
        if result:
            _LOGGER.debug("client is a MQTT")
            if client._client_id.decode("utf-8") == mqttClientId:
                wsClient.send(json.dumps(msg))
        else:
            _LOGGER.debug("client is NOT a MQTT")
    except:
        _LOGGER.exception("WebService not available")


############# /Functional functions #############

############ Funzione invio middleware version ############


def functionRoutingMiddlewareVersion():

    dataToSend = {
        "value": str(VERSION),
    }
    middlerwareVersionTopic = (
        tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/appFORGOOD_mw/Mw_version/get"
    )
    autha = {
        "username": configuration["username_broker_freehands"],
        "password": configuration["password"],
    }
    try:
        publish.single(
            topic=middlerwareVersionTopic,
            payload=json.dumps(dataToSend),
            hostname=configuration["ip_broker_freehands"],
            client_id="mqtt-client-mwversion",
            will=None,
            tls=None,
            protocol=mqtt.MQTTv311,
            transport="tcp",
            port=configuration["port_broker_freehands"],
            auth=autha,
            keepalive=60,
        )
    except Exception as e:
        _LOGGER.info("connection lost when try to publish middleware version")


############ /Funzione invio middleware version ############

############  Funzione per invio IP del gateway ################

# inizializzazione file configuration per external url
file = open(r"/config/configuration.yaml", encoding="utf8")
yaml.add_multi_constructor("", any_constructor, Loader=yaml.SafeLoader)

ha_configuration = yaml.safe_load(file)
# /inizializzazione file configuration per external url


def functionRoutingIpAddress():
    host_ips = {}
    for interface in ["eth0", "wlan0"]:
        try:
            host_ip = socket.inet_ntoa(
                fcntl.ioctl(
                    socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
                    0x8915,  # SIOCGIFADDR
                    struct.pack("256s", bytes(interface, "utf-8")),
                )[20:24]
            )
            host_ips[interface] = host_ip
        except Exception as e:
            pass

    if "eth0" in host_ips:
        chosen_interface = "eth0"
    elif "wlan0" in host_ips:
        chosen_interface = "wlan0"
    else:
        _LOGGER.info("No available interface found")
        return

    # timestamp = time.time()

    # dt = int(timestamp) * 1000

    ext_url = str(ha_configuration["homeassistant"]["external_url"])

    auth = {
        "username": configuration["username_broker_freehands"],
        "password": configuration["password"],
    }

    topic_base = f"{tenantIdentificationCode}/{companyIdentificationCode}/{gatewayTag}/Gateway_IP"
    topics = [
        f"{topic_base}/Internal_URL/get",
        f"{topic_base}/External_URL/get",
    ]
    values = [
        {
            "value": host_ip,
        },
        {
            "value": ext_url,
        },
    ]

    for topic, value in zip(topics, values):
        try:
            publish.single(
                topic=topic,
                payload=json.dumps(value),
                hostname=configuration["ip_broker_freehands"],
                client_id="mqtt-client-ip",
                will=None,
                tls=None,
                protocol=mqtt.MQTTv311,
                transport="tcp",
                port=configuration["port_broker_freehands"],
                auth=auth,
                keepalive=60,
            )
        except Exception as e:
            _LOGGER.info(
                f"connection lost when trying to publish {topic.split('/')[-1]}", e
            )


############  /Funzione per invio IP del gateway ################

############# Funzione per state SmartPlug_1 e Smartligth_1 #############
def functionForRoutingStateCustom(sensor):
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
                    message_routing(wsClient, topic, messageSingleTopic)

    return messageToAppend


############# /Funzione per state SmartPlug_1 e Smartligth_1 #############

############# Funzione creazione battery low #############
def createButoonRouting(data):
    arrStructureJson = []
    for item in data:
        if item["key"] == "battery":
            try:
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
            except Exception as e:
                _LOGGER.info("empty payload in battery level from button ", e)
        elif item["key"] == "action":
            try:
                if (
                    str(item["value"]).lower() == "single"
                    or str(item["value"]).lower() == "double"
                    or str(item["value"]).lower() == "triple"
                    or str(item["value"]).lower() == "quadruple"
                    or str(item["value"]).lower() == "many"
                ):
                    valueAction = "true"
                else:
                    valueAction = "false"
                messageToAppend = {
                    "key": "action",
                    "value": valueAction,
                }
                arrStructureJson.append(messageToAppend)
            except Exception as e:
                _LOGGER.info("empty payload in action from button ", e)
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
def functionRoutingWithings(wsClient, sensor):
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
                if arrStructureJson:
                    dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                    message_routing(wsClient, x["customRoute"], messageSingleTopic)
                    customTopic = (
                        tenantIdentificationCode
                        + "/"
                        + companyIdentificationCode
                        + "/"
                        + gatewayTag
                        + "/SleepTracker_1/get"
                    )
                    message_routing(
                        wsClient,
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
                if arrStructureJson:
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
                        wsClient,
                        customTopic,
                        dataToSend,
                    )


############# /Funzione routing sensore letto #############

############# Funzione routing television #############
def functionRoutingTelevision(wsClient, sensor):
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
                if arrStructureJson:
                    dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                    messageSingleTopic = {"value": state}
                    topicOutCustom = [d for d in x["Topic_out-custom"] == "state"]
                    message_routing(
                        wsClient,
                        topicOutCustom,
                        messageSingleTopic,
                    )
                    message_routing(
                        wsClient,
                        x["Topic_out"],
                        dataToSend,
                    )


############# /Funzione routing television #############

############# Funzione routing Energy Meter ############## 
def functionRoutingEnergyMether(wsClient, data):
     arrStructureJson = []
     if "current_consumption" in data["event"]["data"]["new_state"]["entity_id"]:
         try:
             c = float(data["event"]["data"]["new_state"]["state"]) / 1000
             messageSingleTopicCurrentConsumptionShelly = {"value": str(c)}
             messageToAppend = {"key": "current_consumption", "value": str(c)}
             arrStructureJson.append(messageToAppend)
             topicOutCustom = (
                 tenantIdentificationCode
                 + "/"
                 + companyIdentificationCode
                 + "/"
                 + gatewayTag
                 + "/EnergyMeter_1/current_consumption/get"
             )
             message_routing(
                 wsClient, topicOutCustom, messageSingleTopicCurrentConsumptionShelly
             )
         except Exception as e:
             _LOGGER.info("empty payload in current consumption from energy meter", e)
     elif "total_consumption" in data["event"]["data"]["new_state"]["entity_id"]:
         try:
             c = float(data["event"]["data"]["new_state"]["state"])
             messageSingleTopicTotalConsumptionShelly = {"value": str(c)}
             messageToAppend = {"key": "total_consumption", "value": str(c)}
             arrStructureJson.append(messageToAppend)
             topicOutCustom = (
                 tenantIdentificationCode
                 + "/"
                 + companyIdentificationCode
                 + "/"
                 + gatewayTag
                 + "/EnergyMeter_1/total_consumption/get"
             )
             message_routing(
                 wsClient, topicOutCustom, messageSingleTopicTotalConsumptionShelly
            )
         except Exception as e:
            _LOGGER.info("empty payload in current consumption from energy meter", e)
     timestamp = time.time()
     dt = int(timestamp) * 1000
     print("dt", str(dt))
     if arrStructureJson:
        dataToSend = {"detections": arrStructureJson, "timestamp": dt}
        topicOut = (
            tenantIdentificationCode
            + "/"
            + companyIdentificationCode
            + "/"
            + gatewayTag
            + "/EnergyMeter_1/get"
        )
        message_routing(wsClient, topicOut, dataToSend)

############# /Funzione routing Energy Meter #############

############# Funzione routing ShowerSensor #############
# def functionRoutingShowerSensor(wsClient, data):
#     arrStructureJson = []
#     if "state" in data["event"]["data"]["new_state"]:
#         try:
#             c = data["event"]["data"]["new_state"]["state"])
#             messageToAppend = {"key": "state", "value": str(c)}
#             arrStructureJson.append(messageToAppend)
#             topicOutCustom = (
#                 tenantIdentificationCode
#                 + "/"
#                 + companyIdentificationCode
#                 + "/"
#                 + gatewayTag
#                 + "/ShowerSensor_1/state/get"
#             )
#             message_routing(
#                 wsClient, topicOutCustom, messageSingleTopicCurrentConsumptionShelly
#             )
#         except Exception as e:
#             _LOGGER.info("empty payload in current consumption from energy meter", e)
#     timestamp = time.time()
#     dt = int(timestamp) * 1000
#     print("dt", str(dt))
#     if arrStructureJson:
#         dataToSend = {"detections": arrStructureJson, "timestamp": dt}
#         topicOut = (
#             tenantIdentificationCode
#             + "/"
#             + companyIdentificationCode
#             + "/"
#             + gatewayTag
#             + "/ShowerSensor_1/get"
#         )
#         message_routing(wsClient, topicOut, dataToSend)


############# /Funzione routing ShowerSensor #############

############# MQTT BROKER FUNCTIONS #############
def mqtt_on_connect(client, userdata, flags, result_code):
    if result_code == 0:
        _LOGGER.info("MQTT client connected")

        topicBroker = str(
            tenantIdentificationCode
            + "/"
            + companyIdentificationCode
            + "/"
            + gatewayTag
            + "/#"
        )

        client.subscribe(topicBroker)
        _LOGGER.info(f"Subscription to topic '{topicBroker}' completed")
    else:
        _LOGGER.info(f"MQTT client connection failed (error code = {result_code})")
        # handleConnectToMQTT()
        connectToMQTT()


def mqtt_on_message(client, userdata, msg):
    _LOGGER.info(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
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
                serviceTemperature = str(n2w(msg.payload.decode()))
                if "Conditioner_1" in x["Subtopic"]:
                    remoteConditioner = "remote.conditioner_1_remote"
                elif "Conditioner_2" in x["Subtopic"]:
                    remoteConditioner = "remote.conditioner_2_remote"
                else:
                    remoteConditioner = ""
                serviceData = {remoteConditioner}
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": serviceTemperature,
                    "service_data": serviceData,
                }
            elif "Conditioner_" in x["Subtopic"] and "temperature" not in x["Subtopic"]:
                if "Conditioner_1" in x["Subtopic"]:
                    remoteConditioner = "remote.conditioner_1_remote"
                elif "Conditioner_2" in x["Subtopic"]:
                    remoteConditioner = "remote.conditioner_2_remote"
                else:
                    remoteConditioner = ""
                serviceData = {"entity_id": remoteConditioner}
                command = {
                    "id": id,
                    "type": "call_service",
                    "domain": x["Command"]["domain"],
                    "service": x["Command"]["service"],
                    "service_data": serviceData,
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


def mqtt_on_publish(client, userdata, result):
    _LOGGER.info(f"Data published to MQTT (result = {result})")
    pass


def mqtt_on_socket_open(client, userdata, sock):
    _LOGGER.info("MQTT socket opened")


def mqtt_on_socket_close(client, userdata, sock):
    _LOGGER.info("MQTT socket closed")


############# /MQTT BROKER FUNCTIONS #############

############# WEBSOCKET FUNCTIONS #############
def webSocketErrorLog(close_status_code, close_msg):
    if close_status_code == 1000:
        return _LOGGER.info(
            f"Web Socket connection normally closed (message = '{close_msg}')"
        )
    elif close_status_code == 1001:
        return _LOGGER.error(
            f"Web Socket connection closed because the endpoint is going away (message = '{close_msg}')"
        )
    elif close_status_code == 1002:
        return _LOGGER.error(f"Web Socket protocolo error (message = '{close_msg}')")
    elif close_status_code == 1003:
        return _LOGGER.error(f"Web Socket unsupported data (message = '{close_msg}')")
    elif close_status_code == 1004:
        return _LOGGER.error(f"Web Socket error (message = '{close_msg}')")
    elif close_status_code == 1005:
        return _LOGGER.error(
            f"Web Socket no status code received (message = '{close_msg}')"
        )
    elif close_status_code == 1006:
        return _LOGGER.error(f"Web Socket abnormal closure (message = '{close_msg}')")
    elif close_status_code == 1007:
        return _LOGGER.error(
            f"Web Socket invalid frame payload data (message = '{close_msg}')"
        )
    elif close_status_code == 1008:
        return _LOGGER.error(f"Web Socket policy violation (message = '{close_msg}')")
    elif close_status_code == 1009:
        return _LOGGER.error(f"Web Socket message too big (message = '{close_msg}')")
    elif close_status_code == 1010:
        return _LOGGER.error(
            f"Web Socket missing mandatory extension (message = '{close_msg}')"
        )
    elif close_status_code == 1011:
        return _LOGGER.error(f"Web Socket internal error (message = '{close_msg}')")
    elif close_status_code == 1012:
        return _LOGGER.error(f"Web Socket server restarting (message = '{close_msg}')")
    elif close_status_code == 1013:
        return _LOGGER.error(f"Web Socket try again later (message = '{close_msg}')")
    elif close_status_code == 1014:
        return _LOGGER.error(f"Web Socket bad gateway (message = '{close_msg}')")
    elif close_status_code == 1015:
        return _LOGGER.error(
            f"Web Socket TLS handshake failure (message = '{close_msg}')"
        )
    else:
        _LOGGER.error(
            f"Web Socket generic error (code = {close_status_code}, message = '{close_msg}')"
        )


def websocket_on_close(wsClient, close_status_code, close_msg):
    _LOGGER.info("Connection to Web Socket closed")

    webSocketErrorLog(close_status_code=close_status_code, close_msg=close_msg)
    if close_status_code != 1000:
        _LOGGER.warning(
            f"Web Socket was closed with an error. Going to sleep for {TIMEOUT_CONNECTION}s..."
        )
        time.sleep(TIMEOUT_CONNECTION)
        _LOGGER.warning("Trying to reconnect to Web Socket...")
        # connectToBroker()
        connectToWebSocket()


def websocket_on_error(wsClient, error):
    _LOGGER.error(f"Web Socket error: {error}", exc_info=True)


def websocket_on_message(wsClient, message):
    data = json.loads(message)
    arrStructureJson = []
    if data["type"] == "event" and data["event"]["data"]["new_state"]["entity_id"] is not None:
        filteredObject = {}
        customTopics = {}
        ################## Funzione routing sensore letto ##################
        if "withings" in data["event"]["data"]["new_state"]["entity_id"]:
            functionRoutingWithings(wsClient, data)
        ################## /Funzione routing sensore letto ##################

        ################## Funzione routing televisione ##################
        elif "television" in data["event"]["data"]["new_state"]["entity_id"]:
            functionRoutingTelevision(wsClient, data)
        ################## /Funzione routing televisione ##################

        ################## Funzione routing shelly
        elif "sensor.shelly_shem" in data["event"]["data"]["new_state"]["entity_id"]:
#	    elif "EnergyMeter_" in data["event"]["data"]["attributes"]["friendly_name"]:
            functionRoutingEnergyMether(wsClient, data)
        ################## /Funzione routing shelly

        else:
            for x in Pubs:
                if (
                    x["Friedly_name"]
                    in data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
                ) or (
                    x["Friedly_name"]
                    == data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
                ):

                    for key, value in dict.items(
                        data["event"]["data"]["new_state"]["attributes"]
                    ):
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

                        if key in x["key"]:

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

                            ############################ /Sostituzione chiave "heating_stop" con "state" ############################

                            else:
                                if (
                                    str(value).lower() == "off"
                                    or str(value).lower() == "turn_off"
                                    or str(value).lower() == "false"
                                    or str(value).lower() == "none"  # controllo none
                                ):
                                    value = "false"
                                elif (
                                    str(value).lower() == "on"
                                    or str(value).lower() == "turn_on"
                                    or str(value).lower() == "true"
                                ):
                                    value = "true"
                                elif value is None:  # controllo none
                                    continue

                            filteredObject[key] = value
                            if (
                                str(value).lower() == "off"
                                or str(value).lower() == "turn_off"
                                or str(value).lower() == "false"
                                or str(value).lower() == "none"  # controllo none
                            ):
                                valueToSend = "false"
                            elif (
                                str(value).lower() == "on"
                                or str(value).lower() == "turn_on"
                                or str(value).lower() == "true"
                            ):
                                valueToSend = "true"
                            elif value is None:  # controllo none
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
			            or "ShowerSensor_"
                        in data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
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

                    timestamp = time.time()
                    dt = int(timestamp) * 1000
                    print("dt", str(dt))
                    if arrStructureJson:
                        dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                        if (
                            filteredObject != {}
                            or message != null
                            or arrStructureJson != []
                        ):
                            message_routing(wsClient, x["Topic_out"], dataToSend)
                            try:
                                for topicCustom in x["Topic_out_custom"]:
                                    for key, value in dict.items(filteredObject):

                                        if key == topicCustom["key"]:
                                            if (
                                                str(filteredObject[key]).lower()
                                                == "off"
                                            ):
                                                valueSingletopic = "false"
                                            elif (
                                                str(filteredObject[key]).lower() == "on"
                                            ):
                                                valueSingletopic = "true"
                                            elif (
                                                str(filteredObject[key]).lower()
                                                == "single"
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
                                            elif (
                                                str(filteredObject[key]).lower()
                                                == "none"
                                                or str(filteredObject[key]).lower()
                                                == "None"
                                            ):
                                                valueSingletopic = "false"
                                            else:
                                                valueSingletopic = str(
                                                    filteredObject[key]
                                                ).lower()
                                            msg = (
                                                '{"value": "' + valueSingletopic + '"}'
                                            )

                                            message_routing(
                                                wsClient, topicCustom["Topic_out"], msg
                                            )

                            except KeyError:
                                print("NO CUSTOM TOPICS")
    else:
        print("nessun evento")


def websocket_on_open(wsClient):
    _LOGGER.info("Connection to Web Socket completed")
    global id
    wsClient.send(json.dumps(configuration["LoginToWs"]))
    _LOGGER.info("Authorization message sent to Web Socket")
    wsClient.send(json.dumps(EventsSub))
    id = 1

    _LOGGER.info("Web Socket connection completed")


############# /WEBSOCKET FUNCTIONS ####################

############# CONNECTIONS ####################
# def connectToBroker():
#     _LOGGER.info("Creating connections...")
#
#     global mqttThread
#     global wstThread
#
#     if mqttThread and mqttThread.is_alive():
#         _LOGGER.info("An old MQTT client exists. Killing it...")
#         keepConnectingMQTT = False
#         mqttThread.join(timeout=TIMEOUT_THREAD)
#
#     _LOGGER.info("Starting MQTT client thread...")
#     mqttThread = threading.Thread(target=handleConnectToMQTT)
#     mqttThread.daemon = True
#     mqttThread.start()
#
#     if wstThread and wstThread.is_alive():
#         _LOGGER.info("An old Web Socket client exists. Killing it...")
#         wsClient.keep_running = False
#         # it is not possible to join this thread
#         #wstThread.join(timeout=TIMEOUT_THREAD)
#
#     _LOGGER.info("Starting Web Socket client thread...")
#     wstThread = threading.Thread(target=handleConnectToWebSocket)
#     wstThread.daemon = True
#     wstThread.start()

### FUNZIONE PER TRACCIARE I THREAD ATTIVI ###
# def log_active_threads():
#     active_threads = threading.enumerate()
#     _LOGGER.info("Active threads: {}".format(active_threads))
#     t = threading.Timer(10, log_active_threads)
#     t.start()
### /FUNZIONE PER TRACCIARE I THREAD ATTIVI ###

def handleScheduleFunction():
    _LOGGER.info("Starting schedule function thread...")
    schedule.every(5).minutes.do(functionRoutingMiddlewareVersion)
    schedule.every(5).minutes.do(functionRoutingIpAddress)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            _LOGGER.error("Thread shutting down due to an error: %s" % e)
            n = schedule.idle_seconds()
            if n is None:
                handleScheduleFunction()


def scheduledFunction():
    _LOGGER.info("Starting to manage scheduled function...")

    global scheduleThread

    if scheduleThread and scheduleThread.is_alive():
        _LOGGER.info("An old MQTT client exists. Killing it...")
        scheduleThread.join(timeout=TIMEOUT_THREAD)

    _LOGGER.info("Starting schedule thread...")
    scheduleThread = threading.Thread(target=handleScheduleFunction)
    scheduleThread.daemon = True
    scheduleThread.start()


def connectToMQTT():
    _LOGGER.info("Starting to manage MQTT thread...")

    global mqttThread

    if mqttThread and mqttThread.is_alive():
        _LOGGER.info("An old MQTT client exists. Killing it...")
        keepConnectingMQTT = False
        mqttThread.join(timeout=TIMEOUT_THREAD)

    _LOGGER.info("Starting MQTT client thread...")
    mqttThread = threading.Thread(target=handleConnectToMQTT)
    mqttThread.daemon = True
    mqttThread.start()


def connectToWebSocket():
    _LOGGER.info("Starting to manage Web Socket thread...")

    global wstThread

    if wstThread and wstThread.is_alive():
        _LOGGER.info("An old Web Socket client exists. Killing it...")
        wsClient.keep_running = False
        # it is not possible to join this thread
        # wstThread.join(timeout=TIMEOUT_THREAD)

    _LOGGER.info("Starting Web Socket client thread...")
    wstThread = threading.Thread(target=handleConnectToWebSocket)
    wstThread.daemon = True
    wstThread.start()


def handleConnectToMQTT():
    _LOGGER.info("Handling MQTT connection...")
    i = 2
    while i == 2:
        if keepConnectingMQTT:
            try:
                _LOGGER.info("Connecting to MQTT broker...")
                mqttClient.loop_start()
                mqttClient.connect(
                    mqttClient.broker, mqttClient.port, mqttClient.keepalive
                )
                i = 1
            except Exception as e:
                _LOGGER.error("MQTT connection failed", e)
                mqttClient.loop_stop()
                time.sleep(TIMEOUT_CONNECTION)
                i = 2
        else:
            i = 1


def handleConnectToWebSocket():
    _LOGGER.info("Handling Web Socket connection...")
    wsClient.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


yaml.add_multi_constructor("", any_constructor, Loader=yaml.SafeLoader)
configuration = yaml.safe_load(configFile)

mqttClient = mqtt.Client(
    client_id=mqttClientId,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv31,
    transport="tcp",
)

mqttClient.broker = configuration["ip_broker_freehands"]
mqttClient.keepalive = 60
mqttClient.on_connect = mqtt_on_connect
mqttClient.on_message = mqtt_on_message
mqttClient.on_publish = mqtt_on_publish
mqttClient.on_socket_close = mqtt_on_socket_close
mqttClient.on_socket_open = mqtt_on_socket_open
mqttClient.port = configuration["port_broker_freehands"]
mqttClient.topic = "#"

mqttClient.enable_logger(logger=_LOGGER)
mqttClient.username_pw_set(
    configuration["username_broker_freehands"], configuration["password"]
)

# websocket.enableTrace(True)
wsClient = websocket.WebSocketApp(
    url=str(configuration["ip_broker_gateway"]),
    on_close=websocket_on_close,
    on_error=websocket_on_error,
    on_message=websocket_on_message,
    on_open=websocket_on_open,
)

# connectToBroker()
connectToMQTT()
connectToWebSocket()
scheduledFunction()
#log_active_threads()

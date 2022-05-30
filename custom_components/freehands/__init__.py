"""
Custom integration to integrate freeHands with Home Assistant.

For more details about this integration, please refer to
https://github.com/riveccia/freehands
"""
import _thread
import asyncio
from datetime import timedelta, datetime
import json
import logging
import random
from sqlite3 import Timestamp
import time
import threading


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
from .const import Subs
from .const import EventsSub
from .const import STARTUP_MESSAGE
from .const import PLATFORMS
from .const import DOMAIN
from .const import CONF_USERNAME
from .const import CONF_PASSWORD

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

file = open(r"/config/gateway_conf.yaml", encoding="utf8")


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

############# BROKER FUNCTIONS ####################


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("freeHands connected to MQTT Broker!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_connectToFreehands(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("connected!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    _LOGGER.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    for x in Subs:
        if (x["Subtopic"] in msg.topic) or (x["Subtopic"] == msg.topic):
            if msg.payload.decode() == x["Payload"]:
                message_routing(client, "#", x["Command"])


def message_routing(client, topic, msg):
    global id
    try:
        if client.url in "wss://appforgood.duckdns.org/api/websocket":
            if isinstance(msg, str):
                client1.publish(topic=topic, payload=msg)
            else:
                client1.publish(topic=topic, payload=json.dumps(msg))
    except:
        print("no ws")
    try:
        if client._client_id.decode("utf-8") == clientToFreeHands_id:
            id = id + 1
            target = {"entity_id": msg["entity_id"]}
            command = {
                "id": id,
                "type": "call_service",
                "domain": msg["domain"],
                "service": msg["service"],
                "target": target,
            }
            ws.send(json.dumps(command))
    except:
        print("no mqtt")


def on_publish(client, userdata, result):
    print("data published  \n" + str(result) + "RESULT \n")
    pass


############# BROKER FUNCTIONS ####################


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


############# WS FUNCTIONS ####################


def on_messagews(ws, message):
    data = json.loads(message)
    arrStructureJson = []
    if data["type"] == "event":
        filteredObject = {}
        customTopics = {}
        print(data["event"]["data"]["new_state"]["attributes"]["friendly_name"])
        print("ciao")
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
                    if key in x["key"]:
                        if value is True:
                            value = "true"
                        if value is False:
                            value = "false"
                        if is_float(value):
                            value = str(value)
                        if is_integer(value):
                            value = str(float(value))

                        filteredObject[key] = value
                        if (
                            "sensor.shelly_shem_c45bbe7822e8_2_current_consumption"
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
                            arrStructureJson.append(messageToAppend)
                        messageToAppend = {"key": key, "value": value}
                        arrStructureJson.append(messageToAppend)
                timestamp = time.time()
                dt = int(timestamp)
                print("dt", str(dt))
                dataToSend = {"detections": arrStructureJson, "timestamp": dt}
                if filteredObject != {} or message != null or arrStructureJson != []:
                    message_routing(ws, x["Topic_out"], dataToSend)
                    try:
                        for topicCustom in x["Topic_out_custom"]:
                            for key, value in dict.items(filteredObject):
                                if key == topicCustom["key"]:
                                    msg = (
                                        '{"value": "'
                                        + str(filteredObject[key]).lower()
                                        + '"}'
                                    )
                                    # _LOGGER.info("messaggio singolo" + str(msg))
                                    message_routing(ws, topicCustom["Topic_out"], msg)
                    except KeyError:
                        print("NO CUSTOM TOPICS")
    else:
        print("ciao")


def on_errorws(ws, error):
    print(error)


def on_closews(ws, close_status_code, close_msg):
    print("Reconnecting")
    connectToBroker()


def on_openws(ws):
    global id
    ws.send(json.dumps(configuration["LoginToWs"]))
    print("Auth effettuato")
    ws.send(
        json.dumps({"id": 1, "type": "subscribe_events", "event_type": "state_changed"})
    )
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

client1.connect(client1.broker, client1.port, client1.keepalive)
client1.loop_start()

connectToBroker()

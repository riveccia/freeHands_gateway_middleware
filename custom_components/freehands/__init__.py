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
import time

import jsonpickle
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
from sqlalchemy import null
import websocket
import yaml

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

import yaml

file = open(r"config/gateway_conf.yaml", encoding="utf8")


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


yaml.add_multi_constructor("", any_constructor, Loader=yaml.SafeLoader)
configuration = yaml.safe_load(file)
print(configuration)

# configEntity = yaml.full_load(open("config/configuration.yaml", "r"))

from .api import FreehandsApiClient
from .const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    DOMAIN,
    PLATFORMS,
    STARTUP_MESSAGE,
    EventsSub,
    Topics
)

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


# generate client ID with pub prefix randomly
clientToFreeHands_id = f"freehands-mqtt-{random.randint(0, 1000)}"

############# BROKER FUNCTIONS ####################


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("freeHands connected to MQTT Broker!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_connectToFreehands(client, userdata, flags, rc):
    if rc == 0:
        _LOGGER.info("djahsdkjhaskjdhkajshdkjashdkajshdkajshd!")
        client.subscribe("#")
    else:
        _LOGGER.info("freeHands failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    _LOGGER.info(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


def message_routing(client, topic, msg):

    if client.url in "ws://192.168.3.122:8123/api/websocket":
        print("PAYLOAD :" + str(msg))
        print("TOPIC: " + topic)
        client1.publish(topic=topic, payload=json.dumps(msg))
    elif client._client_id.decode("utf-8") == clientToFreeHands_id:
        print("ciao")


def on_publish(client, userdata, result):
    print("data published  \n" + str(result) + "RESULT \n")
    pass


############# BROKER FUNCTIONS ####################


############# WS FUNCTIONS ####################


def on_messagews(ws, message):
    data = json.loads(message)
    if data["type"] == "event":
        filteredObject = {}
        customTopics = {}
        for x in Topics:
            if (
                x["Topic_in"]
                in data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
            ) or (
                x["Topic_in"]
                == data["event"]["data"]["new_state"]["attributes"]["friendly_name"]
            ):
                print(data["event"]["data"]["new_state"]["attributes"]["friendly_name"])
                print(data)

                for key, value in dict.items(
                    data["event"]["data"]["new_state"]["attributes"]
                ):
                    if key in x["key"]:
                        filteredObject[key] = value

                print("\nfil  " + str(filteredObject) + "\n")
                if filteredObject != {}:
                    message_routing(ws, x["Topic_out"], filteredObject)

                try:
                    for topicCustom in x["Topic_custom"]:
                        for key, value in dict.items(filteredObject):
                            if key == topicCustom["key"]:
                                print("MESSAGGIO FILTRATO PER OGNI KEY")
                                print(
                                    "\n chiave: "
                                    + str(key)
                                    + " valore : "
                                    + str(filteredObject[key])
                                )
                                print(
                                    "\n \n TOPIC CUSTOM DI USCITA : "
                                    + str(topicCustom["Topic_out"])
                                    + "\n"
                                )
                                msg = (
                                    '{"value": "'
                                    + str(filteredObject[key]).lower()
                                    + '"}'
                                )
                                message_routing(ws, topicCustom["Topic_out"], msg)

                    # for key in x["key"]:
                    #     # objectToTopicOut[key] = data["event"]["data"]["new_state"]["attributes"][key]

                    #     objectToTopicOut = json.load(
                    #         {key: data["event"]["data"]["new_state"]["attributes"][key]}
                    #     )
                except KeyError:
                    print("NO CUSTOM TOPICS")


def on_errorws(ws, error):
    print(error)


def on_closews(ws, close_status_code, close_msg):
    print("Reconnecting")
    connectToBroker()


def on_openws(ws):
    ws.send(
        json.dumps(configuration["LoginToWs"])
    )  # json.dumps({"type": "auth","access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI5NGQ4ZDMwYWMzNzQ0MDhkODM4YzZjNTY3MzFmNDhlYSIsImlhdCI6MTY1MDUzMTU5MiwiZXhwIjoxOTY1ODkxNTkyfQ.wGqiJhLJ_2YHgbuyC96iAM4K5v20L-1KYJJhVmRUCKA",})
    print("Auth effettuato")
    ws.send(
        json.dumps(EventsSub)
    )  # json.dumps({"id": 18, "type": "subscribe_events", "event_type": "state_changed"})
    print("Sottoscrizione agli eventi effetuata")
    print("connected")


############# WS FUNCTIONS ####################

############# CONNECTIONS ####################


def connectToBroker():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://192.168.3.122:8123/api/websocket",
        on_open=on_openws,
        on_message=on_messagews,
        on_error=on_errorws,
        on_close=on_closews,
    )
    ws.run_forever()


# def connectToFreehands():
#     client1 = mqtt.Client(
#         client_id=clientToFreeHands_id,
#         clean_session=True,
#         userdata=None,
#         protocol=mqtt.MQTTv31,
#         transport="tcp",
#     )
#     client1.username_pw_set("pippo", "pluto")
#     # client1.username_pw_set(
#     #     FreehandsConfiguration["Username"], FreehandsConfiguration["Password"]
#     # )
#     client1.on_connect = on_connectToFreehands
#     client1.on_message = on_message
#     client1.on_publish = on_publish
#     client1.broker = "192.168.3.63" #Freehands["Mqtt_ip"]
#     client1.port = 51885  # FreehandsConfiguration["Mqtt_port"]
#     client1.topic = "#"
#     client1.keepalive = 60

#     # client1.connect(client1.broker, client1.port, client1.keepalive)
#     # client1.loop_start()


############# CONNECTIONS ####################

client1 = mqtt.Client(
    client_id=clientToFreeHands_id,
    clean_session=True,
    userdata=None,
    protocol=mqtt.MQTTv31,
    transport="tcp",
)
# client1.username_pw_set("pippo", "pluto")
client1.username_pw_set(
    configuration["username_broker_freehands"], configuration["password"]
)
# client1.username_pw_set(
#     FreehandsConfiguration["Username"], FreehandsConfiguration["Password"]
# )
client1.on_connect = on_connectToFreehands
client1.on_message = on_message
client1.on_publish = on_publish
client1.broker = configuration[
    "ip_broker_freehands"
]  # FreehandsConfiguration["Mqtt_ip"]
client1.port = configuration[
    "port_broker_freehands"
]  # FreehandsConfiguration["Mqtt_port"]
client1.topic = "#"
client1.keepalive = 60

client1.connect(client1.broker, client1.port, client1.keepalive)
client1.loop_start()

connectToBroker()

# connectToFreehands()



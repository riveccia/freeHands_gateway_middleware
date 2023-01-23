"""Constants for the freehandsmiddleware integration."""

import yaml

file = open(r"/config/gateway_conf.yaml", encoding="utf8")


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


yaml.add_multi_constructor("", any_constructor, Loader=yaml.SafeLoader)
configuration = yaml.safe_load(file)

tenantIdentificationCode = str(
    configuration["tenantIdentificationCode"]
)  # = "appforgood"

companyIdentificationCode = str(
    configuration["companyIdentificationCode"]
)  # = "appforgood_matera"

gatewayTag = str(configuration["gatewayTag"])  # "gateway_6"


DOMAIN = "freehands"

BROKER = "192.168.3.122"
PORT = "1883"
TOPIC = "zigbee2mqtt/+"
USERNAME = "mqtt_user"
PASSWORD = "%%7!P6C6zji@VADv"
URI = "mqtt://" + USERNAME + ":" + PASSWORD + "@" + BROKER + "." + PORT


"""Constants for freeHands."""
# Base component constants
NAME = "freeHands"
DOMAIN = "freehands"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/riveccia/freehands/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

########### Gateway Settings ###########

EventsSub = {"id": 1, "type": "subscribe_events", "event_type": "state_changed"}


# {
#     "Subtopic" : "appforgood/appforgood_matera/gateway_6/Button_1/click/set",
#     "Payload" : "click",
#     "Command" : {
#         "domain": "switch",
#         "service": "turn_on",
#         "entity_id": "sensor.button_1_click"
#     }
# }
########### Publics to backend ###########

Pubs = [
    ########### AirQualitySensor_1 ###########
    {
        "Friedly_name": "AirQualitySensor_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/AirQualitySensor_1/get",
        "key": [
            "voc",
            "temperature",
            "humidity",
            "battery",
            "battery_low",
            "air_quality",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_1/temperature/get",
            },
            {
                "key": "humidity",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_1/humidity/get",
            },
            {
                "key": "air_quality",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_1/air_quality/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_1/battery_low/get",
            },
        ],
    },
    ########### AirQualitySensor_2 ###########
    {
        "Friedly_name": "AirQualitySensor_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/AirQualitySensor_2/get",
        "key": [
            "voc",
            "temperature",
            "humidity",
            "battery",
            "battery_low",
            "air_quality",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_2/temperature/get",
            },
            {
                "key": "humidity",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_2/humidity/get",
            },
            {
                "key": "air_quality",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_2/air_quality/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_2/battery_low/get",
            },
        ],
    },
    ########### AirQualitySensor_3 ###########
    {
        "Friedly_name": "AirQualitySensor_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/AirQualitySensor_3/get",
        "key": [
            "voc",
            "temperature",
            "humidity",
            "battery",
            "battery_low",
            "air_quality",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_3/temperature/get",
            },
            {
                "key": "humidity",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_3/humidity/get",
            },
            {
                "key": "air_quality",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_3/air_quality/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_3/battery_low/get",
            },
        ],
    },
    ########### AirQualitySensor_4 ###########
    {
        "Friedly_name": "AirQualitySensor_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/AirQualitySensor_4/get",
        "key": [
            "voc",
            "temperature",
            "humidity",
            "battery",
            "battery_low",
            "air_quality",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_4/temperature/get",
            },
            {
                "key": "humidity",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_4/humidity/get",
            },
            {
                "key": "air_quality",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_4/air_quality/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_4/battery_low/get",
            },
        ],
    },
    ########### AirQualitySensor_5 ###########
    {
        "Friedly_name": "AirQualitySensor_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/AirQualitySensor_5/get",
        "key": [
            "voc",
            "temperature",
            "humidity",
            "battery",
            "battery_low",
            "air_quality",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_5/temperature/get",
            },
            {
                "key": "humidity",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_5/humidity/get",
            },
            {
                "key": "air_quality",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_5/air_quality/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/AirQualitySensor_5/battery_low/get",
            },
        ],
    },
    ########### Button_1 ###########
    {
        "Friedly_name": "Button_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_1/get",
        "key": ["battery", "link_quality", "action"],
        "Topic_out_custom": [
            {
                "key": "action",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Button_1/state/get",
            }
        ],
    },
    ########### Button_2 ###########
    {
        "Friedly_name": "Button_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_2/get",
        "key": ["battery", "link_quality", "action"],
        "Topic_out_custom": [
            {
                "key": "action",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Button_2/state/get",
            }
        ],
    },
    ########### Button_3 ###########
    {
        "Friedly_name": "Button_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_3/get",
        "key": ["battery", "link_quality", "action"],
        "Topic_out_custom": [
            {
                "key": "action",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Button_3/state/get",
            }
        ],
    },
    ########### Button_4 ###########
    {
        "Friedly_name": "Button_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_4/get",
        "key": ["battery", "link_quality", "action"],
        "Topic_out_custom": [
            {
                "key": "action",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Button_4/state/get",
            }
        ],
    },
    ########### Button_5 ###########
    {
        "Friedly_name": "Button_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_5/get",
        "key": ["battery", "link_quality", "action"],
        "Topic_out_custom": [
            {
                "key": "action",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Button_5/state/get",
            }
        ],
    },
    ########### EnergyMeter_1 ###########
    {
        "Friedly_name": "EnergyMeter_1-2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_1/get",
        "key": ["current_consumption", "total_consumption"],
        "Topic_out_custom": [
            {
                "key": "current_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_1/current_consumption/get",
            },
            {
                "key": "total_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_1/total_consumption/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_1/battery_low/get",
            },
        ],
    },
    ########### EnergyMeter_2 ###########
    {
        "Friedly_name": "EnergyMeter_2-2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_2/get",
        "key": ["current_consumption", "total_consumption"],
        "Topic_out_custom": [
            {
                "key": "current_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_2/current_consumption/get",
            },
            {
                "key": "total_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_2/total_consumption/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_2/battery_low/get",
            },
        ],
    },
    ########### EnergyMeter_3 ###########
    {
        "Friedly_name": "EnergyMeter_3-2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_3/get",
        "key": ["current_consumption", "total_consumption"],
        "Topic_out_custom": [
            {
                "key": "current_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_3/current_consumption/get",
            },
            {
                "key": "total_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_3/total_consumption/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_3/battery_low/get",
            },
        ],
    },
    ########### EnergyMeter_4 ###########
    {
        "Friedly_name": "EnergyMeter_4-2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_4/get",
        "key": ["current_consumption", "total_consumption"],
        "Topic_out_custom": [
            {
                "key": "current_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_4/current_consumption/get",
            },
            {
                "key": "total_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_4/total_consumption/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_4/battery_low/get",
            },
        ],
    },
    ########### EnergyMeter_5 ###########
    {
        "Friedly_name": "EnergyMeter_5-2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_5/get",
        "key": ["current_consumption", "total_consumption"],
        "Topic_out_custom": [
            {
                "key": "current_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_5/current_consumption/get",
            },
            {
                "key": "total_consumption",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_5/total_consumption/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/EnergyMeter_5/battery_low/get",
            },
        ],
    },
    ########### HeatAlarm_1 ###########
    {
        "Friedly_name": "HeatAlarm_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_1/get",
        "key": [
            "temperature",
            "battery",
            "smoke",
            "battery_low",
            "alarm",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_1/temperature/get",
            },
            {
                "key": "smoke",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_1/state/get",
            },
            {
                "key": "alarm",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_1/alarm/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_1/battery_low/get",
            },
        ],
    },
    ########### HeatAlarm_2 ###########
    {
        "Friedly_name": "HeatAlarm_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_2/get",
        "key": [
            "temperature",
            "battery",
            "smoke",
            "battery_low",
            "alarm",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_2/temperature/get",
            },
            {
                "key": "smoke",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_2/state/get",
            },
            {
                "key": "alarm",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_2/alarm/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_2/battery_low/get",
            },
        ],
    },
    ########### HeatAlarm_3 ###########
    {
        "Friedly_name": "HeatAlarm_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_3/get",
        "key": [
            "temperature",
            "battery",
            "smoke",
            "battery_low",
            "alarm",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_3/temperature/get",
            },
            {
                "key": "smoke",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_3/state/get",
            },
            {
                "key": "alarm",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_3/alarm/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_3/battery_low/get",
            },
        ],
    },
    ########### HeatAlarm_4 ###########
    {
        "Friedly_name": "HeatAlarm_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_4/get",
        "key": [
            "temperature",
            "battery",
            "smoke",
            "battery_low",
            "alarm",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_4/temperature/get",
            },
            {
                "key": "smoke",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_4/state/get",
            },
            {
                "key": "alarm",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_4/alarm/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_4/battery_low/get",
            },
        ],
    },
    ########### HeatAlarm_5 ###########
    {
        "Friedly_name": "HeatAlarm_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_5/get",
        "key": [
            "temperature",
            "battery",
            "smoke",
            "battery_low",
            "alarm",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_5/temperature/get",
            },
            {
                "key": "smoke",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_5/state/get",
            },
            {
                "key": "alarm",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_5/alarm/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/HeatAlarm_5/battery_low/get",
            },
        ],
    },
    ########### MotionSensor_1 ###########
    {
        "Friedly_name": "MotionSensor_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/MotionSensor_1/get",
        "key": [
            "occupancy",
            "battery_low",
            "tamper",
            "temperature",
            "illuminance_lux",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_1/temperature/get",
            },
            {
                "key": "illuminance_lux",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_1/illuminance_lux/get",
            },
            {
                "key": "occupancy",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_1/occupancy/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_1/battery_low/get",
            },
        ],
    },
    ########### MotionSensor_2 ###########
    {
        "Friedly_name": "MotionSensor_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/MotionSensor_2/get",
        "key": [
            "occupancy",
            "battery_low",
            "tamper",
            "temperature",
            "illuminance_lux",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_2/temperature/get",
            },
            {
                "key": "illuminance_lux",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_2/illuminance_lux/get",
            },
            {
                "key": "occupancy",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_2/occupancy/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_2/battery_low/get",
            },
        ],
    },
    ########### MotionSensor_3 ###########
    {
        "Friedly_name": "MotionSensor_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/MotionSensor_3/get",
        "key": [
            "occupancy",
            "battery_low",
            "tamper",
            "temperature",
            "illuminance_lux",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_3/temperature/get",
            },
            {
                "key": "illuminance_lux",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_3/illuminance_lux/get",
            },
            {
                "key": "occupancy",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_3/occupancy/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_3/battery_low/get",
            },
        ],
    },
    ########### MotionSensor_4 ###########
    {
        "Friedly_name": "MotionSensor_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/MotionSensor_4/get",
        "key": [
            "occupancy",
            "battery_low",
            "tamper",
            "temperature",
            "illuminance_lux",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_4/temperature/get",
            },
            {
                "key": "illuminance_lux",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_4/illuminance_lux/get",
            },
            {
                "key": "occupancy",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_4/occupancy/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_4/battery_low/get",
            },
        ],
    },
    ########### MotionSensor_5 ###########
    {
        "Friedly_name": "MotionSensor_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/MotionSensor_5/get",
        "key": [
            "occupancy",
            "battery_low",
            "tamper",
            "temperature",
            "illuminance_lux",
            "link_quality",
        ],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_5/temperature/get",
            },
            {
                "key": "illuminance_lux",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_5/illuminance_lux/get",
            },
            {
                "key": "occupancy",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_5/occupancy/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/MotionSensor_5/battery_low/get",
            },
        ],
    },
    ########### SleepTracker_1 ###########
    {
        "Friedly_name": "SleepTracker_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SleepTracker_1/get",
        "key": [
            "withings_sleep_breathing_disturbances_intensity",
            "withings_sleep_deep_duration_seconds",
            "withings_sleep_heart_rate_average_bpm",
            "withings_sleep_heart_rate_max_bpm",
            "withings_sleep_heart_rate_min",
            "withings_sleep_light_duration_seconds",
            "withings_sleep_rem_duration_seconds",
            "withings_sleep_respiratory_average_bpm",
            "withings_sleep_respiratory_max_bpm",
            "withings_sleep_respiratory_min_bpm",
            "withings_sleep_score",
            "withings_sleep_snoring_eposode_count",
            "withings_sleep_snoring",
            "withings_sleep_tosleep_duration_seconds",
            "withings_sleep_towakeup_duration_seconds",
            "withings_sleep_wakeup_count",
            "withings_sleep_wakeup_duration_seconds",
            "withings_heart_pulse_bpm",
            "withings_in_bed",
        ],
        "Topic_out_custom": [
            {
                "key": "withings_in_bed",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SleepTracker_1/occupancy/get",
            }
        ],
    },
    ########### SmartLight_1 ###########
    {
        "Friedly_name": "SmartLight_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLight_1/get",
        "key": ["state"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartLight_1/state/get",
            }
        ],
    },
    ########### SmartPlug_1 ##########
    {
        "Friedly_name": "SmartPlug_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_1/get",
        "key": ["current", "energy", "state", "power", "link_quality", "voltage"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartPlug_1/state/get",
            }
        ],
    },
    ########### SmartPlug_2 ##########
    {
        "Friedly_name": "SmartPlug_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_2/get",
        "key": ["current", "energy", "state", "power", "link_quality", "voltage"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartPlug_2/state/get",
            }
        ],
    },
    ########### SmartPlug_3 ##########
    {
        "Friedly_name": "SmartPlug_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_3/get",
        "key": ["current", "energy", "state", "power", "link_quality", "voltage"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/SmartPlug_3/state/get",
            }
        ],
    },
    ########### Thermovalve_1 ##########
    {
        "Friedly_name": "Thermovalve_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/get",
        "key": [
            "battery_low",  # true /false
            "child_lock",  # lock unlock  = lock
            "open_window",  # on off  = switch
            "local_temperature",  # float
            "comfort_temperature",  # float = number
            "frost_protection",  # on off = switch
            "link_quality",  # int
            "heating_stop",  # on off = switch
            "online",  # on off = switch
        ],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_1/state/get",
            },
            {
                "key": "local_temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_1/temperature/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_1/battery_low/get",
            },
        ],
    },
    ########### Thermovalve_2 ##########
    {
        "Friedly_name": "Thermovalve_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/get",
        "key": [
            "battery_low",
            "child_lock",
            "open_window",
            "local_temperature",
            "comfort_temperature",
            "frost_protection",
            "link_quality",
            "heating_stop",
            "online",
        ],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_2/state/get",
            },
            {
                "key": "local_temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_2/temperature/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_2/battery_low/get",
            },
        ],
    },
    ########### Thermovalve_3 ##########
    {
        "Friedly_name": "Thermovalve_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/get",
        "key": [
            "battery_low",
            "child_lock",
            "open_window",
            "local_temperature",
            "comfort_temperature",
            "frost_protection",
            "link_quality",
            "heating_stop",
            "online",
        ],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_3/state/get",
            },
            {
                "key": "local_temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_3/temperature/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_3/battery_low/get",
            },
        ],
    },
    ########### Thermovalve_4 ##########
    {
        "Friedly_name": "Thermovalve_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/get",
        "key": [
            "battery_low",
            "child_lock",
            "open_window",
            "local_temperature",
            "comfort_temperature",
            "frost_protection",
            "link_quality",
            "heating_stop",
            "online",
        ],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_4/state/get",
            },
            {
                "key": "local_temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_4/temperature/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_4/battery_low/get",
            },
        ],
    },
    ########### Thermovalve_5 ##########
    {
        "Friedly_name": "Thermovalve_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/get",
        "key": [
            "battery_low",
            "child_lock",
            "open_window",
            "local_temperature",
            "comfort_temperature",
            "frost_protection",
            "link_quality",
            "heating_stop",
            "online",
        ],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_5/state/get",
            },
            {
                "key": "local_temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_5/temperature/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Thermovalve_5/battery_low/get",
            },
        ],
    },
    ########### WaterLeakDetector_1 ##########
    {
        "Friedly_name": "WaterLeakDetector_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WaterLeakDetector_1/get",
        "key": ["tamper", "battery_low", "water_leak", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_1/temperature/get",
            },
            {
                "key": "water_leak",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_1/state/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_1/battery_low/get",
            },
        ],
    },
    ########### WaterLeakDetector_2 ##########
    {
        "Friedly_name": "WaterLeakDetector_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WaterLeakDetector_2/get",
        "key": ["tamper", "battery_low", "water_leak", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_2/temperature/get",
            },
            {
                "key": "water_leak",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_2/state/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_2/battery_low/get",
            },
        ],
    },
    ########### WaterLeakDetector_3 ##########
    {
        "Friedly_name": "WaterLeakDetector_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WaterLeakDetector_3/get",
        "key": ["tamper", "battery_low", "water_leak", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_3/temperature/get",
            },
            {
                "key": "water_leak",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_3/state/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WaterLeakDetector_3/battery_low/get",
            },
        ],
    },
    ########### WindowSensor_1 ##########
    {
        "Friedly_name": "WindowSensor_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WindowSensor_1/get",
        "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_1/temperature/get",
            },
            {
                "key": "contact",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_1/contact/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_1/battery_low/get",
            },
        ],
    },
    ########### WindowSensor_2 ##########
    {
        "Friedly_name": "WindowSensor_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WindowSensor_2/get",
        "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_2/temperature/get",
            },
            {
                "key": "contact",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_2/contact/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_2/battery_low/get",
            },
        ],
    },
    ########### WindowSensor_3 ##########
    {
        "Friedly_name": "WindowSensor_3",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WindowSensor_3/get",
        "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_3/temperature/get",
            },
            {
                "key": "contact",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_3/contact/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_3/battery_low/get",
            },
        ],
    },
    ########### WindowSensor_4 ##########
    {
        "Friedly_name": "WindowSensor_4",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WindowSensor_4/get",
        "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_4/temperature/get",
            },
            {
                "key": "contact",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_4/contact/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_4/battery_low/get",
            },
        ],
    },
    ########### WindowSensor_5 ##########
    {
        "Friedly_name": "WindowSensor_5",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/WindowSensor_5/get",
        "key": ["contact", "battery_low", "tamper", "temperature", "link_quality"],
        "Topic_out_custom": [
            {
                "key": "temperature",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_5/temperature/get",
            },
            {
                "key": "contact",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_5/contact/get",
            },
            {
                "key": "battery_low",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/WindowSensor_5/battery_low/get",
            },
        ],
    },
    ########### Television_1 ###########
    {
        "Friedly_name": "Television_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_1/get",
        "key": ["state"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Television_1/state/get",
            },
        ],
    },
    ########### Television_2 ###########
    {
        "Friedly_name": "Television_2",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_2/get",
        "key": ["state"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Television_2/state/get",
            },
        ],
    },
    ########### /Television_1 ###########
]


########### Subscribes from backend ###########

Subs = [
    ############# CUSTOM RESTART HOMEASSISTANT #############
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Restar_HA/set",
        "Payload": "",
        "Command": {
            "domain": "homeassistant",
            "service": "restart",
            "entity_id": "homeassistant.restart",
        },
    },
    ########### Button_1 ###########
    # Button_1_Click # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_1/click/set",
        "Payload": "click",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "sensor.button_1_click",
        },
    },
    ########### Button_2 ###########
    # Button_2_Click # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_2/click/set",
        "Payload": "click",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "sensor.button_2_click",
        },
    },
    ########### Button_3 ###########
    # Button_3_Click # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_3/click/set",
        "Payload": "click",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "sensor.button_3_click",
        },
    },
    ########### Button_4 ###########
    # Button_4_Click # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_4/click/set",
        "Payload": "click",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "sensor.button_4_click",
        },
    },
    ########### Button_5 ###########
    # Button_5_Click # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Button_5/click/set",
        "Payload": "click",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "sensor.button_5_click",
        },
    },
    ########### SmartLight_1 ###########
    # SmartLight_1_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLight_1/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "light",
            "service": "turn_on",
            "entity_id": "light.smartlight_1",
        },
    },
    # SmartLight_1_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLight_1/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "light",
            "service": "turn_off",
            "entity_id": "light.smartlight_1",
        },
    },
    # SmartLight_1_Brightness #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLight_1/brightness/set",
        "Payload": "",
        "Command": {
            "domain": "light",
            "service": "turn_on",
            "entity_id": "light.smartlight_1",
        },
    },
    # SmartLight_1_Color #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLight_1/color/set",
        "Payload": "",
        "Command": {
            "domain": "light",
            "service": "turn_on",
            "entity_id": "light.smartlight_1",
        },
    },
    ########### SmartPlug_1 ##########
    # SmartPlug_1_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_1/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.smartplug_1",
        },
    },
    # SmartPlug_1_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_1/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.smartplug_1",
        },
    },
    ########### SmartPlug_2 ##########
    # SmartPlug_2_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_2/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.smartplug_2",
        },
    },
    # SmartPlug_2_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_2/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.smartplug_2",
        },
    },
    ########### SmartPlug_3 ##########
    # SmartPlug_3_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_3/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.smartplug_3",
        },
    },
    # SmartPlug_3_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartPlug_3/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.smartplug_3",
        },
    },
    ########### Thermovalve_1 ##########
    # Thermovalve_1_ChildLock_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/child_lock/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.thermovalve_1_child_lock",
        },
    },
    # Thermovalve_1_ChildLock_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/child_lock/set",
        "Payload": "unlock",
        "Command": {
            "domain": "switch",
            "service": "unlock",
            "entity_id": "lock.thermovalve_1_child_lock",
        },
    },
    # Thermovalve_1_Preset #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "number",
            "service": "set_value",
            "entity_id": "number.thermovalve_1_comfort_temperature",
        },  # TODO: fare custom set
    },
    # Thermovalve_1_Frost_protection_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/frost_protection/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_1_frost_protection",
        },
    },
    # Thermovalve_1_Frost_protection_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/frost_protection/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_1_frost_protection",
        },
    },
    # Thermovalve_1_heating_stop_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/heating_stop/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_1_heating_stop",
        },
    },
    # Thermovalve_1_heating_stop_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/heating_stop/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_1_heating_stop",
        },
    },
    # Thermovalve_1_Online_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/online/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_1_online",
        },
    },
    # Thermovalve_1_Online_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_1/online/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_1_online",
        },
    },
    ########### Thermovalve_2 ##########
    # Thermovalve_2_ChildLock_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/child_lock/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.thermovalve_2_child_lock",
        },
    },
    # Thermovalve_2_ChildLock_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/child_lock/set",
        "Payload": "unlock",
        "Command": {
            "domain": "switch",
            "service": "unlock",
            "entity_id": "lock.thermovalve_2_child_lock",
        },
    },
    # Thermovalve_2_Preset #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "number",
            "service": "set_value",
            "entity_id": "number.thermovalve_2_comfort_temperature",
        },  # TODO: fare custom set
    },
    # Thermovalve_2_Frost_protection_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/frost_protection/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_2_frost_protection",
        },
    },
    # Thermovalve_2_Frost_protection_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/frost_protection/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_2_frost_protection",
        },
    },
    # Thermovalve_2_heating_stop_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/heating_stop/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_2_heating_stop",
        },
    },
    # Thermovalve_2_heating_stop_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/heating_stop/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_2_heating_stop",
        },
    },
    # Thermovalve_2_Online_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/online/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_2_online",
        },
    },
    # Thermovalve_2_Online_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_2/online/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_2_online",
        },
    },
    ########### Thermovalve_3 ##########
    # Thermovalve_3_ChildLock_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/child_lock/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.thermovalve_3_child_lock",
        },
    },
    # Thermovalve_3_ChildLock_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/child_lock/set",
        "Payload": "unlock",
        "Command": {
            "domain": "switch",
            "service": "unlock",
            "entity_id": "lock.thermovalve_3_child_lock",
        },
    },
    # Thermovalve_3_Preset #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "number",
            "service": "set_value",
            "entity_id": "number.thermovalve_3_comfort_temperature",
        },  # TODO: fare custom set
    },
    # Thermovalve_3_Frost_protection_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/frost_protection/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_3_frost_protection",
        },
    },
    # Thermovalve_3_Frost_protection_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/frost_protection/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_3_frost_protection",
        },
    },
    # Thermovalve_3_heating_stop_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/heating_stop/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_3_heating_stop",
        },
    },
    # Thermovalve_3_heating_stop_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/heating_stop/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_3_heating_stop",
        },
    },
    # Thermovalve_3_Online_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/online/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_3_online",
        },
    },
    # Thermovalve_3_Online_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_3/online/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_3_online",
        },
    },
    ########### Thermovalve_4 ##########
    # Thermovalve_4_ChildLock_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/child_lock/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.thermovalve_4_child_lock",
        },
    },
    # Thermovalve_4_ChildLock_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/child_lock/set",
        "Payload": "unlock",
        "Command": {
            "domain": "switch",
            "service": "unlock",
            "entity_id": "lock.thermovalve_4_child_lock",
        },
    },
    # Thermovalve_4_Preset #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "number",
            "service": "set_value",
            "entity_id": "number.thermovalve_4_comfort_temperature",
        },  # TODO: fare custom set
    },
    # Thermovalve_4_Frost_protection_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/frost_protection/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_4_frost_protection",
        },
    },
    # Thermovalve_4_Frost_protection_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/frost_protection/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_4_frost_protection",
        },
    },
    # Thermovalve_4_heating_stop_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/heating_stop/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_4_heating_stop",
        },
    },
    # Thermovalve_4_heating_stop_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/heating_stop/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_4_heating_stop",
        },
    },
    # Thermovalve_4_Online_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/online/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_4_online",
        },
    },
    # Thermovalve_4_Online_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_4/online/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_4_online",
        },
    },
    ########### Thermovalve_5 ##########
    # Thermovalve_5_ChildLock_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/child_lock/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.thermovalve_5_child_lock",
        },
    },
    # Thermovalve_5_ChildLock_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/child_lock/set",
        "Payload": "unlock",
        "Command": {
            "domain": "switch",
            "service": "unlock",
            "entity_id": "lock.thermovalve_5_child_lock",
        },
    },
    # Thermovalve_5_Preset #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "number",
            "service": "set_value",
            "entity_id": "number.thermovalve_5_comfort_temperature",
        },  # TODO: fare custom set
    },
    # Thermovalve_5_Frost_protection_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/frost_protection/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_5_frost_protection",
        },
    },
    # Thermovalve_5_Frost_protection_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/frost_protection/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_5_frost_protection",
        },
    },
    # Thermovalve_5_heating_stop_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/heating_stop/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_5_heating_stop",
        },
    },
    # Thermovalve_5_heating_stop_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/heating_stop/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_5_heating_stop",
        },
    },
    # Thermovalve_5_Online_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/online/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.thermovalve_5_online",
        },
    },
    # Thermovalve_5_Online_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Thermovalve_5/online/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.thermovalve_5_online",
        },
    },
    ########### Television_1 ###########
    # Television_1_on
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_1/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "media_player",
            "service": "turn_on",
            "entity_id": "media_player.television_1",
        },
    },
    # Television_1_off
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_1/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "media_player",
            "service": "turn_off",
            "entity_id": "media_player.television_1",
        },
    },
    ########### Television_2 ###########
    # Television_2_on
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_2/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "media_player",
            "service": "turn_on",
            "entity_id": "media_player.television_2",
        },
    },
    # Television_2_off
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_2/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "media_player",
            "service": "turn_off",
            "entity_id": "media_player.television_2",
        },
    },
    ########### EnergyMeter_1 ########### complete
    # EnergyMeter_1_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_1/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    # EnergyMeter_1_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_1/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    ########### EnergyMeter_2 ########### complete
    # EnergyMeter_2_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_2/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    # EnergyMeter_2_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_2/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    ########### EnergyMeter_3 ########### complete
    # EnergyMeter_3_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_3/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    # EnergyMeter_3_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_3/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    ########### EnergyMeter_4 ########### complete
    # EnergyMeter_4_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_4/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    # EnergyMeter_4_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_4/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    ########### EnergyMeter_5 ########### complete
    # EnergyMeter_5_State_on # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_5/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    # EnergyMeter_5_State_off # ok
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/EnergyMeter_5/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.shelly_shem_c45bbe7822e8",
        },
    },
    ########### Conditioner_1 ###########
    # Conditioner_1_State_On #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_1/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "script",
            "service": "conditioner_power",
            "entity_id": "script.conditioner_power",
        },
    },
    # Conditioner_1_State_Off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_1/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "script",
            "service": "turn_on",
            "entity_id": "script.conditioner_power",
        },
    },
    # Conditioner_1_Temperature #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_1/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "script",
            "service": "",
            "entity_id": "",
        },
    },
    # Conditioner_1_Operating_status #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_1/operating_status/set",
        "Payload": "-",
        "Command": {"domain": "switch", "service": "-", "entity_id": "-"},
    },
    ########### Conditioner_2 ###########
    # Conditioner_2_State_On #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_2/state/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "script",
            "service": "turn_on",
            "entity_id": "script.conditioner_power",
        },
    },
    # Conditioner_2_State_Off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_2/state/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "script",
            "service": "turn_on",
            "entity_id": "script.conditioner_power",
        },
    },
    # Conditioner_2_Temperature #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_2/temperature/set",
        "Payload": "",
        "Command": {
            "domain": "script",
            "service": "",
            "entity_id": "",
        },
    },
    # Conditioner_2_Operating_status #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Conditioner_2/operating_status/set",
        "Payload": "-",
        "Command": {"domain": "switch", "service": "-", "entity_id": "-"},
    },
    ########### HeatAlarm_1 ###########
    # HeatAlarm_1_StateAlarm_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_1/alarm/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.heatalarm_1_alarm",
        },
    },
    # HeatAlarm_1_StateAlarm_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_1/alarm/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.heatalarm_1_alarm",
        },
    },
    ########### HeatAlarm_2 ###########
    # HeatAlarm_2_StateAlarm_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_2/alarm/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.heatalarm_2_alarm",
        },
    },
    # HeatAlarm_2_StateAlarm_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_2/alarm/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.heatalarm_2_alarm",
        },
    },
    ########### HeatAlarm_3 ###########
    # HeatAlarm_3_StateAlarm_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_3/alarm/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.heatalarm_3_alarm",
        },
    },
    # HeatAlarm_3_StateAlarm_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_3/alarm/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.heatalarm_3_alarm",
        },
    },
    ########### HeatAlarm_4 ###########
    # HeatAlarm_4_StateAlarm_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_4/alarm/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.heatalarm_4_alarm",
        },
    },
    # HeatAlarm_4_StateAlarm_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_4/alarm/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.heatalarm_4_alarm",
        },
    },
    ########### HeatAlarm_5 ###########
    # HeatAlarm_5_StateAlarm_on #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_5/alarm/set",
        "Payload": "turn_off",
        "Command": {
            "domain": "switch",
            "service": "turn_on",
            "entity_id": "switch.heatalarm_5_alarm",
        },
    },
    # HeatAlarm_5_StateAlarm_off #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/HeatAlarm_5/alarm/set",
        "Payload": "turn_on",
        "Command": {
            "domain": "switch",
            "service": "turn_off",
            "entity_id": "switch.heatalarm_5_alarm",
        },
    },
    ########### SmartLock_1 ###########
    # SmartLock_1_lock #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLock_1/state/set",
        "Payload": "lock",
        "Command": {
            "domain": "lock",
            "service": "lock",
            "entity_id": "lock.nuki_smartlock_1_lock",
        },
    },
    # SmartLock_1_unlock #
    {
        "Subtopic": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SmartLock_1/state/set",
        "Payload": "unlock",
        "Command": {
            "domain": "lock",
            "service": "unlock",
            "entity_id": "lock.nuki_smartlock_1_lock",
        },
    },
]


##########################SleepTracker_1##########################

Routes = [
    {
        "entity_id": "_heart_pulse_bpm",
        "customRoute": "",
        "key": "withings_heart_pulse_bpm",
    },
    {
        "entity_id": "_in_bed",
        "customRoute": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/SleepTracker_1/occupancy/get",
        "key": "occupancy",
    },
    {
        "entity_id": "_sleep_deep_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_deep_duration_seconds",
    },
    {
        "entity_id": "_sleep_breathing-disturbances_intensity",
        "customRoute": "",
        "key": "withings_sleep_breathing-disturbances_intensity",
    },
    {
        "entity_id": "_sleep_breathing-disturbances_intensity",
        "customRoute": "",
        "key": "withings_sleep_breathing-disturbances_intensity",
    },
    {
        "entity_id": "_sleep_heart_rate_average_bpm",
        "customRoute": "",
        "key": "withings_heart_rate_average_bpm",
    },
    {
        "entity_id": "_sleep_heart_rate_max_bpm",
        "customRoute": "",
        "key": "withings_heart_rate_max_bpm",
    },
    {
        "entity_id": "_sleep_heart_rate_min_bpm",
        "customRoute": "",
        "key": "withings_heart_rate_min_bpm",
    },
    {
        "entity_id": "_sleep_light_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_light_duration_seconds",
    },
    {
        "entity_id": "_sleep_rem_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_rem_duration_seconds",
    },
    {
        "entity_id": "_sleep_respiratory_average_bpm",
        "customRoute": "",
        "key": "withings_sleep_respiratory_average_bpm",
    },
    {
        "entity_id": "_sleep_respiratory_max_bpm",
        "customRoute": "",
        "key": "withings_sleep_respiratory_max_bpm",
    },
    {
        "entity_id": "_sleep_respiratory_min_bpm",
        "customRoute": "",
        "key": "withings_sleep_respiratory_min_bpm",
    },
    {"entity_id": "_sleep_score", "customRoute": "", "key": "withings_sleep_score"},
    {"entity_id": "_sleep_snoring", "customRoute": "", "key": "withings_sleep_snoring"},
    {
        "entity_id": "_sleep_snoring_eposode_count",
        "customRoute": "",
        "key": "withings_sleep_snoring_eposode_count",
    },
    {
        "entity_id": "_sleep_tosleep_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_tosleep_duration_seconds",
    },
    {
        "entity_id": "_sleep_towakeup_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_towakeup_duration_seconds",
    },
    {
        "entity_id": "_sleep_wakeup_count",
        "customRoute": "",
        "key": "withings_sleep_wakeup_count",
    },
    {
        "entity_id": "_sleep_wakeup_duration_seconds",
        "customRoute": "",
        "key": "withings_sleep_wakeup_duration_seconds",
    },
]

televisionPubs = [
    {
        "Name": "television_1",
        "Topic_out": tenantIdentificationCode
        + "/"
        + companyIdentificationCode
        + "/"
        + gatewayTag
        + "/Television_1/get",
        "key": ["state"],
        "Topic_out_custom": [
            {
                "key": "state",
                "Topic_out": tenantIdentificationCode
                + "/"
                + companyIdentificationCode
                + "/"
                + gatewayTag
                + "/Television_1/state/get",
            },
        ],
    }
]


num2words = {
    17: "conditioner_diciasette",
    18: "conditioner_diciotto",
    19: "conditioner_diciannove",
    20: "conditioner_venti",
    21: "conditioner_ventuno",
    22: "conditioner_ventidue",
    23: "conditioner_ventitre",
    24: "conditioner_ventiquattro",
    25: "conditioner_venticinque",
    26: "conditioner_ventisei",
    27: "conditioner_ventisette",
    28: "conditioner_ventotto",
    29: "conditioner_ventinove",
    30: "conditioner_trenta",
}

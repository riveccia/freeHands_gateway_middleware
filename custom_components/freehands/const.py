"""Constants for the freehandsmiddleware integration."""

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

tenantIdentificationCode = "appforgood"

companyIdentificationCode = "appforgood_matera"

gatewayTag = "gateway_6"


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
    ########### WindowSensor_1 ##########
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
    ########### /Television_1 ###########
]


########### Subscribes from backend ###########

Subs = [
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
            "service": "toggle",
            "entity_id": "script.script.1654613661500",
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
            "service": "toggle",
            "entity_id": "script.script.1654613661500",
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
        "Payload": "xx.x",
        "Command": {"domain": "switch", "service": "-", "entity_id": "-"},
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
    ########### HeatAlarm_1 ###########
    # EnergyMeter_1_StateAlarm_on #
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
    # EnergyMeter_1_StateAlarm_off #
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
    # {
    #     "Subtopic": tenantIdentificationCode
    #     + "/"
    #     + companyIdentificationCode
    #     + "/"
    #     + gatewayTag
    #     + "/SmartLight_1/state/set",
    #     "Payload": "turn_off",
    #     "Command": {
    #         "domain": "light",
    #         "service": "turn_off",
    #         "entity_id": "light.smartlight_1",
    #     },
    # },
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
    # SmartLight_1_WhiteCold# ok
    # {
    #     "Subtopic": tenantIdentificationCode
    #     + "/"
    #     + companyIdentificationCode
    #     + "/"
    #     + gatewayTag
    #     + "/SmartLight_1/color/set",
    #     "Payload": "turn_on",
    #     "Command": {
    #         "domain": "script",
    #         "service": "turn_on",
    #         "entity_id": "script.1652352106785",
    #     },
    # },
    # # SmartLight_1_WhiteHot# ok
    # {
    #     "Subtopic": tenantIdentificationCode
    #     + "/"
    #     + companyIdentificationCode
    #     + "/"
    #     + gatewayTag
    #     + "/SmartLight_1/color/set",
    #     "Payload": "color_white",
    #     "Command": {
    #         "domain": "script",
    #         "service": "turn_on",
    #         "entity_id": "script.striscia_led_bianco_caldo",
    #     },
    # },
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
        },  
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
    # Thermovalve_1_Temperature #
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
        },  # TODO: custom set
    },
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
]


##########################SleepTracker_1##########################

Routes = [
    {
        "entity_id": "_pulse_wave_velocity",
        "customRoute": "",
        "key": "pulseWaveVelocity",
    },
    {"entity_id": "_spo2_pct", "customRoute": "", "key": "spo2pct"},
    {"entity_id": "_heart_pulse_bpm", "customRoute": "", "key": "heartPulseBpm"},
    {
        "entity_id": "_systolic_blood_pressure_mmhg",
        "customRoute": "",
        "key": "SystolicBlood",
    },
    {
        "entity_id": "_diastolic_blood_pressure_mmhg",
        "customRoute": "",
        "key": "DiastolicBlood",
    },
    {"entity_id": "_fat_ratio_pct", "customRoute": "", "key": "fatRatio"},
    {"entity_id": "_skin_temperature_c", "customRoute": "", "key": "skinTemperature"},
    {"entity_id": "_body_temperature_c", "customRoute": "", "key": "bodyTemperature"},
    {"entity_id": "_temperature_c", "customRoute": "", "key": "temperature"},
    {"entity_id": "_bone_mass_kg", "customRoute": "", "key": "boneMass"},
    {"entity_id": "_muscle_mass_kg", "customRoute": "", "key": "muscleMass"},
    {"entity_id": "_fat_free_mass_kg", "customRoute": "", "key": "fatFreeMass"},
    {"entity_id": "_fat_mass_kg", "customRoute": "", "key": "fatMass"},
    {"entity_id": "_weight_kg", "customRoute": "", "key": "weight"},
    {
        "entity_id": "_in_bed",
        "customRoute": "appforgood/appforgood_matera/gateway_6/SleepTracker_1/occupancy/get",
        "key": "occupancy",
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

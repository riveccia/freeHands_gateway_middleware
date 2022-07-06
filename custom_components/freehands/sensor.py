"""Sensor platform for freeHands."""
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import FreehandsEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([FreehandsSensor(coordinator, entry)])


class FreehandsSensor(FreehandsEntity):
    """freehands Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        # return self.coordinator.data.get("body")
        return ""

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "freehands__custom_device_class"

from homeassistant.helpers.entity import DeviceInfo


DOMAIN = "newsbinpro"
DEFAULT_PORT = 118
UPDATE_INTERVAL = 30  # seconds
DEVICE_INFO = DeviceInfo(
    identifiers={(DOMAIN, "newsbinpro")},
    name="Newsbin Pro",
    manufacturer="DJI Enterprises",
    model="Newsbin Pro",
)

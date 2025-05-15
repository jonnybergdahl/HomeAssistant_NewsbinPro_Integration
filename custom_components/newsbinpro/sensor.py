from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, DEVICE_INFO
from .coordinator import NewsbinProCoordinator

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator: NewsbinProCoordinator = hass.data[DOMAIN]
    entities = [
        NewsbinProSensor(coordinator, "version", "NewsbinPro Version", config_entry),
        NewsbinProSensor(coordinator, "speed", "Current Speed", config_entry, "bit/s", SensorDeviceClass.DATA_RATE),
        NewsbinProSensor(coordinator, "data_free", "Data Folder Free", config_entry, "GB", SensorDeviceClass.DATA_SIZE),
        NewsbinProSensor(coordinator, "download_free", "Download Folder Free", config_entry, "GB", SensorDeviceClass.DATA_SIZE),
        NewsbinProSensor(coordinator, "files_count", "Files Count", config_entry, None, SensorDeviceClass.ENUM),
        NewsbinProSensor(coordinator, "downloads_count", "Downloads Count", config_entry, None, SensorDeviceClass.ENUM),
    ]
    async_add_entities(entities)

class NewsbinProSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key, name, config_entry, unit=None, device_class=None):
        super().__init__(coordinator)
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = f"{DOMAIN}_{key}"
        self._key = key
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class
        self._attr_device_info = DEVICE_INFO

    @property
    def native_value(self):
        return self.coordinator.data.get(self._key)

    @property
    def should_poll(self):
        return False

    async def async_update(self):
        await self.coordinator.async_request_refresh()
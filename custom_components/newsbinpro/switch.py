from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, DEVICE_INFO
from .coordinator import NewsbinProCoordinator

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator: NewsbinProCoordinator = hass.data[DOMAIN]
    entities = [
        NewsbinProSwitch(coordinator, "limiter", "Bandwidth Limiter"),
        NewsbinProSwitch(coordinator, "paused", "Paused"),
    ]
    async_add_entities(entities)

class NewsbinProSwitch(CoordinatorEntity, SwitchEntity):
    def __init__(self, coordinator, key, name):
        super().__init__(coordinator)
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = f"newsbinpro_{key}"
        self._attr_device_info = DEVICE_INFO
        self._key = key

    @property
    def is_on(self):
        return self.coordinator.data.get(self._key)

    async def async_turn_on(self, **kwargs):
        if self._key == "limiter":
            await self.coordinator.client.set_bandwidth_limiter_state(True)
        elif self._key == "paused":
            await self.coordinator.client.set_paused_state(True)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        if self._key == "limiter":
            await self.coordinator.client.set_bandwidth_limiter_state(False)
        elif self._key == "paused":
            await self.coordinator.client.set_paused_state(False)
        await self.coordinator.async_request_refresh()

    @property
    def should_poll(self):
        return False
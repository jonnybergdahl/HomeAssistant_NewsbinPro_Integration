from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN
from .coordinator import NewsbinProCoordinator

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator: NewsbinProCoordinator = hass.data[DOMAIN]
    entities = [
        NewsbinProSwitch(coordinator, "limiter", "Bandwidth Limiter"),
        NewsbinProSwitch(coordinator, "paused", "Paused"),
    ]
    async_add_entities(entities)

class NewsbinProSwitch(SwitchEntity):
    def __init__(self, coordinator, key, name):
        self.coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = f"{DOMAIN}_{key}"
        self._key = key
        self._attr_device_info = coordinator.device_info

    @property
    def is_on(self):
        return self.coordinator.data.get(self._key)

    async def async_turn_on(self, **kwargs):
        if self._key == "limiter":
            await self.coordinator.client.set_limiter_enabled(True)
        elif self._key == "paused":
            await self.coordinator.client.set_paused(True)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        if self._key == "limiter":
            await self.coordinator.client.set_limiter_enabled(False)
        elif self._key == "paused":
            await self.coordinator.client.set_paused(False)
        await self.coordinator.async_request_refresh()

    @property
    def should_poll(self):
        return False
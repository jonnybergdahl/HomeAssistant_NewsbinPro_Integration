from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .coordinator import NewsbinProCoordinator

async def async_setup_entry(hass: HomeAssistant, config_entry):
    coordinator = NewsbinProCoordinator(hass, config_entry)
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN] = coordinator
    await hass.config_entries.async_forward_entry_setups(config_entry, ["sensor", "switch"])
    return True
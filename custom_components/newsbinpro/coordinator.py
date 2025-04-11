import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo, DeviceEntryType
from .const import DOMAIN, UPDATE_INTERVAL
from newsbinpro_client import NewsbinProClient, NewsbinProStatus

_LOGGER = logging.getLogger(__name__)

class NewsbinProCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, config_entry):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )
        self.config_entry = config_entry
        self.client = NewsbinProClient(config_entry.data["host"], config_entry.data["port"], config_entry.data["password"])

    async def _async_update_data(self):
        try:
            if not self.client.connected:
                await self.client.connect()

            statistics: NewsbinProStatus = await self.client.get_status()
            files_count = await self.client.get_files_count()
            downloads_count = await self.client.get_downloads_count()
            paused =  await self.client.get_paused_state()
            limiter = await self.client.get_bandwidth_limiter_state()

            return {
                "version": self.client.newsbin_version,
                "speed": statistics.speed,
                "data_free": round(statistics.data_folder_free_space / (1024 * 1024), 3),
                "download_free": round(statistics.download_folder_free_space / (1024 * 1024), 3),
                "files_count": files_count,
                "downloads_count": downloads_count,
                "paused": paused,
                "limiter": limiter,
            }
        except Exception as err:
            _LOGGER.exception("Error fetching data from NewsbinPro: %s", err)
            raise
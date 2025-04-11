from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
from homeassistant.exceptions import HomeAssistantError
from .const import DOMAIN, DEFAULT_PORT
from newsbinpro_client import NewsbinProClient
import logging

_LOGGER = logging.getLogger(__name__)

class NewsbinProConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                await self._validate_input(user_input)
                return self.async_create_entry(title="NewsbinPro", data=user_input)
            except Exception as ex:  # noqa: B902
                errors["base"] = str(ex)

        data_schema = vol.Schema({
            vol.Required("host"): str,
            vol.Required("port", default=DEFAULT_PORT): int,
            vol.Required("password"): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    async def _validate_input(self, data):
        """Try to connect to the NewsbinPro server to validate the credentials."""
        client = NewsbinProClient(data["host"], data["port"], data["password"])
        await client.connect()
        await client.disconnect()

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return NewsbinProOptionsFlowHandler(config_entry)

class NewsbinProOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host", default=self.config_entry.data.get("host", "")): str,
            vol.Required("port", default=self.config_entry.data.get("port", DEFAULT_PORT)): int,
            vol.Required("password", default=self.config_entry.data.get("password", "")): str,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema,
        )
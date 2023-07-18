"""Adds config flow for Transport NSW."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import CONF_DESTINATION, CONF_ROUTE, CONF_STOP_ID, DEFAULT_NAME, DOMAIN

_LOGGER = logging.getLogger(__name__)


def _get_schema(
    hass: HomeAssistant,
    user_input: dict[str, Any],
    default_dict: dict[str, Any],
    entry_id: str = None,
) -> vol.Schema:
    # pylint: disable=deprecated-typing-alias
    # pylint: disable=consider-alternative-union-syntax
    """Gets a schema using the default_dict as a backup."""  # noqa: D401

    if user_input is None:
        user_input = {}

    def _get_default(key: str, fallback_default: Any = None) -> None:
        """Gets default value for key."""  # noqa: D401
        return user_input.get(key, default_dict.get(key, fallback_default))

    return vol.Schema(
        {
            vol.Required(CONF_API_KEY, default=_get_default(CONF_API_KEY)): cv.string,
            vol.Required(CONF_STOP_ID, default=_get_default(CONF_STOP_ID)): cv.string,
            vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
            vol.Optional(CONF_ROUTE, default=_get_default(CONF_ROUTE)): cv.string,
            vol.Optional(
                CONF_DESTINATION, default=_get_default(CONF_DESTINATION)
            ): cv.string,
        }
    )


@config_entries.HANDLERS.register(DOMAIN)
class TransportNSWFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for TransportNSW."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._data = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""

        if user_input is not None:
            return self.async_create_entry(title=self._data[CONF_NAME], data=self._data)
        return await self._show_config_form(user_input)

    async def _show_config_form(self, user_input):
        """Show the configuration form to edit location data."""

        # Defaults
        defaults = {
            CONF_API_KEY: "",
            CONF_STOP_ID: "",
            CONF_NAME: DEFAULT_NAME,
            CONF_ROUTE: None,
            CONF_DESTINATION: None,
        }
        return self.async_show_form(
            step_id="user", data_schema=_get_schema(self.hass, user_input, defaults)
        )

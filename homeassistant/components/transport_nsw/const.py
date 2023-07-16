"""Constants for Transport NSW integration."""

ATTR_STOP_ID = "stop_id"
ATTR_ROUTE = "route"
ATTR_DUE_IN = "due"
ATTR_DELAY = "delay"
ATTR_REAL_TIME = "real_time"
ATTR_DESTINATION = "destination"

ATTRIBUTION = "Data provided by Transport NSW"

CONF_STOP_ID = "stop_id"
CONF_ROUTE = "route"
CONF_DESTINATION = "destination"

DEFAULT_NAME = "Next Bus"

DOMAIN = "transport_nsw"

ICONS = {
    "Train": "mdi:train",
    "Lightrail": "mdi:tram",
    "Bus": "mdi:bus",
    "Coach": "mdi:bus",
    "Ferry": "mdi:ferry",
    "Schoolbus": "mdi:bus",
    "n/a": "mdi:clock",
    None: "mdi:clock",
}

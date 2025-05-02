import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "bubble_card_templates"
_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initialize the Bubble Card Templates integration."""
    _LOGGER.info("Setting up Bubble Card Templates")
    
    # Example: Register a service
    def example_service(call):
        _LOGGER.info(f"Service called with data: {call.data}")

    hass.services.register(DOMAIN, "example_service", example_service)

    return True
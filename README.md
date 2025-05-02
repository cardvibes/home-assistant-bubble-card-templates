# Home Assistant Bubble Card Templates

This repository contains a collection of template configurations for the [Bubble Card](https://github.com/custom-cards/bubble-card) custom component in Home Assistant.

## Overview

Bubble Card Templates provide ready-to-use configurations for various sensor types displayed with the Bubble Card custom component. These templates make it easy to create visually appealing and functional cards for your Home Assistant dashboard.

## Installation

1. Make sure you have [HACS (Home Assistant Community Store)](https://hacs.xyz/) installed
2. First install the [Bubble Card](https://github.com/custom-cards/bubble-card) custom component via HACS
3. Clone this repository into your Home Assistant configuration directory:
   ```
   cd /path/to/your/config
   git clone https://github.com/cardvibes/home-assistant-bubble-card-templates.git
   ```
4. Restart Home Assistant

## Available Templates

### Battery Status Template

A template for displaying battery levels with dynamic icons and colors based on the battery percentage.

**Usage example:**

```yaml
- type: custom:template-card
  template: bubble_card_templates.battery_status
  variables:
    entity: sensor.my_device_battery
    name: Device Battery
```

**Features:**
- Dynamic icon that changes based on battery level
- Background color changes based on battery level (green, yellow, orange, red)
- Shows battery percentage
- Opens more-info dialog when tapped

## Usage

To use a template in your dashboard:

1. Add the template reference to your Lovelace configuration
2. Pass the required variables (such as entity_id and name)

## Creating Your Own Templates

You can create your own templates by adding YAML files to the `custom_components/bubble_card_templates/` directory and following the same structure.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Thanks to the creators of [Bubble Card](https://github.com/custom-cards/bubble-card) for the amazing custom component
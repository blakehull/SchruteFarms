# Schrute Farms

Schrute Farms is a goofy farm technology software designed to facilitate farm management and automation. It provides integration with various sensors and devices to monitor and control farm-related parameters. Currently, it supports water sensors and water pumps through a generic GPIO interface. In the future, the software will also incorporate temperature sensors for plants and light sensors to monitor water levels and optimize plant growth.

## Features

Schrute Farms offers the following features:

- **Water Sensor Integration**: The software seamlessly integrates with water sensors connected to a GPIO interface. It allows you to monitor water levels and trigger actions based on customizable thresholds.

- **Water Pump Control**: You can control water pumps using the software. It provides an interface to activate and deactivate water pumps based on sensor readings or manual input.

- **Temperature Sensor Integration** (upcoming): Schrute Farms will soon support temperature sensors for plants. This feature will enable you to monitor and manage temperature levels for optimal plant growth.

- **Light Sensor Integration** (upcoming): The software will also incorporate light sensors to measure the amount of light plants are receiving. This information will help you ensure that your plants are getting adequate light for their growth.

## Getting Started

To use Schrute Farms, follow these steps:

1. Install the required dependencies. You can use `pip` to install the necessary packages:

   ```shell
   pip install -r requirements.txt
   ```

2. Connect the water sensors and water pumps to your system's GPIO pins. Make sure to refer to the documentation for your specific hardware setup.

3. Configure the GPIO pins and thresholds for water sensors in the `config.yaml` file. You can specify the GPIO pins used for sensors and pumps, as well as the desired water level thresholds.

The software will start monitoring the water sensors and allow you to control the water pumps based on the specified thresholds.

## Contributing

Contributions to Schrute Farms are welcome! 

## License

Schrute Farms is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the software according to the terms of the license.
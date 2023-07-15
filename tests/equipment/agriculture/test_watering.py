import unittest
from unittest.mock import MagicMock, patch

import pytest

from equipment.agriculture.watering import WateringFactory
from equipment.helpers.sensors import SensorBoundary


@pytest.mark.watering
class WateringTests(unittest.TestCase):
    sensor_boundary = SensorBoundary(4, 7)

    @patch("equipment.agriculture.watering.WateringSensor")
    @patch("equipment.agriculture.watering.WaterPump")
    def setUp(self, mock_pump, mock_sensor):
        self.water_sensor = mock_sensor.return_value
        self.water_pump = mock_pump.return_value
        self.water_sensor.value = MagicMock(
            return_value=0
        )  # Set value attribute as a MagicMock with a default return value
        self.water_sensor.lower_bound = self.sensor_boundary.lower_bound
        self.water_sensor.upper_bound = self.sensor_boundary.upper_bound

        self.wf = WateringFactory(self.water_sensor, self.water_pump)

    def test_water_sensor_off(self):
        self.water_sensor.is_active = False
        with self.assertRaises(Exception) as cm:
            self.wf.is_time_to_water()
        self.assertEqual(
            str(cm.exception), "Watering not allowed. Sensor is not running."
        )

        with self.assertRaises(Exception) as cm:
            self.wf.sensor_reading()
        self.assertEqual(
            str(cm.exception), "Watering not allowed. Sensor is not running."
        )

    def test_water_sensor_on_low(self):
        self.water_sensor.is_active = True
        self.water_sensor.value = 1
        self.assertTrue(self.wf.is_time_to_water())
        self.assertEqual(self.wf.sensor_reading(), 1)

    def test_water_sensor_on_high(self):
        self.water_sensor.is_active = True
        self.water_sensor.value = 8
        self.assertFalse(self.wf.is_time_to_water())
        self.assertEqual(self.wf.sensor_reading(), 8)

    def test_water_sensor_in_middle(self):
        self.water_sensor.is_active = True
        self.water_sensor.value = 5
        self.assertFalse(self.wf.is_time_to_water())
        self.assertEqual(self.wf.sensor_reading(), 5)

    def test_water_pump_on(self):
        self.water_pump.value = 1
        self.assertTrue(self.wf.is_pump_running())
        self.assertFalse(self.wf.is_pump_stopped())

    def test_water_pump_off(self):
        self.water_pump.value = 0
        self.assertTrue(self.wf.is_pump_stopped())
        self.assertFalse(self.wf.is_pump_running())

    def test_turning_on_water_when_not_time_to_water(self):
        self.water_sensor.is_active = True
        self.water_sensor.value = 10
        with self.assertRaises(Exception) as cm:
            self.wf.turn_on_water()
        self.assertEqual(
            str(cm.exception),
            "you cannot turn on the water when it is not time to water!",
        )

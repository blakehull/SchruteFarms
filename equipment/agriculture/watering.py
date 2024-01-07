from gpiozero import InputDevice, OutputDevice

from equipment.monitors.sensors import SensorBoundary


class WateringFactoryProtectorMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and attr_name != "__init__":
                attrs[attr_name] = cls.wrap_method(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def wrap_method(method):
        def wrapper(self, *args, **kwargs):
            if self.sensor.is_active:
                return method(self, *args, **kwargs)
            else:
                # send alert?
                raise Exception("Watering not allowed. Sensor is not running.")

        return wrapper


class WateringSensor(InputDevice):
    def __init__(self, pin: int, interval: SensorBoundary):
        super().__init__(pin)
        self.lower_bound = interval.lower_bound
        self.upper_bound = interval.upper_bound


class WaterPump(OutputDevice):
    def __init__(self, pin: int):
        super().__init__(pin)

    def turn_on(self):
        print("turning on!")
        self.on()

    def turn_off(self):
        print("turning off!")
        self.off()


class WateringFactory(metaclass=WateringFactoryProtectorMeta):
    def __init__(
        self,
        water_sensor: WateringSensor,
        water_pump: WaterPump,
    ):
        self.sensor = water_sensor
        self.pump = water_pump
        self.low_water = self.sensor.lower_bound
        self.max_water = self.sensor.upper_bound

    def is_time_to_water(self):
        if self.sensor.value <= self.low_water:
            return True
        return False

    def sensor_reading(self):
        return self.sensor.value

    def turn_on_water(self):
        if not self.is_time_to_water():
            raise Exception(
                "you cannot turn on the water when it is not time to water!"
            )
        self.pump.turn_on()

    def is_pump_running(self):
        return self.pump.value == 1

    def is_pump_stopped(self):
        return not self.is_pump_running()

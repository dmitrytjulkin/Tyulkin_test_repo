import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def dec2bin(value):
        return [int(element) for element in bin(value)[2:].zfill(8)] #returns binary array

    def num2dac(self, number):
        signal = dec2bin(value)
        GPIO.output(dac, signal)                                     #shows bin array on dac
        return signal

    def sequential_counting_adc(self):
        for value in range(256):
            signal = num2dac(value)
            voltage = value / self.dynamic_range * 255
            # comparatorValue = GPIO.input(comparator)
            # if comparatorValue == 0:
            #     print ("ADC value = :{^3} -> {}, "
            #            "input voltage = {.2f}".format(value, signal, voltage))
            time.sleep(0.01)

    def get_sc_voltage(self):


try:
    dac = R2R_ADC(3.3)
finally:
    dac.deinit()

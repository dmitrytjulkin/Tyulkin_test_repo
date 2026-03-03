import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('chart')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.grid()
    plt.show()

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [11, 25, 12, 13, 16, 19, 20, 26]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in f"{value:08b}"][::-1] #returns binary array

    def num2dac(self, number):
        GPIO.output(self.bits_gpio, self.dec2bin(number))                                     #shows bin array on dac

    def sequential_counting_adc(self):
        for value in range(256):
            self.num2dac(value)
            
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                return value

    def get_sc_voltage(self):
        value = self.sequential_counting_adc()
        voltage = value / 255.0 * self.dynamic_range
        return voltage


voltage_values = []
time_values = []
duration = 3.0


if __name__ == "__main__":
    try:
        start_time = time.time()
        adc = R2R_ADC(4.5, 0.0001, True)

        while time.time() - start_time < duration:
            voltage = adc.get_sc_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time())
            print ('\033[33m The actual voltage is \033[0m', voltage)

        plot_voltage_vs_time(time_values, voltage_values, 4.5)

    finally:
        adc.deinit()

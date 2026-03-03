import RPi.GPIO as GPIO
import time


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
    
    def successive_approximation_adc(self):
        left_ptr = 0
        right_ptr = 255

        for i in range (8):
            middle = (right_ptr+left_ptr)//2
            self.num2dac(middle)
            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                right_ptr = middle
            else:
                left_ptr = middle + 1

            print (left_ptr, right_ptr)

        return left_ptr
    
    def get_sar_voltage(self):
        code = self.successive_approximation_adc()
        voltage = code / 255 * self.dynamic_range
        return voltage


if __name__ == "__main__":
    try:
        adc = R2R_ADC(4.5, 0.0001, True)
        # print ('\033[31mPASSED\033[0m')
        while True:
        #   voltage = adc.get_sc_voltage()
          voltage = adc.get_sar_voltage()
          print ('\033[33m The actual voltage is \033[0m', voltage)

    finally:
        adc.deinit()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        for i in range(8):
           bit_value = (number >> i) & 1
           GPIO.output(self.gpio_bits[i], bit_value)     
        if self.verbose:
            print(f"Установленно число: {number}")

    def set_voltage(self, voltage):
        max_number = 2**8 - 1
        number = int(voltage * max_number / self.dynamic_range)
        number = max(0, min(number, max_number))
        self.set_number(number)
        if self.verbose:
            print(f"Установленное напряжение: {voltage:.2f}")

if __name__ == "__main__":
    dac = None
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    
    finally:
        dac.deinit()


import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.0001, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.cur_res = 0

        self.bits_gpio = [11, 25, 12, 13, 16, 19, 20, 26][::-1]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]   #returns binary array

    def num2dac(self, number):
        GPIO.output(self.bits_gpio, self.dec2bin(number))           #shows bin array on dac

    def sequential_counting_adc(self):
        for value in range(256):
            self.num2dac(value)

            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                return value
        return 255

    def get_sc_voltage(self):
        value = self.sequential_counting_adc()
        voltage = value / 255.0 * self.dynamic_range
        return voltage

    def successive_approximation_adc(self):
        # time.sleep(self.compare_time)
        cb = 7
        self.cur_res = 0

        while (cb >= 0):
            cmp = GPIO.input(self.comp_gpio)
            if cmp > 0:
                self.cur_res -= 1 << cb
            else:
                self.cur_res += 1 << cb

            if self.cur_res >= 256:
                self.cur_res = 255
            if self.cur_res < 0:
                self.cur_res = 0

            cb -= 1
            self.num2dac(self.cur_res)
            time.sleep(self.compare_time)

# ## 1
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 2
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 3
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 4
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 5
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 6
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 7
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)
# ## 8
#         cmp = GPIO.input(self.comp_gpio)
#         if cmp > 0:
#             self.cur_res -= 1 << cb
#         else:
#             self.cur_res += 1 << cb

#         cb -= 1
#         self.num2dac(self.cur_res)
#         time.sleep(self.compare_time)

        return self.cur_res 

        # for i in range (8):
        #     middle = (right_ptr+left_ptr) // 2
        #     self.num2dac(middle)
        #     if GPIO.input(self.comp_gpio) == GPIO.HIGH:
        #         right_ptr = middle
        #     else:
        #         left_ptr = middle + 1
        #     time.sleep(self.compare_time)

            # print (f"left pointer: {left_ptr}, right pointer: {right_ptr}")
        # print (f"left pointer: {left_ptr}, right pointer: {right_ptr}")
        # return left_ptr

    def get_sar_voltage(self):
        code = self.successive_approximation_adc()
        voltage = code / 255.0 * self.dynamic_range
        return voltage


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.2, 0.001, True)
        # print ('\033[31mPASSED\033[0m')
        while True:
            voltage = adc.get_sc_voltage()
            # voltage = adc.get_sar_voltage()
            print ('\033[33m The actual voltage is \033[0m', voltage)

    finally:
        adc.deinit()

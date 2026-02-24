import RPi.GPIO as GPIO

# TODO needs lots of changes
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)

        if self.verbose:
            print(f"PWM_DAC инициализирован на пине {gpio_pin}, частота {pwm_frequency} Гц, дипазон {dynamic_range} B")

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup(self.gpio_pin)
        if self.verbose:
            print (f"PWM_DAC деинициализирован")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон"
                  f"ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            duty = 0.0

        else:
            duty = voltage / self.dynamic_range * 100.0

        self.pwm.ChangeDutyCycle(duty)

        if self.verbose:
            print (f"Установлено напряжение {voltage:.2f} B -> duty cycle = {duty:.1f}%")

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

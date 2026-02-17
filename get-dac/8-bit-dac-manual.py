import RPi.GPIO as GPIO

dac_pins = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setmode(GPIO.BCM)          
GPIO.setup(dac_pins, GPIO.OUT)  

dynamic_range = 3.18
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):

    for i in range(8):
        
        bit_value = (number >> i) & 13
        
        GPIO.output(dac_pins[i], bit_value)
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_pins, 0)
    GPIO.cleanup()


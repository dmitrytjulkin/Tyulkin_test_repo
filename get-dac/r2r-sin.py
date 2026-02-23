import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        driver = MCP4725(5.5, 0x61, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                driver.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        driver.deinit()


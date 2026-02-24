import signal_generator as sg   #(4th task)
import mcp4725_driver as md
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        driver = md.MCP4725(5.5, 0x61, True)

        sampling_period = 1 / sampling_frequency
        t = 0.0

        while True:
            cur_amplitude = sg.get_sin_wave_amplitude(signal_frequency, t)
            driver.set_voltage(cur_amplitude * amplitude)
            sg.wait_for_sampling_period(sampling_frequency)

            t += sampling_period

    except KeyboardInterrupt:
        print("\nГенерация сигнала остановлена")

    finally:
        driver.deinit()

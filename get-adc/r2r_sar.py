import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC
from adc_plot import plot_sampling_period_hist, plot_voltage_vs_time
import time

voltage_values = []
time_values = []
duration = 5.0

if __name__ == "__main__":
    try:
        start_time = time.time()
        adc = R2R_ADC(3.3, 0.001, True)

        while time.time() - start_time < duration:
            voltage = adc.get_sar_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - start_time)
            print ('\033[33m The actual voltage is \033[0m', voltage)

        plot_voltage_vs_time(time_values, voltage_values, 3.2)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()

import matplotlib.pyplot as plt
import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

voltage_values = []
time_values = []
duration = 5.0

if __name__ == "__main__":
    try:
        start_time = time.time()
        adc = MCP3021(5.2, True)          #have to be measured

        while time.time() - start_time < duration:
            voltage = adc.get_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - start_time)
            print ('\033[33m The actual voltage is \033[0m', voltage)

        plot_voltage_vs_time(time_values, voltage_values, 3.3)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()

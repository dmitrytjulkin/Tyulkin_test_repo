import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC
import time


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('chart')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.grid()
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range (len(time) - 1):
        sampling_periods.append(abs(time[i] - time[i+1]))

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title('there is something')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.xlim(0, 0.06)
    plt.grid()
    plt.show()


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
            time_values.append(time.time() - start_time)
            print ('\033[33m The actual voltage is \033[0m', voltage)

        # plot_voltage_vs_time(time_values, voltage_values, 4.5)
        plot_sampling_period_hist(time_values)

    finally:
        adc.deinit()

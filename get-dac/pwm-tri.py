import pwm_dac as pd
import signal_generator_tri as sg
import time

amplitude = 2.0
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pd.PWM_DAC(12, 1000, 3.290, True)
        sampling_period = 1 / sampling_frequency
        t = 0

        while True:
            cur_amplitude = sg.get_tri(signal_frequency, t)
            dac.set_voltage (amplitude * cur_amplitude)
            sg.wait_for_sampling_period(sampling_frequency)

            t += sampling_period
    
    finally:
        dac.deinit()
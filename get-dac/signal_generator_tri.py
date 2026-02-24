import numpy as np
import time
import math

def get_tri(freq, time):
    return (math.asin(math.sin(2*math.pi*freq*time))/2/np.pi+1)

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)

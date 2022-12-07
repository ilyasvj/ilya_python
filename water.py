import common
import numpy as np
import matplotlib.pyplot as plt

class Water(common.Common):
    def get_signal(self, r, fi):
        time = np.arange(0, self.Tc, 1 / self.fd)
        signal_left = np.random.randn(time.size) / 10
        signal_right = np.random.randn(time.size) / 10

        delay = r/1500
        dt = self.d/1500*np.sin(fi/180.0*np.pi)
        for i in range (time.size):
            if time[i] > delay and time[i] < delay + self.ti:
                signal_left[i] += np.sin(2 * np.pi * self.fs * time[i])
                signal_right[i] += np.sin(2 * np.pi * self.fs * (time[i] - dt))

        print(2 * np.pi * self.fs * dt * 180 / np.pi)
        plt.plot(time, signal_left, time, signal_right)
        plt.show()
        return ((time, signal_left, signal_right))
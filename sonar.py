import common
import numpy as np

class Sonar(common.Common):
    def get_coordinates(self, signal_left, signal_right):
        spectrum_left = np.fft.fft(signal_left)
        spectrum_right = np.fft.fft(signal_right)

        n = spectrum_left.size
        spectrum_left[int(n / 2):] = 0
        spectrum_right[int(n / 2):] = 0
        signal_left = np.fft.ifft(spectrum_left)
        signal_right = np.fft.ifft(spectrum_right)

        z_left = np.abs(np.fft.ifft(spectrum_left))
        sigma = np.sqrt((np.sum(np.sqrt(z_left)) / n))

        detection_level = np.where(z_left >= sigma)
        print(detection_level)

        distance = ((detection_level[0][0]) / self.fd) * 1500
        print(distance)

        fi_left = np.angle(signal_left)
        fi_right = np.angle(signal_right)
        delta_fi = fi_right - fi_left

        delta_fi[np.where(delta_fi > np.pi)] -= 2 * np.pi
        delta_fi[np.where(delta_fi < -np.pi)] += 2 * np.pi
        delta_fi_mean = sum(delta_fi) / delta_fi.size
        print(delta_fi_mean)

        peleng = np.arcsin((self.c * delta_fi_mean) / (2 * np.pi * self.fs * self.d))
        print(peleng * (180 / np.pi))
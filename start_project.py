import sonar
import water

water = water.Water()
(time, signal_left, signal_right) = water.get_signal(500, 30)
distance = sonar.Sonar().get_coordinates(signal_left, signal_right)
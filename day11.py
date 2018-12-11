sn = 4842
import numpy as np

def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += sn
    power *= rack
    return (power // 100 % 10) - 5

grid = np.fromfunction(power, (300, 300))


for x in range(2, 299):
    for y in range(2, 299):
        power = 0
        for width in range(1,300):
            windows = sum(grid[x:x-width, y:y-width] for x in range(width) for y in range(width))
            maximum = int(windows.max())
            location = np.where(windows == maximum)
            print(width, maximum, location[0][0] + 1, location[1][0] + 1)

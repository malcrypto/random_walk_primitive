import numpy as np
import matplotlib.pyplot as plt
import pylab
import random
def rand_walk(inp):
    if inp == 1:
        prob = [0.5, 0.5]
        start = 0
        positions = [start]
        rr = np.random.random(100)
        downp = rr < prob[0]
        upp = rr > prob[1]

        for idownp, iupp in zip(downp, upp):
            down = idownp and positions[-1] > -10000
            up = iupp and positions[-1] < 10000
            positions.append(positions[-1] - down + up)
        plt.plot(positions)
        plt.show()
    elif inp == 2:
        
        n = 100000

        # creating two array for containing x and y coordinate
        # of size equals to the number of size and filled up with 0's
        x = np.zeros(n)
        y = np.zeros(n)

        # filling the coordinates with random variables
        for i in range(1, n):
            val = random.randint(1, 4)
            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1

        pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
        pylab.plot(x, y)
        pylab.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
        pylab.show()
    else:
        print("Haven't implemented this dimension yet")

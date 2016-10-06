
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt


plot_ns = [2, 10, 50, 100, 150, 200]


def generate_point_pair(n):
    point1 = np.random.random_sample((n,))
    point2 = np.random.random_sample((n,))
    return (point1, point2)


def count_distance(point_pair):
    return distance.euclidean(point_pair[0], point_pair[1])


def main():
    for n in range(2, 101):
        distances = []

        for i in range(1, 1001):
            point_pair = generate_point_pair(n)
            distance = count_distance(point_pair)
            distances.append(distance)

        mean = np.mean(distances)
        var = np.var(distances)

        # print "Mean: ", mean
        # print "Variance: ", var

        if n in plot_ns:
            hist, bins = np.histogram(distances, bins=20)
            width = 0.2 * (bins[1] - bins[0])
            center = (bins[:-1] + bins[1:]) / 2
            plt.hist(distances, bins)
            plt.savefig('file'+str(n)+'.png', dpi=96)
            plt.clf()


if __name__ == "__main__":
    main()
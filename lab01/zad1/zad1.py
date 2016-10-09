
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt


plot_ns = [2, 10, 50, 100, 150, 200]


def main():
	means = []
	variances = []

	zero_means = []
	zero_variances = []

	for n in range(2, 201):
		distances = []
		distances_zero = []
		zeros = np.zeros((n,))
		for i in range(1, 1001):
			point1 = np.random.random_sample((n,))
			point2 = np.random.random_sample((n,))

			distances.append(distance.euclidean(point1, point2))

			distances_zero.append(distance.euclidean(point1, zeros))

		mean = np.mean(distances)
		var = np.var(distances)

		means.append(mean)
		variances.append(var)

		mean = np.mean(distances_zero)
		var = np.var(distances_zero)

		zero_means.append(mean)
		zero_variances.append(var)

		if n in plot_ns:
			hist, bins = np.histogram(distances, bins=20)
			plt.hist(distances, bins)
			plt.savefig('a_dim_' + str(n) + '.png', dpi=96)
			plt.clf()
			hist, bins = np.histogram(distances_zero, bins=20)
			plt.hist(distances_zero, bins)
			plt.savefig('b_dim_' + str(n) + '.png', dpi=96)
			plt.clf()

	plt.plot(range(2, 201), means)
	plt.savefig('a_means.png', dpi=96)
	plt.clf()

	plt.plot(range(2, 201), variances)
	plt.savefig('a_variances.png', dpi=96)
	plt.clf()

	plt.plot(range(2, 201), zero_means)
	plt.savefig('b_means.png', dpi=96)
	plt.clf()

	plt.plot(range(2, 201), zero_variances)
	plt.savefig('b_variances.png', dpi=96)
	plt.clf()

if __name__ == "__main__":
	main()
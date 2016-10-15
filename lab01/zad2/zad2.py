import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


plot_ns = [10, 50, 100, 150, 200]


def generate_point_pair(n):
	cube_point = np.random.random_sample((n,))
	sphere_point = np.random.random_sample((n,))
	zeros = [0] * n
	sphere_point = sphere_point * np.power(np.random.random_sample(), 1./n) / distance.euclidean(sphere_point, zeros)
	return (cube_point, sphere_point)


def perform_pca(cube, sphere, n):
    cube_pca = PCA(2)
    sphere_pca = PCA(2)
    reduced_cube = cube_pca.fit_transform(cube)
    reduced_sphere = sphere_pca.fit_transform(sphere)
    return (reduced_cube, reduced_sphere)


def visualize_pca(reduced_cube, reduced_sphere, n):
	colors = ['blue', 'green']
	plt.figure()
	plt.scatter(reduced_cube[:, 0], reduced_cube[:, 1], color=colors[0])
	plt.scatter(reduced_sphere[:, 0], reduced_sphere[:, 1], color=colors[1])
	plt.xlabel('x')
 	plt.ylabel('y')
	plt.title('PCA. Points in Hypercube: blue, in Hypersphere: green.')
	plt.savefig('file' + str(n) + '.png', dpi=96)
	plt.clf()


def plot_dist(cube_means, sphere_means):
    rang = range(3, 201)
    plt.figure()
    plt.plot(rang, cube_means, color='blue')
    plt.plot(rang, sphere_means, color='green')
    plt.xlabel('dimension')
    plt.ylabel('distance from coord center')
    plt.title('Hypercube: blue, Hypersphere: green')
    plt.savefig('distance.png', dpi=96)
    plt.clf()


def plot_insphere_ratio(cube_points, center, n, file_prefix):
	r = 0.5
	xticks = ('<= r', '> r')
	y_pos = np.arange(len(xticks))
	greater_count = 0
	for point in cube_points:
		if distance.euclidean(point, center) > r:
			greater_count += 1

	plt.figure()
	plt.bar(y_pos, [len(cube_points) - greater_count, greater_count], align='center', color="blue")
	plt.xticks(y_pos, xticks)
	plt.savefig(file_prefix + str(n) + '.png', dpi=96)
	plt.clf()


def plot_insphere_ratio_v2(cube_points, center, n, r):
	y = []
	x = []

	for j in np.arange(0.1, r, 0.1):
		gt = 0
		for point in cube_points:
			if distance.euclidean(point, center) > j:
				gt += 1

		le = ((len(cube_points) - gt) / len(cube_points))*100
		y.append(le)
		x.append(j)
		if le >99.9:
			break

	plt.figure()
	plt.xlabel('r')
	plt.ylabel('% of points in sphere')
	plt.plot(x,y)
	plt.savefig('radius_v2_' + str(n) + '.png', dpi=96)
	plt.clf()


def main():

	mean_dists_cube = []
	mean_dists_sphere = []

	for n in range(3, 201):
		cube_points = []
		sphere_points = []
		dist_cube = []
		dist_sphere = []
		zeros = [0] * n
		sphere_center = [0.5] * n
		
		for i in range(1, 1501):
			point_pair = generate_point_pair(n)
			cube_points.append(point_pair[0])
			sphere_points.append(point_pair[1])
			dist_cube.append(distance.euclidean(point_pair[0], zeros))
			dist_sphere.append(distance.euclidean(point_pair[1], zeros))

		pca = perform_pca(cube_points, sphere_points, n)

		if n in plot_ns:
			visualize_pca(pca[0], pca[1], n)

		mean_dists_cube.append(np.mean(dist_cube))
		mean_dists_sphere.append(np.mean(dist_sphere))

		if n in plot_ns + [75]:
			plot_insphere_ratio(cube_points, sphere_center, n, 'insphere_ratio_')
			plot_insphere_ratio(pca[0], [0.5] * 2, n, 'insphere_ratio_2d_')

			plot_insphere_ratio_v2(cube_points, sphere_center, n, np.sqrt(n))

	plot_dist(mean_dists_cube, mean_dists_sphere)


if __name__ == "__main__":
	main()
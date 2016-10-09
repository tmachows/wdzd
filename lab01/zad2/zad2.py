import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import sklearn.decomposition as deco

plot_ns = [2, 10, 50, 100, 150, 200]


def generate_point_pair(n):
    cube = np.random.random_sample((n,))
    ball = np.random.random_sample((n,))
    zeros = np.zeros((n,), dtype=np.int)
    ball = ball*np.power(np.random.random_sample(), 1./n)/distance.euclidean(ball,zeros)
    # ball = ball-1
    #
    # while distance.euclidean(zeros, ball) > 1:
    #     ball = 0.9 * ball
    return (cube, ball)



def do_pca(ball, cube, n):
    pca_cube = deco.PCA(n_components)
    pca_ball = deco.PCA(n_components)
    reduced_cube = pca_cube.fit(cube).transform(cube)
    reduced_ball = pca_ball.fit(ball).transform(ball)
    if n in plot_ns:
        colors = ['blue', 'red']
        plt.figure()
        plt.scatter(reduced_cube[:, 0], reduced_cube[:, 1], marker='x', color=colors[0])
        plt.scatter(reduced_ball[:, 0], reduced_ball[:, 1], marker='.', color=colors[1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Cartesian coordinate PCA: HyperCube[blue] HyperBall[red]')
        plt.savefig('file' + str(n) + '.png', dpi=96)
        plt.clf()
    return (reduced_cube, reduced_ball)

def print_radius(ball, center, n):
    objects = ('inside', 'out')
    y_pos = np.arange(len(objects))
    if n in plot_ns:
        gt = 0
        for i in ball:
            if distance.euclidean(i, center) > r:
                gt += 1

        le = len(ball) - gt
        plt.figure()
        plt.bar(y_pos, [le, gt], align='center', color="blue")
        plt.xticks(y_pos, objects)
        plt.savefig('radius' + str(n) + '.png', dpi=96)
        plt.clf()

def print_radius2d(ball, center, n):
    objects = ('inside', 'out')
    y_pos = np.arange(len(objects))
    if n in plot_ns:
        gt = 0
        for i in ball:
            if distance.euclidean(i, center) > r:
                gt += 1

        le = len(ball) - gt
        plt.figure()
        plt.bar(y_pos, [le, gt], align='center', color="blue")
        plt.xticks(y_pos, objects)
        plt.savefig('radius2d' + str(n) + '.png', dpi=96)
        plt.clf()

def print_dist(mean_ball, mean_cube):
    rang = range(3, 201)
    plt.figure()
    plt.plot(rang, mean_cube, color='blue')
    plt.plot(rang, mean_ball, marker='.', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('distans from center: HyperCube[blue] HyperBall[red]')
    plt.savefig('distance.png', dpi=96)
    plt.clf()


n_components = 2
r = 0.5
def main():
    mean_cube = []
    mean_ball = []

    for n in range(3, 201):
        cube = []
        ball = []
        dist_ball = []
        dist_cube = []
        center = [0.5] * n
        zeros = np.zeros((n,), dtype=np.int)
        for i in range(1, 101):
            point_pair = generate_point_pair(n)
            cube.append(point_pair[0])
            ball.append(point_pair[1])
            dist_cube.append(distance.euclidean( point_pair[0],zeros))
            dist_ball.append(distance.euclidean( point_pair[1],zeros))

        # prepare PCA
        pca = do_pca(ball, cube, n)
#         prepare dist
        mean_cube.append(np.mean(dist_cube))
        mean_ball.append(np.mean(dist_ball))

        print_radius(cube, center, n)
        print_radius2d(pca[0],[0.5] * 2, n)

    print_dist(mean_ball, mean_cube)






if __name__ == "__main__":
    main()
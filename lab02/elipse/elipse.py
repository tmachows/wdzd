import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random_sample as random
import sklearn.decomposition as deco

def random_uniform_in_disc():
    # returns a tuple which is uniform in the disc
    theta = 2 * np.pi * random()
    r2 = random()
    r = np.sqrt(r2)
    return np.array((r * np.sin(theta), r * np.cos(theta)))


def random_uniform_in_ellipse(a=2, b=1):
    x = a * random_uniform_in_disc()[0]
    y = b * np.sqrt(1 - (x / a) ** 2) * (1 - 2 * np.random.random_sample())
    return np.array((x, y))

def main():
    sample = np.array([random_uniform_in_ellipse() for i in np.arange(1000)])
    pca_data = deco.PCA()

    reduced_data = pca_data.fit(sample).transform(sample)
    cov = pca_data.get_covariance()

    eigw, eigv = np.linalg.eig(cov)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    U,V = zip(*eigv)
    ax.quiver([0,0],[0,0],U,V,angles='xy',scale_units='xy',scale=1)
    ax.scatter(sample[:, 0], sample[:, 1])
    plt.show()


if __name__ == "__main__":

	main()
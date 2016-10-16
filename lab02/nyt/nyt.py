from pandas import *
import os

import matplotlib.pyplot as plt
import sklearn.decomposition as deco



def do_pca(data):

    pca_data = deco.PCA()

    reduced_data = pca_data.fit(data).transform(data)

    var = pca_data.explained_variance_
    colors = ['navy', 'red']
    plt.figure()
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], marker='x', color=colors[0])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cartesian coordinate PCA: ')
    plt.savefig('reduced.png', dpi=96)
    plt.clf()
    return (reduced_data)


def main():

    nyt = read_csv("nyt-frame.csv")
    labels = nyt['class.labels']
    nyt = nyt.drop(['class.labels'], axis=1)



    # nyt_demeaned = nyt - nyt.mean(0)


    # print(labels)
    #
    print('X.\n',nyt['X.'])
    print('\nability\n',nyt['ability'])

    os.system('Rscript nyt.R')


    # do_pca(nyt)

if __name__ == "__main__":

	main()
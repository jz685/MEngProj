from plot_chebint import plot_chebint
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy as sp

def compare_chebhist(dname, mylambda, c, Nbin = 25):
    lmin = max(min(mylambda), -1)
    lmax = min(max(mylambda),  1)

    # print c
    cheb_file_content = '\n'.join([str(st) for st in c])
    x = np.linspace(lmin, lmax, Nbin + 1)
    y = plot_chebint(c, x)
    u = (x[1:] + x[:-1]) / 2
    v =  y[1:] - y[:-1]

    plt.clf()
    plt.hold(True)
    plt.hist(mylambda,Nbin)
    plt.plot(u, v, "r.", markersize=10)
    plt.hold(False)
    # plt.show()
    filename = 'data/' + dname + '.png'
    plt.savefig(filename)

    cheb_filename = 'data/' + dname + '.cheb'
    f = open(cheb_filename, 'w+')
    f.write(cheb_file_content)
    f.close()
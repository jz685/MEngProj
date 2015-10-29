from plot_chebint import plot_chebint

def compare_chebhist(l,c,Nbin=25):

    lmin = max(min(l),-1)
    lmax = min(max(l),1)

    x = np.linspace(lmin,lmax,Nbin+1)
    y = plot_chebint(c,x)
    u = (x[1:] + x[:-1]) / 2
    v = (y[1:] - y[:-1])

    plt.clf()
    plt.hold(True)
    plt.hist(l,Nbin)
    plt.plot(u,v,"r.",markersize=10)
    plt.hold(False)
    plt.show()
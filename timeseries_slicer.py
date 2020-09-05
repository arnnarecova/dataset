import numpy as np
import matplotlib.pyplot as plt

def slice_timeseries(x, l=128, d=64, max_k = None):
    k = (len(x) - l + 1) / d
    if not max_k == None:
        k = max(k, max_k)
    X = np.zeros([k,2,l], dtype=np.float32)
    for i in range(0,k):
        w = np.ones([l])
        #w = np.sin(np.arange(0,np.pi,np.pi/l))
        #plt.figure()
        #plt.plot(w)
        #plt.show()
        x_i = x[i*d:i*d+l] * w
        X[i,0,:] = np.real(x_i)
        X[i,1,:]     = np.imag(x_i)
    return X

def slice_timeseries_dict(td, l=128, d=64, max_k = None):
    nd = {}
    for k,v in td.iteritems():
        nd[k] = slice_timeseries(v)
    return nd

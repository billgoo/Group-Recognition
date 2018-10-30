import scipy
import numpy as np
import scipy.cluster.hierarchy as sch

# points=scipy.randn(20,4)
points=np.array([[0,3,1,2,0],
                 [1,3,0,1,0],
                 [3,3,0,0,1],
                 [1,1,0,2,0],
                 [3,2,1,2,1],
                 [4,1,1,1,0]])
print points

disMat = sch.distance.pdist(points,'euclidean')
print disMat

Z=sch.linkage(disMat,method='average')
print Z

cluster= sch.fcluster(Z, t=1)
print "Original cluster by hierarchy clustering:\n",cluster

import scipy.cluster.hierarchy as sch
import numpy as np

data_test1=np.array([292,311,390,401,379,
                     318,409,373,375,
                     448,345,364,
                     464,448,
                     273])

data_test2=np.array([321,295,387,367,346,392,366,
                     279,333,296,290,335,339,
                     335,280,287,292,309,
                     254,245,350,290,
                     190,301,265,
                     294,259,
                     235])

data_test3=np.array([241,286,338,333,328,346,333,
                     295,287,315,308,328,326,
                     269,325,242,225,292,
                     261,288,280,265,
                     290,276,237,
                     186,272,
                     276])

data = [data_test1,data_test2,data_test3]
#print data

for i in range(0,3):
    for j in range(2,5):
        # print data[i]
        Z = sch.linkage(data[i], method='single')
        cluster = sch.fcluster(Z, t=j, criterion='maxclust')
        print "Original cluster by", j, "hierarchy clustering:", i+1, "\n", cluster


import scipy.cluster.hierarchy as sch
import numpy as np

data_test1=np.array([292,311,390,401,353,379,376,
                     318,409,373,359,375,397,
                     448,345,342,364,376,
                     464,427,448,381,
                     304,273,343,
                     302,183,
                     352])

data_test2=np.array([321,295,387,367,346,392,377,366,
                     279,333,296,290,335,328,339,
                     335,280,287,292,324,309,
                     254,245,350,346,290,
                     190,301,317,265,
                     294,298,259,
                     330,235,
                     322])

data_test3=np.array([241,286,338,333,320,318,328,346,378,333,
                     295,287,315,292,294,308,328,337,326,
                     269,325,269,252,242,225,345,292,
                     261,291,287,288,280,329,265,
                     307,271,290,276,320,237,
                     134,287,280,105,318,
                     252,233,155,295,
                     186,324,272,
                     306,276,
                     357])

data = [data_test1,data_test2,data_test3]
#print data

for i in range(0,3):
    for j in range(2,5):
        # print data[i]
        Z = sch.linkage(data[i], method='single')
        cluster = sch.fcluster(Z, t=j, criterion='maxclust')
        print "Original cluster by", j, "hierarchy clustering:", i+1, "\n", cluster


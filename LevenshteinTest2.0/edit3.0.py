# divide every 15 windows

import csv

import numpy as np
from Levenshtein import *

with open('predict3-10.csv') as ftr:
    predict = csv.reader(ftr);
    dataset = list(predict)
    data = np.array(dataset)

# print data
# print dataset
s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""

for i in range(0, 3230):
    if data[i, 2] == '10':
        data[i, 2] = '0'

m = 15
n = 1
for n in range(8, 32):
    print '\t', n-1, '\n\n'
    for i in range(0, 3230):
        if m * n - 15 <= int(data[i, 1]) < m * n:
            if data[i, 0] == '1':
                s1 += data[i, 2]
            elif data[i, 0] == '2':
                s2 += data[i, 2]
            elif data[i, 0] == '3':
                s3 += data[i, 2]
            elif data[i, 0] == '4':
                s4 += data[i, 2]
            elif data[i, 0] == '5':
                s5 += data[i, 2]
            elif data[i, 0] == '6':
                s6 += data[i, 2]
            elif data[i, 0] == '7':
                s7 += data[i, 2]
            #elif data[i, 0] == '8':
            #    s8 += data[i, 2]
            #elif data[i, 0] == '9':
            #    s9 += data[i, 2]
            elif data[i, 0] == '10':
                s10 += data[i, 2]
            elif data[i, 0] == '11':
                s11 += data[i, 2]
            elif data[i, 0] == '12':
                s12 += data[i, 2]
            #elif data[i, 0] == '13':
            #    s13 += data[i, 2]
            elif data[i, 0] == '14':
                s14 += data[i, 2]
            elif data[i, 0] == '15':
                s15 += data[i, 2]
            elif data[i, 0] == '16':
                s16 += data[i, 2]
    #print s10
    #print s11
    #print s14
    #print s2
    #print s3
    a = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""
    # print s1
    for i in range(0, 16):
        for j in range(i + 1, 16):
            if a[i] != "":
                if a[j] != "":
                    print distance(a[i], a[j])
                    # print distance(a[i],a[j]),i+1,j+1
        print "\n"


# print s1,'\n',s2,'\n',s4,'\n',s6,'\n',s7,'\n',s8,'\n',s11,'\n',s13

#print distance(s1,s2)
#print distance(s1,s4)
#print distance(s1,s5)
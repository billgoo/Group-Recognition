# divide every 15 windows

import csv

import numpy as np
from Levenshtein import *

with open('predict1-10.csv') as ftr:
    predict = csv.reader(ftr);
    dataset = list(predict)
    data = np.array(dataset)

# print data
# print dataset
s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""

for i in range(0, 3336):
    if data[i, 2] == '10':
        data[i, 2] = '0'

m = 15
n = 1
simmap = {}

for n in range(1, 33):
    # print '\t', n, '\n\n'
    for i in range(0, 3336):
        if m * n - 15 <= int(data[i, 1]) < m * n:
            if data[i, 0] == '1':
                s1 += data[i, 2]
            elif data[i, 0] == '2':
                s2 += data[i, 2]
            elif data[i, 0] == '3':
                s3 += data[i, 2]
            elif data[i, 0] == '6':
                s6 += data[i, 2]
            elif data[i, 0] == '7':
                s7 += data[i, 2]
            elif data[i, 0] == '10':
                s10 += data[i, 2]
    a = [s1, s2, s3, s6, s7, s10]
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""
    N = []
    F = []
    # print s1
    for i in range(0, 6):
        for j in range(0, 6):
            if a[i] != "" and a[j] != "":
                # print distance(a[i], a[j])
                # print distance(a[i],a[j]),i+1,j+1
                F.append(distance(a[i], a[j]))
            elif a[i] == "" or a[j] == "":
                F.append(-1)
        # print "\n"
        if F != []:
            N.append(F)
        F = []

    # print N
    simm = np.array(N)
    simmap[n] = simm
    N = []
    # print n


# print s1,'\n',s2,'\n',s4,'\n',s6,'\n',s7,'\n',s8,'\n',s11,'\n',s13

#print distance(s1,s2)
#print distance(s1,s4)
#print distance(s1,s5)

groupaffi = [[-1,1,1,1,0,0],
             [1,-1,1,1,0,0],
             [1,1,-1,1,0,0],
             [1,1,1,-1,0,0],
             [0,0,0,0,-1,1],
             [0,0,0,0,1,-1]]
result = {}
th = {}
acc = {}
threshold = 0.0
total = 15
count = 0
# print simmap[32][1,0]
while threshold < 15.0:
    accuracy = 0.0
    for windowsNumber in range(1, 33):
        pos = 0
        for ui in range(0, 6):
            for uj in range(0, 6):
                if ui < uj:
                    if int(simmap[windowsNumber][ui, uj]) <= threshold:
                        if groupaffi[ui][uj] == 1:
                            pos += 1
                    else:
                        if groupaffi[ui][uj] == 0:
                            pos += 1
        acc[windowsNumber] = float(pos)/total
        accuracy += acc[windowsNumber]
    accuracy /= 32
    result[count] = accuracy
    th[count] = threshold
    count += 1
    print str(accuracy), '\t', threshold
    threshold += 0.01
# print result
for i in range(1, 1500):
    if result[i] <= result[i-1]:
        temp = result[i]
        result[i] = result[i-1]
        result[i-1] = temp
        temp0 = th[i]
        th[i] = th[i - 1]
        th[i - 1] = temp0

print '\n', result[1499], '\t', th[1499]


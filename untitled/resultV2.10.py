# -*- coding:utf-8 -*-
# divide every 15 windows

import csv

import numpy as np
from Levenshtein import *

with open('10_action.csv') as ftr:
    predict = csv.reader(ftr);
    dataset = list(predict)
    data = np.array(dataset)

# print data
# print dataset
s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""

for i in range(0, 4717):
    if data[i, 2] == '10':
        data[i, 2] = '0'

m = 15
n = 1
simmap1 = {}
simmap2 = {}
n0 = 1
sig = True

for n in range(1, 40):
    # print '\t', n, '\n\n'
    for i in range(0, 4717):
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
            elif data[i, 0] == '8':
                s8 += data[i, 2]
            elif data[i, 0] == '9':
                s9 += data[i, 2]
            elif data[i, 0] == '11':
                s11 += data[i, 2]
    a = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s11]
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = ""
    N = []
    F = []
    # print s1
    for i in range(0, 10):
        for j in range(0, 10):
            if len(a[i]) >= 10 and len(a[j]) >= 10:
                # print distance(a[i], a[j])
                # print distance(a[i],a[j]),i+1,j+1
                F.append(distance(a[i], a[j]))
            else:
                F.append(-1)
                sig = False
        # print "\n"
        if F != []:
            N.append(F)
        F = []

    # print N
    if N != [] and sig:
        simm = np.array(N)
        simmap1[n0] = simm
        simmap2[n0] = simm
        n0 += 1
        N = []
    else:
        N = []
        sig = True
    # print n


# print s1,'\n',s2,'\n',s4,'\n',s6,'\n',s7,'\n',s8,'\n',s11,'\n',s13

#print distance(s1,s2)
#print distance(s1,s4)
#print distance(s1,s5)

groupaffi = [[-1,1,0,0,0,0,0,0,0,0],
             [1,-1,0,0,0,0,0,0,0,0],
             [0,0,-1,1,0,0,0,0,0,0],
             [0,0,1,-1,0,0,0,0,0,0],
             [0,0,0,0,-1,1,1,0,0,0],
             [0,0,0,0,1,-1,1,0,0,0],
             [0,0,0,0,1,1,-1,0,0,0],
             [0,0,0,0,0,0,0,-1,1,1],
             [0,0,0,0,0,0,0,1,-1,1],
             [0,0,0,0,0,0,0,1,1,-1]]

# 取矩阵平均值
arraylen = len(simmap1)

if arraylen == 1:
    for i in range(0, 10):
        for j in range(0, 10):
            simmap2[1][i, j] = simmap1[1][i, j]
else:
    # 头尾
    for i in range(0, 10):
        for j in range(0, 10):
            simmap2[1][i, j] = (simmap1[1][i, j] + simmap1[2][i, j]) / 2
            simmap2[arraylen][i, j] = (simmap1[arraylen - 1][i, j] + simmap1[arraylen][i, j]) / 2

    for windowsNumber in range(2, arraylen):
        for i in range(0, 10):
            for j in range(0, 10):
                simmap2[windowsNumber][i, j] = (simmap1[windowsNumber - 1][i, j]
                                                + simmap1[windowsNumber][i, j]
                                                + simmap1[windowsNumber + 1][i, j]) / 3

result = {}
th = {}
acc = {}
threshold = 0.0
total = 45
count = 0
# print simmap[32][1,0]
while threshold < 15.0:
    accuracy = 0.0
    for windowsNumber in range(1, arraylen+1):
        pos = 0
        for ui in range(0, 10):
            for uj in range(0, 10):
                if ui < uj:
                    if int(simmap2[windowsNumber][ui, uj]) <= threshold:
                        if groupaffi[ui][uj] == 1:
                            pos += 1
                    else:
                        if groupaffi[ui][uj] == 0:
                            pos += 1
        acc[windowsNumber] = float(pos)/total
        accuracy += acc[windowsNumber]
    accuracy /= arraylen
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


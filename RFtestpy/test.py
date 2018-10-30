# -*- coding:utf-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestClassifier

import csv

with open('train1.csv') as ftr:
    trainreader = csv.reader(ftr);
    trainset = list(trainreader)
    for i in range(len(trainset)):
        trainset[i] = [float(x) for x in trainset[i]]
    #print trainset
    train = np.array(trainset)

data = train[:, 2:32]
target = train[:, 1]
#print data
rf = RandomForestClassifier(n_estimators=10, max_features=6)  # 这里使用了默认的参数设置
rf.fit(data, target)  # 进行模型的训练
#    
# 随机挑选两个预测不相同的样本
with open('test1.csv') as fte:
    testreader = csv.reader(fte);
    testset = list(testreader)
    for i in range(len(testset)):
        testset[i] = [float(x) for x in testset[i]]
    #print testset
    test = np.array(testset)

idata = test[:, 2:32]
itarget = test[:, 1]
#print idata
for i in range(0, 850):
    print 'phone no:\t', test[i, 0], '\ttrue value:\t', itarget[i], '\tPrediction:\t', rf.predict(idata[i])

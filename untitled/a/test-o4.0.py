# -*- coding:utf-8 -*-
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Imputer

import csv

with open('train_feature_train_o.csv') as ftr:
    trainreader = csv.reader(ftr);
    trainset = list(trainreader)
    for i in range(len(trainset)):
        trainset[i] = [float(x) for x in trainset[i]]

    train = np.array(trainset)
    # 会报错，因为数据的问题
    train = Imputer().fit_transform(train)

data = train[:, 2:33]
target = train[:, 1]

rf = RandomForestClassifier(n_estimators=10, max_features=6)  # 这里使用了默认的参数设置
rf.fit(data, target)  # 进行模型的训练
#
# 随机挑选两个预测不相同的样本
with open('12_features.csv') as fte:
    testreader = csv.reader(fte);
    testset = list(testreader)
    for i in range(len(testset)):
        testset[i] = [float(x) for x in testset[i]]
    test = np.array(testset)

idata = test[:, 2:33]
iid = test[:, 0]


s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = ""


for i in range(0, 879):
    a = int(rf.predict(idata[i]))
    # print 'phone no:\t', test[i, 0], '\ttrue value:\t', itarget[i], '\tPrediction:\t',
    if a==10:
        a=0
    else:
        a=a
    #print int(rf.predict(idata[i]))
    #print a

    if iid[i] == 1.0:
        s1 += str(a)
    elif iid[i] == 2.0:
        s2 += str(a)
    elif iid[i] == 3.0:
        s3 += str(a)
    elif iid[i] == 4.0:
        s4 += str(a)
    elif iid[i] == 5.0:
        s5 += str(a)
    elif iid[i] == 6.0:
        s6 += str(a)
    elif iid[i] == 7.0:
        s7 += str(a)
    elif iid[i] == 8.0:
        s8 += str(a)
    elif iid[i] == 9.0:
        s9 += str(a)
    elif iid[i] == 10.0:
        s10 += str(a)
    elif iid[i] == 11.0:
        s11 += str(a)

    #print s10
b = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
for i in range(0, 11):
    print i+1, " : ", b[i]
    print "\n"


# print s1,'\n',s2,'\n',s4,'\n',s6,'\n',s7,'\n',s8,'\n',s11,'\n',s13

#print distance(s1,s2)
#print distance(s1,s4)
#print distance(s1,s5)

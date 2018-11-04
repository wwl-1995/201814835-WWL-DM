import time
from os import listdir
from math import log
from numpy import *
from numpy import linalg
from operator import itemgetter

def doProcess():    #主函数
    trainFiles = 'D:/dataset1/train-TFIDF.txt'
    testFiles = 'D:/dataset1/test-TFIDF.txt'
    knnResultFile = 'D:/dataset1/KNN.txt'
    #训练集
    trainDocWordMap = {}
    for line in open(trainFiles).readlines():
        lineSplitBlock = line.strip('\n').split(' ')  #去掉空行，按空格分块
        trainWordMap = {}
        m = len(lineSplitBlock)-1   #？
        for i in range(2,m,2):  #在每个文档向量中提取word，TF-IDF
            trainWordMap[lineSplitBlock[i]] = lineSplitBlock[i+1]
        tem_key = lineSplitBlock[0] + '_' +lineSplitBlock[1]   #在每个文档向量中提取file，data
        trainDocWordMap[tem_key] = trainWordMap
    #测试集
    testDocWordMap = {}
    for line in open(testFiles).readlines():
        lineSplitBlock = line.strip('\n').split(' ')
        testWordMap = {}
        n = len(lineSplitBlock) - 1
        for i in range(2, n, 2):
            testWordMap[lineSplitBlock[i]] = lineSplitBlock[i + 1]
        tem_key = lineSplitBlock[0] + '_' + lineSplitBlock[1]
        testDocWordMap[tem_key] = testWordMap

    #遍历每一个测试样例计算与所有训练样本的距离，做分类
    count = 0
    rightCount = 0
    knnResultWriter = open(knnResultFile, 'w')    #结果写入文档中
    for item in testDocWordMap.items():
        classifyResult = knnComputeCate(item[0], item[1], trainDocWordMap) #调用knnComputeCate(）函数做分类
        count += 1
        print(' this is %d round' % count)
        classifyRight = item[0].split('_')[0]
        knnResultWriter.write('%s %s\n' % (classifyRight, classifyResult))  #正确分类结果与原始分类结果写入文档中
        if classifyRight == classifyResult:  #如果分类正确，加1
            rightCount += 1
        print('%s %s  rightCount: %d' % (classifyRight, classifyResult, rightCount))
    acc = float(rightCount)/float(count)
    print('rightCount %d,count: %d,acc: %.6f' % (rightCount, count, acc))
    return acc

def knnComputeCate(cate_Doc, testDic, trainMap):    #做分类
    simMap = {}  #文件名，距离
    for item in trainMap.items():
        similarity = computeSim(testDic, item[1])   #调用函数计算距离
        simMap[item[0]] = similarity
    sortedSimMap = sorted(simMap.items(), key=itemgetter(1), reverse=True)
    k = 18
    cateSimMap = {}  #类，距离和
    for i in range(k):
        cate = sortedSimMap[i][0].split('_')[0]
        cateSimMap[cate] = cateSimMap.get(cate, 0) + sortedSimMap[i][1]
    sortedCateSimMap = sorted(cateSimMap.items(), key=itemgetter(1), reverse=True)
    return sortedCateSimMap[0][0]



def computeSim(testDic, trainDic):    #计算距离
     testList = []   #测试向量与训练向量共有的词在测试向量中的TFIDF值
     trainList = []   #训练
     for word, weight in testDic.items():
         if word in trainDic:  #如果word在训练字典中
             testList.append(float(weight))   #在列表末尾加入weight
             trainList.append((float(trainDic[word])))   #在列表末尾加入word
     testVect = mat(testList)   #列表转矩阵
     trainVect = mat(trainList)   #便于下面向量相乘运算和使用numpy模块的范式函数计算
     num = float(testVect*trainVect.T)
     denom = linalg.norm(testVect)*linalg.norm(trainVect)
     return float(num)/(1.0+float(denom))

doProcess()















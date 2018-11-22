import os
import math
from os import path, listdir
from math import log
def computeAcc(rightCate,resultCate):

    rightCateDict = {}
    resultCateDict = {}
    rightCount = 0.0

    for line in open(rightCate).readlines():  #正确分类
        (sampleFile, cate) = line.strip('\n').split(' ')
        rightCateDict[sampleFile] = cate
    for line in open(resultCate).readlines():   #结果分类
        (sampleFile, cate) = line.strip('\n').split(' ')
        resultCateDict[sampleFile] = cate
    for sampleFile in rightCateDict.keys():
        if (rightCateDict[sampleFile] == resultCateDict[sampleFile]):
            rightCount += 1.0
    print('rightCount ：%d rightCate: %d' % (rightCount ,len(rightCateDict)))
    acc = rightCount/len(rightCateDict)
    print('acc %d :' % acc)
    return acc

if __name__ == '__main__':
    rightCate = 'D:/dataset1/classReC.txt'
    resultCate = 'D:/dataset1/result.txt'
    computeAcc(rightCate, resultCate)


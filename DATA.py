import time
from os import listdir
from math import log
#from numpy import *
#from numpy import linalg
from operator import itemgetter

###################################################
## 计算所有单词的IDF值
###################################################
def computeIDF():
    fileDir = 'processedSampleOnlySpecial_2'
    wordDocMap = {}  # <word, set(docM,...,docN)>
    IDFPerWordMap = {}  # <word, IDF值>
    countDoc = 0.0
    cateList = listdir(fileDir)
    for i in range(len(cateList)):
        sampleDir = fileDir + '/' + cateList[i]
        sampleList = listdir(sampleDir)
        for j in range(len(sampleList)):
            sample = sampleDir + '/' + sampleList[j]
            for line in open(sample).readlines():
                word = line.strip('\n')
                if word in wordDocMap.keys():
                    wordDocMap[word].add(sampleList[j])  # set结构保存单词word出现过的文档
                else:
                    wordDocMap.setdefault(word, set())
                    wordDocMap[word].add(sampleList[j])
        print
        'just finished %d round ' % i

    for word in wordDocMap.keys():
        countDoc = len(wordDocMap[word])  # 统计set中的文档个数
        IDF = log(20000 / countDoc) / log(10)
        IDFPerWordMap[word] = IDF

    return IDFPerWordMap
import time
from os import listdir
from math import log
from numpy import *
from numpy import linalg
from operator import itemgetter

strainfilepath = 'D:/dataset1/straindataset'
stestfilepath = 'D:/dataset1/stestdataset'

#计算所有单词的IDF值

#（1）在过滤后的训练集上计算
def computeIDF():
    wordDocMap = {}
    IDFPerWordMap = {}
    countDoc = 0.0
    strainflist = listdir(strainfilepath) #训练集上的文件夹列表
    #stestflist = listdir(stestfilepath)   #测试集上的文件夹列表
    for i in range(len(strainflist)):
        strainfdir = strainfilepath + '/' + strainflist[i]
        straindlist = listdir(strainfdir)
        for j in range(len(straindlist)):
            sample = strainfdir + '/' + straindlist[j]
            for line in open(sample).readlines():
                word = line.strip('\n')
                if word in wordDocMap.keys():
                    wordDocMap[word].add(straindlist[j])
                else:
                    wordDocMap.setdefault(word, set())
                    wordDocMap[word].add(straindlist[j])
        print('use %d round' % i)

    for word in wordDocMap.keys():
        countDoc = len(wordDocMap[word])
        IDF = log(20000/countDoc)/log(10)
        IDFPerWordMap[word] = IDF
    return IDFPerWordMap

#将IDF值写入保存
def main():
    print("hello")
    start = time.perf_counter()
    IDFPerWordMap = computeIDF()
    end = time.perf_counter()
    print('runtime:' + str(end-start))
    fw = open('D:/dataset1/train-IDF.txt', 'w')
    for word ,IDF in IDFPerWordMap.items():
        fw.write('%s %.6f\n' % (word, IDF))
    fw.close()

#main()

#生成文档向量,并计算TF与IDF成绩
def computeTFIDF():
    IDFPerWord = {}
    tsTrainWriter = open('D:/dataset1/train-TFIDF.txt', 'w')    #IDFTF写入txt中
   # tsTestWriter = open('D:/dataset1/test-TFIDF.txt', 'w')
    for line in open ('D:/dataset1/train-IDF.txt').readlines():   #读取计算出的IDF.txt
        (word , IDF)= line.strip('\n').split(' ')
        IDFPerWord[word] = IDF
    strainflist = listdir(strainfilepath)  # 训练集上的文件夹列表
    #stestflist = listdir(stestfilepath)  # 测试集上的文件夹列表
    for i in range(len(strainflist)):
        strainfdir = strainfilepath + '/' + strainflist[i]
        straindlist = listdir(strainfdir)
        for j in range(len(straindlist)):
            TFPerDocMap = {}
            sumPerDoc = 0
            sample = strainfdir + '/' + straindlist[j]
            for line in open(sample).readlines():
                sumPerDoc +=1
                word = line.strip('\n')
                TFPerDocMap[word] = TFPerDocMap.get(word, 0)+1
            tsTrainWriter.write('%s %s ' %(strainflist[i],straindlist[j]))    #文件夹，数据文件
            for word,count in TFPerDocMap.items():
                TF = float(count)/float(sumPerDoc)
                d = float(IDFPerWord[word])
                tfd = TF * d
                tsTrainWriter.write('%s %f ' % (word, tfd))
            tsTrainWriter.write('\n')
        print('use %d round' % i)
    tsTrainWriter.close()
computeTFIDF()

#(2)在过滤后的测试集上训练
def computeIDF():
    wordDocMap = {}
    IDFPerWordMap = {}
    countDoc = 0.0
    #strainflist = listdir(strainfilepath) #训练集上的文件夹列表
    stestflist = listdir(stestfilepath)   #测试集上的文件夹列表
    for i in range(len(stestflist)):
        stestfdir = stestfilepath + '/' + stestflist[i]
        stestdlist = listdir(stestfdir)
        for j in range(len(stestdlist)):
            sample = stestfdir + '/' + stestdlist[j]
            for line in open(sample).readlines():
                word = line.strip('\n')
                if word in wordDocMap.keys():
                    wordDocMap[word].add(stestdlist[j])
                else:
                    wordDocMap.setdefault(word, set())
                    wordDocMap[word].add(stestdlist[j])
        print('use %d round' % i)

    for word in wordDocMap.keys():
        countDoc = len(wordDocMap[word])
        IDF = log(20000/countDoc)/log(10)
        IDFPerWordMap[word] = IDF
    return IDFPerWordMap

#将IDF值写入保存
def main():
    print("hello")
    start = time.perf_counter()
    IDFPerWordMap = computeIDF()
    end = time.perf_counter()
    print('runtime:' + str(end-start))
    fw = open('D:/dataset1/test-IDF.txt', 'w')
    for word ,IDF in IDFPerWordMap.items():
        fw.write('%s %.6f\n' % (word, IDF))
    fw.close()

#main()

#生成文档向量,并计算TF与IDF成绩
def computeTFIDF():
    IDFPerWord = {}
    #tsTrainWriter = open('D:/dataset1/train-TFIDF.txt', 'w')    #IDFTF写入txt中
    tsTestWriter = open('D:/dataset1/test-TFIDF.txt', 'w')
    for line in open ('D:/dataset1/test-IDF.txt').readlines():   #读取计算出的IDF.txt
        (word , IDF)= line.strip('\n').split(' ')
        IDFPerWord[word] = IDF
    #strainflist = listdir(strainfilepath)  # 训练集上的文件夹列表
    stestflist = listdir(stestfilepath)  # 测试集上的文件夹列表
    for i in range(len(stestflist)):
        stestfdir = stestfilepath + '/' + stestflist[i]
        stestdlist = listdir(stestfdir)
        for j in range(len(stestdlist)):
            TFPerDocMap = {}
            sumPerDoc = 0
            sample = stestfdir + '/' + stestdlist[j]
            for line in open(sample).readlines():
                sumPerDoc +=1
                word = line.strip('\n')
                TFPerDocMap[word] = TFPerDocMap.get(word, 0)+1
            tsTestWriter.write('%s %s ' %(stestflist[i],stestdlist[j]))    #文件夹，数据文件
            for word,count in TFPerDocMap.items():
                TF = float(count)/float(sumPerDoc)
                d = float(IDFPerWord[word])
                tfd = TF * d
                tsTestWriter.write('%s %f ' % (word, tfd))
            tsTestWriter.write('\n')
        print('use %d round' % i)
    tsTestWriter.close()
computeTFIDF()






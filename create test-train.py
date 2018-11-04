import re, nltk, operator,os
from numpy import *
from os import listdir,mkdir,path
from nltk.corpus import stopwords

#定义一个函数，把预处理好的数据集分成0.2的测试集，0.8的训练集
def createTestSample(index, classifyRightCate,p=0.8):
    fr = open(classifyRightCate, 'w')
    prefilepath = 'D:/dataset1/predataset/'  #预处理好的数据集路径
    testpath = 'D:/dataset1/testsample/'      #存放测试集的路径
    trainpath = 'D:/dataset1/trainsample/'     #存放训练集的路径
    prefilelist = listdir(prefilepath)    #20个文件夹
    for i in range(len(prefilelist)):
        prefiledir = prefilepath + '/' + prefilelist[i]  #每个文件夹的路径
        predatalist = listdir(prefiledir)  #返回每个文件夹里的数据文件
        k = len(predatalist)   #每个文件夹里的数据文件数
        testBeginIndex = index * (k * (1-p))   #？
        testEndIndex = (index + 1)*(k * (1-p))
        for j in range(k):    #序号在规定区间内的作为测试样本，
            if(j > testBeginIndex)and (j < testEndIndex):
                fr.write('%s %s\n' % (predatalist[j], prefilelist[i]))
                targetdir= testpath + str(index)+'/'+prefilelist[i]  #生成类别-序号文件
            else:
                targetdir = trainpath + str(index)+'/'+prefilelist[i]

            if path.exists(targetdir)==False:
                os.makedirs(targetdir)
            predatadir = prefiledir + '/' + predatalist[j]  #数据文件地址
            sample = open(predatadir).readlines()    #读取每篇数据文件的内容
            sampleWriter = open(targetdir + '/' +predatalist[j], 'w')  #对每篇数据文件进行写入
            for line in sample:
                sampleWriter.write('%s\n' % line.strip('\n'))
            sampleWriter.close()
    fr.close()

for i in range(5):
    classifyRightCate = 'classifyRightCate' + str(i) + '.txt'
    createTestSample(i, classifyRightCate)
    print("分割完成！")

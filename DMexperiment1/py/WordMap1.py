import re, nltk, operator,os
from numpy import *
from os import listdir,mkdir,path
from nltk.corpus import stopwords

#构造词典
trainpath = 'D:/dataset1/trainsample/2/'
def createW():
    WM= {}   #原始词典
    NWM= {}   #新词典
    trainflist = listdir(trainpath)

    for i in range(len(trainflist)):   #循环20个文件夹
        trainfdir = trainpath + trainflist[i]  #每个文件夹地址
        traindlist = listdir(trainfdir)   #文件夹里边的数据文件列表
        for j in range(len(traindlist)):  #循环处理每个文件夹里边的数据文件
           trainddir = trainfdir + '/'+ traindlist[j]  #每个数据文件地址
           for line in open(trainddir).readlines():    #处理每个数据文件
               word = line.strip('\n')
               WM[word] = WM.get(word, 0.0)+1.0     #返回指定的词，若不存在，返回默认值
    for key, value in WM.items():   #出现次数大于10的单词
        if value > 10:
            NWM[key] = value

    print('WM size : %d' % len(WM))   #输出原始词典的长度
    print('NWM size : %d' % len(NWM))    #输出新词典的长度
    return NWM

#打印字典
def PWM():
    print("print word map")
    fr = open('D:/dataset1/newWordMap.txt','w')    #打开词典文件
    NWM = createW()   #分类词典
    for key,count in NWM.items():
        fr.write('%s %.1f\n' % (key, count))


#PWM()

#特征词选取,生成20个文件夹，每个文件夹的每篇文档存放本篇数据文件的特征词
strainfilepath = 'D:/dataset1/straindataset'
stestfilepath = 'D:/dataset1/stestdataset'
trainfilepath = 'D:/dataset1/trainsample/2/'
testfilepath = 'D:/dataset1/testsample/2/'

#在训练集上进行过滤
def filterTrainSPwords():
    WMdict =createW()
    trainflist = listdir(trainfilepath)
    for i in range(len(trainflist)):
        strainfdir = strainfilepath + '/'+trainflist[i]  #新的文件夹路径
        trainfdir = trainfilepath+'/'+trainflist[i]
        if path.exists(strainfdir) == False:
            os.makedirs(strainfdir)
        sample = listdir(trainfdir)
        for j in range(len(sample)):
            strainddir = strainfdir + '/' + sample[j]
            fr = open(strainddir, 'w')
            trainddir = trainfdir + '/' + sample[j]
            for line in open(trainddir).readlines():
                word = line.strip('\n')
                if word in WMdict.keys():
                    fr.write('%s\n' % word)
            fr.close()
#filterTrainSPwords()


#在测试集上进行过滤
def filterTestSPwords():
    WMdict =createW()
    testflist = listdir(testfilepath)
    for i in range(len(testflist)):
        stestfdir = stestfilepath + '/'+testflist[i]  #新的文件夹路径
        testfdir = testfilepath+'/'+testflist[i]
        if path.exists(stestfdir) == False:
            os.makedirs(stestfdir)
        sample = listdir(testfdir)
        for j in range(len(sample)):
            stestddir = stestfdir + '/' + sample[j]
            fr = open(stestddir, 'w')
            testddir = testfdir + '/' + sample[j]
            for line in open(testddir).readlines():
                word = line.strip('\n')
                if word in WMdict.keys():
                    fr.write('%s\n' % word)
            fr.close()

#filterTestSPwords()
from math import log
from os import listdir,mkdir ,path
def CountWords(strdir):    #统计训练样本中每个单词的出现次数，及每个目录下的单词总数
    cateWordsNum = {}
    cateWordsProb = {}
    CateDir = listdir(strdir)  #每个类别文件
    for i in range(len(CateDir)):  #循环20个文件夹
        count = 0
        sampleDir = strdir + '/' + CateDir[i]   #每个文件夹地址
        sample = listdir(sampleDir) #文件夹里的文档
        for j in range(len(sampleDir)):  #循环文件夹里所有文档
            sampleFile = sampleDir + '/'+sample[j]   #每篇文档地址
            words = open(sampleFile).readlines()  #读取每篇文档的单词
            for line in words:
                count = count + 1
                word = line.strip('\n')
                keyName = CateDir[i] + '_' + word
                cateWordsProb[keyName] = cateWordsProb.get(keyName, 0)+1 #记录每个文档中每个单词的出现次数
        cateWordsNum[CateDir[i]] = count  #每个文件夹里的单词总数
        print('cate %d contains %d' % (i, cateWordsNum[CateDir[i]]))  #输出每个文件夹里的单词总数
    print('cate-word size: %d' % len(cateWordsProb))  #输出每个单词的出现次数
    return cateWordsProb,cateWordsNum

#用贝叶斯对测试文档分类
def NBprocess(traindir,testdir,classifyResultFileNew):

    crWriter = open(classifyResultFileNew,'w')  #写入分类结果文件

    cateWordsNum, cateWordsProb =CountWords(traindir)  #返回类k下词c的出现次数，类k总词数
    trainTotalNum= sum(cateWordsNum.values())      #训练集的总词数
    print('trainTotalNum: %d' % trainTotalNum)
    #开始对测试集做分类
    testDirFiles = listdir(testdir)   #测试集下的20个文件夹
    for i in range(len(testDirFiles)):  #对20个文件夹循环
        testSampleDir = testdir + '/' +testDirFiles[i]    #每个文件夹的地址
        testSample = listdir((testSampleDir))      #每个文件夹的所有文档
        for j in range(len(testSample)):  #处理每篇文档
            testFilesWords = []
            sampleDir = testSampleDir + '/' + testSample[j]   #每篇文档地址
            lines = open(sampleDir).readlines()  #读取每篇文档的每一行
            for line in lines:     #处理每一行
                word = line.strip('\n')
                testFilesWords.append(word)


            maxP = 0.0
            trainDirFiles = listdir(traindir)  #训练集下的20个文件夹
            for k in range(len(trainDirFiles)):  #对20个文件夹循环
                #p = computeCateProb(trainDirFiles[k],testFilesWords,WordNum,trainTotalNum,WordProb)
                #计算最佳的p值
                p = computeCateProb(trainDirFiles[k], testFilesWords,cateWordsNum, trainTotalNum, cateWordsProb)
                if k == 0:
                    maxP = p
                    bestCate = trainDirFiles[k]    #第k个文件夹
                    continue
                if p > maxP:
                    maxP = p
                    bestCate = trainDirFiles[k]
            crWriter.write('%s %s\n' % (testSample[j] , bestCate))
    crWriter.close()

def computeCateProb(traindir,testFileWords,cateWordsNum,totalWordsNum,cateWordsProb):
    prob = 0
    wordNumInCate = cateWordsNum[traindir]  #类k下单词总数
    for i in range(len(testFileWords)):   #循环类k下的测试文档
        keyName = traindir + '_' + testFileWords[i]
        if keyName in cateWordsProb.keys():
            testFileWordNumInCate = cateWordsProb[keyName]  #类k下词c出现的次数

        else:testFileWordNumInCate = 0.0
        xcProb = log((testFileWordNumInCate + 0.0001)/(wordNumInCate + totalWordsNum))  #求对数避免下溢出
        # 条件概率 =（类k中单词i的数目+0.0001）/（类k中单词总数+训练样本中所有类单词总数）
        prob = prob + xcProb  #
    res = prob + log(wordNumInCate) - log(totalWordsNum)
    return res



if __name__ == '__main__':
    classifyResultFileNew = 'D:/dataset1/classReC.txt'
    traindir = 'D:/dataset1/trainsample/1/'  # 训练集样本
    testdir = 'D:/dataset1/testsample/1/'  # 测试集样本
    NBprocess(traindir, testdir, classifyResultFileNew)













#数据预处理

import re, nltk, operator
from numpy import *
from os import listdir,mkdir,path
from nltk.corpus import stopwords

filepath = 'D:/dataset1/20news-18828/'
prefilepath = 'D:/dataset1/predataset/'

#创建新文件夹，存放预处理后的数据
def CF():
    flist = listdir(filepath)   #返回20个文件夹名字
    for i in range(len(flist)):  #对20个文件夹里的数据文件进行处理
        #if i== 0: continue
        ddir = filepath + flist[i]  #每个文件夹路径
        dlist = listdir(ddir)   #返回每个文件夹里的数据文件
        predir = prefilepath + flist[i]     #预处理的文件夹路径
        if path.exists(predir) == False:
            mkdir(predir)
        else:
            print('%s exists' % predir)
        for j in range(len(dlist)):   #对每个数据文件进行处理
            CPF(flist[i], dlist[j])
            print('%s %s' % (flist[i], dlist[j]))
    print("preprocessing finished！")

#定义数据文件处理函数
def CPF(flistname,dlistname):
    datapath = filepath +flistname +'/'+dlistname  #原始数据文件地址
    predatapath = prefilepath + flistname +'/'+dlistname   #预处理后的数据文件地址
    fw = open(predatapath, 'w')    #打开新的数据文件，进行写入
    countdlist = open(datapath, encoding='utf8', errors='ignore').readlines()  #读取原始数据文件的行数,
                                                                              # 不加encoding和errors运行会报错
    for line in countdlist:  #对每个数据文件进行循环处理
        resline = lineprocess(line)  #调用行处理函数
        for word in resline:  #对每行文本进行循环
            fw.write("%s\n" % word)   #一行一个单词输出
    fw.close()


#定义行处理函数:去除非字母字符，转换大写为小写，去停用词
def lineprocess(line):
    stopwords= nltk.corpus.stopwords.words('english')   #去停用词
    porter = nltk.PorterStemmer()  #词干分析
    splitter = re.compile('[^a-zA-Z]')    #去除非字母字符，形成分隔
    #words = [porter.stem(word.lower())] for word in splitter.split(line) \
       # if len(word)>0 and word.lower() not in stopwords]
    words = [porter.stem(word.lower()) for word in splitter.split(line) \
             if len(word) > 0 and \
             word.lower() not in stopwords]
    return words

if __name__ == '__main__':
   CF()








import json
import sklearn
from sklearn.cluster import *
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize

dataDict = {}
data = []   #读入的数据
dataLabels = []  #类标签
dataCluster = []   #聚类结果
vec = []  #文本转化的向量

def readTweets():  #处理文本
    global dataDict, data, dataLabels, vec
    dataset = open('D:/dataset3/Tweets.txt', 'r')
    print("读取文本成功！")
    for line in dataset.readlines():
        dataDict = json.loads(line)
        data.append(dataDict['text'])
        dataLabels.append(dataDict['cluster'])
    vectorizer = TfidfVectorizer()
    vec = vectorizer.fit_transform(data)
    print("文本转化为向量成功！")




def Kmeans():
    global dataCluster,dataLabels, vec
    dataCluster = KMeans(n_clusters=100, random_state=10,).fit_predict(vec)
    nmi= normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of KMeans :', nmi)
def MBKmeans():
    global dataCluster, dataLabels, vec
    dataCluster = MiniBatchKMeans(n_clusters=100, random_state=10).fit_predict(vec)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of MiniBatchKMeans :', nmi)
def AffP():
    global dataCluster, dataLabels, vec
    clustering = AffinityPropagation().fit(vec)
    dataCluster = clustering.labels_
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of AffinityPropagation :', nmi)
def meanShift():
    global dataCluster, dataLabels, vec
    clustering = vec.toarray()
    dataCluster = MeanShift().fit_predict(clustering)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of MeanShift :', nmi)
def SpClustering():
    global dataCluster, dataLabels, vec
    dataCluster = SpectralClustering(n_clusters=100).fit_predict(vec)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of SpectralClustering :', nmi)
def AggClustering():
    global dataCluster, dataLabels, vec
    clustering = vec.toarray()
    dataCluster = AgglomerativeClustering(n_clusters=100).fit_predict(clustering)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of AgglomerativeClustering :', nmi)
def dbScan():
    global dataCluster, dataLabels, vec
    dataCluster = DBSCAN(eps=1.13).fit_predict(vec)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of DBSCAN :', nmi)
def birch():
    global dataCluster, dataLabels, vec
    dataCluster = Birch(n_clusters=100).fit_predict(vec)
    nmi = normalized_mutual_info_score(dataLabels, dataCluster)
    print('the NMI of Birch :', nmi)



if __name__ == '__main__':
    readTweets()
    Kmeans()
    MBKmeans()
    AffP()
    meanShift()
    SpClustering()
    AggClustering()
    dbScan()
    birch()
    print("测试成功！")









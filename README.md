# 201814835wangweilin
---对给定的20组新闻数据进行预处理，并得到每个文本的VSM表示<br>
---实现KNN分类器，测试其在给定数据集上的效果<br>
(1)data preprocess.py 实现了数据预处理，包括去停用词，词干分析等<br>
(2)create test-train.py 将数据集划分为20%的测试集，80%的训练集<br>
(3)wordMap1.py 构造词典，并进行过滤，将出现次数小于10的词过滤掉，进行特征词筛选<br>
(4)TF-IDF.py 计算TF-IDF<br>
(5)KNN.py  生成向量，并实现knn，统计分类正确的次数，计算acc<br>


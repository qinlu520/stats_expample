import numpy as np
import jieba

# 欧氏距离(Euclidean distance)


def euclidean(x, y):
    return np.sqrt(np.sum((x - y)**2))


# 曼哈顿距离(Manhattan distance)


def manhattan(x, y):
    return np.sum(np.abs(x - y))


# 切比雪夫距离(Chebyshev distance)


def chebyshev(x, y):
    return np.max(np.abs(x - y))


# 闵可夫斯基距离(Minkowski distance)


def minkowski(x, y, p):
    return np.sum(np.abs(x - y) ** p) ** (1 / p)


# 汉明距离(Hamming distance)


def hamming(x, y):
    return np.sum(x != y) / len(x)


# 马氏距离(Mahalanobis Distance)


def mahalanobis(x, y):
    xv = np.vstack([x, y])
    xt = xv.T
    si = np.linalg.inv(np.cov(xv))  # 协方差矩阵的逆矩阵
    # 马氏距离计算两个样本之间的距离，此处共有10个样本，两两组合，共有45个距离。
    n = xt.shape[0]
    d1 = []
    for i in range(0, n):
        for j in range(i+1, n):
            delta = xt[i]-xt[j]
            d = np.sqrt(np.dot(np.dot(delta, si), delta.T))
            d1.append(d)
    return d1


# 标准化欧氏距离 (Standardized Euclidean distance)


def standardized_euclidean(x, y):
    return np.sqrt(((x - y) ** 2 / np.var(np.vstack([x, y]), axis=0, ddof=1)).sum())


# 皮尔逊相关系数(Pearson correlation coefficient)


def pearson(x, y):
    return np.corrcoef(x, y)


# 余弦相似度(Cosine similarity)


def cos_sim(x, y):
    x = np.mat(x)
    y = np.mat(y)
    num = float(np.vstack([x, y]) * y.T)
    denom = np.linalg.norm(np.vstack([x, y])) * np.linalg.norm(y)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim


# 杰卡德相似度(Jaccard index)


def Jaccrad(model, reference):  # terms_reference为源句子，terms_model为候选句子
    terms_reference = jieba.cut(reference)  # 默认精准模式
    terms_model = jieba.cut(model)
    grams_reference = set(terms_reference)  # 去重；如果不需要就改为list
    grams_model = set(terms_model)
    temp = 0
    for i in grams_reference:
        if i in grams_model:
            temp = temp+1
    fenmu = len(grams_model)+len(grams_reference)-temp  # 并集
    jaccard_coefficient = float(temp/fenmu)  # 交集
    return jaccard_coefficient
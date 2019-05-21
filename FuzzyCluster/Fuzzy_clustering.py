# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:44:41 2019

@author: zmddzf
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy


# 定义异常类
class ParamError(Exception):  # 继承异常类
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason


class FuzzyClustering:
    def __init__(self, lamb=None, membership='cosin'):
        """
        构造器，传入所需要取的lambda水平与隶属度函数类型
        :param lamb: 缺省情况下为空，即进行动态聚类
        :param membership: 隶属度函数类型，有余弦相似度(cosin)与欧式相似度(euclid)(1/(1+d))，缺省为余弦相似度
        """
        self.lamb = None
        self.membership = membership

    def __cosin(self, x1, x2):
        """
        计算余弦相似度
        :param x1: numpy.array向量
        :param x2: numpy.array向量
        :return cosin_dist: 余弦相似度
        """
        cosin_dist = x1.dot(x2) / (sum(x1 ** 2) ** 0.5 * sum(x2 ** 2) ** 0.5)
        return cosin_dist

    def __euclid(self, x1, x2):
        """
        计算欧式相似度
        :param x1: numpy.array向量
        :param x2: numpy.array向量
        :return eusim: 欧式相似度
        """
        eudist = sum((x1 - x2) ** 2) ** 0.5
        eusim = 1 / (1 + eudist)
        return eusim

    def simMat(self, X):
        """
        计算模糊相似矩阵
        :param X: 每一行为一个样本，每一列为一个特征
        :Mat: 模糊相似矩阵
        """
        if self.membership == 'cosin':
            memFun = self.__cosin
        elif self.membership == 'euclid':
            memFun = self.__euclid
        else:
            raise ParamError("ParamError", "Params error!")

        n = X.shape[0]
        Mat = []
        for i in range(n):
            Mat.append([memFun(X[i], X[j]) for j in range(n)])
        Mat = np.array(Mat)
        return Mat

    def __composition(self, Mat):
        """
        求相似度矩阵与自身的合成
        :param Mat: 相似度矩阵
        :return result: 合成运算后的矩阵
        """
        result = []
        for i in range(Mat.shape[0]):
            result.append([max(np.fmin(Mat[i, :], Mat[:, j])) for j in range(Mat.shape[0])])
        result = np.array(result)
        return result

    def equivalenceMat(self, Mat):
        """
        求模糊相似矩阵的模糊等价矩阵
        :param Mat: 相似度矩阵
        :return equiveMat: 模糊等价矩阵
        """
        mat = Mat.copy()
        while True:
            temp = mat.copy()
            mat = self.__composition(temp)
            if (temp == mat).all():
                return mat

    def cutSet(self, mat, lamb):
        """
        求模糊等价矩阵截集
        :param mat: 模糊等价矩阵
        :param lamb: 截lambda
        :return indexSet:
        """
        indexList = []
        for arr in mat:
            c = (arr >= lamb)
            c = [i if (c[i] == True) else None for i in range(len(c))]
            while None in c:
                c.remove(None)
            indexList.append(tuple(c))
        indexSet = list(set(indexList))
        indexSet = [set(t) for t in indexSet]
        return indexSet

    def clustering(self, X):
        """
        进行聚类操作
        :param X: 每一行为一个样本，每一列为一个特征
        :return cluster:
        """
        Mat = self.simMat(X)
        mat = self.equivalenceMat(Mat)
        memValue = set(mat.reshape(mat.shape[0] * mat.shape[1]))
        cluster = dict()
        if self.lamb == None:
            for value in memValue:
                cluster[value] = self.cutSet(mat, value)
            return cluster
        elif self.lamb < 0 or self.lamb > 1:
            raise ParamError("ParamError", "Params error! lambda should belong to 0 to 1!")
        else:
            cluster = self.cutSet(mat, self.lamb)
            return cluster


def compare(c1, c2):
    c = [x for x in c1 if x in c2]
    d = [y for y in (c2 + c1) if y not in c]
    return d



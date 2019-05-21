# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:14:51 2019

@author: zmddzf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten

def data_format(df, n_back):
    """
    将时间序列数据转换为可训练的类型
    基本假设为后一期数据受到前几期数据影响
    :param df: 时间序列
    :param n_back:
    :return new_df:
    """
    length = len(df)
    data = []
    target = []
    for i in range(0, length-n_back):
        data.append(df[i:i+n_back].values.T.tolist()[0])
        target.append(df[i+n_back: i+n_back+1].values.tolist()[0][0])
    return data, target
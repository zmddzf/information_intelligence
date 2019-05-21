# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:20:57 2019

@author: zmddzf
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

class Birds:
    """
    鸟群类，用于承载粒子群的数据结构
    """
    def __init__(self, popsize, dim):
        """
        鸟群构造器，初始化鸟群实例
        :param popsize: 种群个数
        :param dim: 问题维度
        :param indiv_best: 个体最优适应度
        :param group_best: 种群最优适应度
        :param position: 占位，种群坐标
        :param v_mat: 占位，种群速度
        :param best_position: 占位，最优位置
        """
        self.popsize = popsize
        self.dim = dim
        self.indiv_best = np.array([-1e10 for i in range(popsize)])
        self.group_best = -1e10
        self.position = None
        self.v_mat = None
        self.best_position = None
        self.best_indiv_posion = None
    
    def init_poplation(self, v_max, x_bound):
        """
        初始化鸟群位置和速度
        :param v_max: 最大速度
        :param x_bound: 位置向量约束条件，x_bound = [max=[],min=[]]
        """
        self.v_mat = np.random.uniform(0, v_max, (self.popsize, self.dim))
        self.position = np.random.uniform(x_bound[0],x_bound[1],(self.popsize, self.dim))
        self.best_indiv_posion = self.position.copy()
        
    
    def select_best(self, fitness_values):
        """
        选择最优的适应度与位置
        :param fitness_values: 个体的适应度向量
        """
        # 若当前适应度小于新的适应度，替换为新的适应度
        #print('fitness:', fitness_values)
        #print('preindiv:', self.indiv_best)
        self.best_indiv_posion[self.indiv_best < fitness_values] = self.position[fitness_values > self.indiv_best] 
        self.indiv_best[self.indiv_best < fitness_values] = fitness_values[fitness_values > self.indiv_best]


        
        # 选出当前种群最大的适应度
        self.group_best = max(self.indiv_best)
        # 选出当前种群最大适应度对应的位置
        self.best_position = self.best_indiv_posion[self.indiv_best.argmax()]


       
class PSO:
    """
    PSO算法的实现
    """
    def __init__(self, w, c1, c2, popsize, dim, x_bound, v_max, fitness_func):
        """
        PSO构造器
        :param w: 惯性因子
        :param c1: 自身经验加速常数
        :param c2: 社会经验加速常数
        :param popsize: 种群个数
        :param dim: 问题维度
        :param v_max: 最大速度
        :param x_bound: 位置向量约束条件，x_bound = [max=[],min=[]]
        :param fitness_fuc: 适应度函数，定义时需要能够支持向量的计算
        """
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.v_max = v_max
        self.popsize = popsize
        self.dim = dim
        self.x_bound = x_bound
        self.fitness_func = fitness_func
        self.birds = Birds(self.popsize, self.dim)
    
    def compute_fitness(self, X):
        """
        计算种群适应度
        :param X: X为行向量，每行代表一个位置
        :return fitness_values: 返回适应度向量，shape为(popsize)
        """
        fitness_values = self.fitness_func(X)
        fitness_values = fitness_values.reshape(self.popsize)
        return fitness_values
    
    def update(self):
        """
        更新位置与速度
        """
        self.birds.v_mat = self.w * self.birds.v_mat + self.c1 * np.random.rand() * (self.birds.best_indiv_posion - self.birds.position) + self.c2 * np.random.rand() * (self.birds.best_position - self.birds.position)
        self.birds.v_mat[self.birds.v_mat>self.v_max] = self.v_max
        self.birds.position = self.birds.position + self.birds.v_mat
        for i in range(len(self.x_bound[0])):
            self.birds.position[:,i][self.birds.position[:,i] < self.x_bound[0][i]] = self.x_bound[0][i]
            self.birds.position[:,i][self.birds.position[:,i] > self.x_bound[1][i]] = self.x_bound[1][i]

        #print('postposition:')
        #print(self.birds.position)

        
    def run(self, iter_n):
        # 初始化鸟群
        s_ = 'generation 0\nbest fitness_value:%f'%self.birds.group_best
        self.birds.init_poplation(self.v_max, self.x_bound)
        fitness_values = self.compute_fitness(self.birds.position)
        self.birds.select_best(fitness_values)
        
        position_list = self.birds.position
        
        diff_p = []
        
        best_fitness_hist = []
        best_position_hist = []
        
        s_ = ''
        for i in range(iter_n):
            
            s1 = 'generation %d \nbest fitness_value:%f'%(i, self.birds.group_best)


            w = 1 - i*0.0099999
            self.w = w
            self.update()
            
            position_list = np.hstack([position_list, self.birds.position])
            
            fitness_values = self.compute_fitness(self.birds.position)

            self.birds.select_best(fitness_values)
            
            best_fitness_hist.append(self.birds.group_best)
            best_position_hist.append(self.birds.best_position)
            s2 = 'group best:'+str(self.birds.group_best)
            s3 = 'best position:'+str(self.birds.best_position)

            s = '\n'+s1+'\n'+s2+'\n'+s3
            s_ = s_ + s

        position_list.reshape(self.popsize, iter_n+1, self.dim)
        return self.birds, best_fitness_hist, best_position_hist, s_

def func(x):
    """
    目标函数
    :param x: 自变量
    :return y: 函数值
    """
    y = x + 10*np.sin(5*x) + 7 * np.cos(4*x)
    return y

def sigmoid(x):
    return 1/(1+np.e**(-x))




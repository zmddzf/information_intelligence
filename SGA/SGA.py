# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:17:06 2019

@author: zmddzf
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def objfun(x):
    """
    目标函数
    :param x: 自变量
    :return y: 函数值
    """
    y = x + 10*np.sin(5*x) + 7 * np.cos(4*x)
    return y

def bit_length(bounder, precision):
    """
    计算二进制编码长度
    :param bounder: 变量边界，[lower, upper]
    :param precision: 计算精度
    :return length: 编码长度
    """
    length = int(np.ceil(np.log2((bounder[1] - bounder[0]) / precision+1)))
    return length

def bin_decoder(bin_num, bounder, length):
    """
    将二进制解码十进制
    :param bounder: 变量边界，[lower, upper]
    :param length: 编码长度
    :param bin_num: 二进制字符串
    :return bin_str: 十进制数
    """
    delta = (bounder[1] - bounder[0]) / (2**length - 1)
    x = eval('0b'+bin_num)
    decim_x = bounder[0] + x * delta
    return decim_x

def generate_pop(pop_size, length):
    """
    初始化种群
    :param pop_size: 种群容量
    :param length: 编码长度
    :return bin_population: 二进制编码种群
    """
    decim_population = np.random.randint(0, 2**length-1, pop_size)
    print(decim_population)
    bin_population = [('{:0%sb}'%length).format(x) for x in decim_population]
    return bin_population

def fitness_compute(population, fitness_func):    
    """
    计算种群的适应度
    :param population: 种群表现型
    :param fitness_fuc: 适应度函数
    :return fitness_val: 种群适应度值
    """
    fitness_val = []
    for pop in population:
        x = fitness_func(pop)
        fitness_val.append(x)
    return fitness_val

def select(population, fitness_val):
    """
    选择操作，用轮盘赌法进行选择
    :param population: 种群基因型
    :param fitness_val: 种群适应度
    :return selected_pop: 选择后的种群
    """
    f_sum = sum(fitness_val)
    cumulative = []
    for i in range(1, len(fitness_val)+1):
        cumulative.append(sum(fitness_val[:i]) / f_sum)
    
    selected_pop = []
    for i in range(len(fitness_val)):
        rand = np.random.rand()
        prand = [(c - rand) for c in cumulative]
        j = 0
        while prand[j] < 0:
            j = j+1
        selected_pop.append(population[j]) 
        
    return selected_pop

def crossover(population, length, Pc=0.8):
    """
    交叉操作，默认交叉概率为0.8
    """
    # 根据交叉概率计算交叉个体数目
    num = np.uint8(len(population) * Pc)
    # 保证偶数个交叉
    if num % 2 != 0:
        num = num + 1
    
    index = random.sample(range(len(population)), num)
    
    new_population = []
    for i in range(len(population)):
        if i in index:
            pass
        else:
            new_population.append(population[i])


    while len(index) > 0:
        mother = index.pop()
        father = index.pop()
        rand = np.random.randint(1, length)
        
        mother_gene = population[mother]
        father_gene = population[father]
        
        child1 = mother_gene[:rand] + father_gene[rand:]
        child2 = father_gene[:rand] + mother_gene[rand:]
        
        new_population.append(child1)
        new_population.append(child2)

    
    
    return new_population


def mutation(population, length, Pm=0.01):
    """
    变异操作
    """
    num = np.uint8(len(population) * Pm)
    index = random.sample(range(len(population)), num)
    
    for i in index:
        rand = np.random.randint(1, length)
        gene = list(population[i])
        if gene[rand] == '1':
            gene[rand] = '0'
        else:
            gene[rand] = '1'
        population[i] = ''.join(gene)
    
    return population


# 定义适应度函数
def fitness_func(x):
    y = objfun(x) + 200
    return y





    
    





    
    
    
    
    
    
    
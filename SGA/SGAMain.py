from SGA.SGAUI import SGAUI
import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from SGA.Figure_Canvas import Figure_Canvas
from SGA.SGA import *

class LogicalUI(QMainWindow, SGAUI):
    def __init__(self, parent=None):
        super(LogicalUI, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.start.clicked.connect(self.on_start_clicked)

    @pyqtSlot()
    def on_start_clicked(self):
        bounder = [0, 9]  # 自变量边界
        precision = 0.0001  # 精度
        pop_size = 200  # 种群数量
        max_iter = 1000  # 最大迭代次数

        length = bit_length(bounder, precision)  # 编码长度
        population = generate_pop(pop_size, length)  # 初始化种群

        max_fitness = []  # 每一轮最大适应度
        max_x = []  # 每一轮最大适应度对应的自变量
        mean_fitness = []

        for i in range(max_iter):
            decim_pop = [bin_decoder(bin_num, bounder, length) for bin_num in population]
            fitness_val = fitness_compute(decim_pop, fitness_func)
            population = select(population, fitness_val)
            population = crossover(population, length, Pc=0.8)
            population = mutation(population, length, Pm=0.1)

            mf = max(fitness_val)
            mean_f = np.mean(fitness_val)
            mean_fitness.append(mean_f)
            mx = population[fitness_val.index(mf)]

            mx = bin_decoder(mx, bounder, length)

            max_fitness.append(mf)
            max_x.append(mx)

            self.textBrowser.append('第%d轮迭代' % i)
            self.textBrowser.append('本轮最大适应度为：'+str(mf))
            self.textBrowser.append('本轮最大目标函数值为：'+str(objfun(mx)))
            self.textBrowser.append('本轮最大适应度对应的自变量为：'+str(mx))

        font1 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 23}

        fc = Figure_Canvas()
        fc.draw_pict(max_fitness, mean_fitness)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(fc)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()
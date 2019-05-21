import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=10, dpi=100):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)

    def draw_pict(self, df, train_target, target, predict):
        ax = self.fig.add_subplot(111)
        ax.scatter(df.index[2:37], train_target)
        ax.scatter(df.index[37:], np.array(target[35:]))
        ax.plot(df.index[2:], predict)

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster import hierarchy
import numpy as np

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=25, height=15, dpi=100):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)

    def draw_pict(self, Z, index):
        ax = self.fig.add_subplot(111)
        ax.set_xlim((0.4, 1.01))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示
        plt.rcParams['axes.unicode_minus'] = False  # 解决符号无法显示
        dn = hierarchy.dendrogram(np.array(Z), labels=index, orientation='right', ax=ax)
        plt.tick_params(labelsize=23)


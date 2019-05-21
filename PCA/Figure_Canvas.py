import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=6, dpi=100):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)
        #self.axes = self.fig.add_subplot(111)  # 调用figure下面的add_subplot方法

    def draw_pict(self, data):
        if data.shape[0] == 2:
            ax = self.fig.add_subplot(111)
            ax.scatter(data[0], data[1])
        else:
            ax = Axes3D(self.fig, rect=[0, 0, 1, 1], elev=30, azim=20)
            ax.scatter(data[0], data[1], data[2], marker='o', s=60)


import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=10, dpi=100):

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure
        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)

    def draw_pict(self, max_fitness, mean_fitness):
        ax = self.fig.add_subplot(111)
        ax.plot(max_fitness, label='max_fitness')
        ax.plot(mean_fitness, label='mean_fitness')

from FuzzyCluster.FCUI import FCUI
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from FuzzyCluster.Fuzzy_clustering import FuzzyClustering, compare
from FuzzyCluster.Figure_Canvas import Figure_Canvas

class LogicalUI(QMainWindow, FCUI):
    def __init__(self, parent=None):
        super(LogicalUI, self).__init__(parent)
        self.setupUi(self)
        self.start.clicked.connect(self.on_start_clicked)
        self.showMaximized()

    @pyqtSlot()
    def on_start_clicked(self):
        fc = FuzzyClustering(membership='euclid')
        try:
            path = self.lineEdit.text()  # 获取路径
            data = pd.read_csv(open(path, encoding='utf-8'))
            for column in list(data.columns[data.isnull().sum() > 0]):
                mean_val = data[column].mean()
                data[column].fillna(mean_val, inplace=True)

            index = data['区县'].tolist()
            del data['区县']
            df_norm = (data - data.min()) / (data.max() - data.min())

            cluster = fc.clustering(df_norm.values)

            keys = list(cluster.keys())
            keys.sort(reverse=True)

            Z = []

            news_cluster = dict([(ix, {ix}) for ix in range(0, 38)])
            new_keys = list(news_cluster.keys())
            for i in range(1, len(cluster)):
                c1 = cluster[keys[i]]
                c2 = cluster[keys[i - 1]]
                d = compare(c1, c2)
                max_d = d[[len(x) for x in d].index(max([len(x) for x in d]))]
                news_cluster[max(new_keys) + 1] = max_d
                new_keys.append(max(new_keys) + 1)
                del d[d.index(max_d)]
                if new_keys[list(news_cluster.values()).index(d[0])] < new_keys[list(news_cluster.values()).index(d[1])]:
                    Z.append([new_keys[list(news_cluster.values()).index(d[0])],
                              new_keys[list(news_cluster.values()).index(d[1])],
                              keys[37 - i], len(max_d)])
                else:
                    Z.append([new_keys[list(news_cluster.values()).index(d[1])],
                              new_keys[list(news_cluster.values()).index(d[0])],
                              keys[37 - i], len(max_d)])
            fc = Figure_Canvas()
            fc.draw_pict(Z, index)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(fc)
            self.graphicsView.setScene(graphicscene)
            self.graphicsView.show()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "路径有误", self.tr("请输入正确的路径！"))



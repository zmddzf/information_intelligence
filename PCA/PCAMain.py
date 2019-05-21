from PCA.PCAUI import PCAUI
import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PCA.Figure_Canvas import Figure_Canvas
from PCA.PCA import PCA, scale

class LogicalUI(QMainWindow, PCAUI):
    def __init__(self, parent=None):
        super(LogicalUI, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.start.clicked.connect(self.on_start_clicked)
        self.selectData.clicked.connect(self.on_selectData_clicked)
        self.selectNew.clicked.connect(self.on_selectNew_clicked)

    @pyqtSlot()
    def on_start_clicked(self):
        """
        运行PCA过程，并保存降维后数据文件
        :return: None
        """
        try:
            dataPath = self.dataPath.text()  # 获取数据集路径
            newPath = self.newPath.text()  # 获取降维后文件的路径
            ratio = float(self.ratio.text())  # 降维比例
            data = np.loadtxt(dataPath, skiprows=1).T  # 导入数据
            data_scaled = scale(data)  # Z-Score数据集
            pca = PCA(ratio=ratio)  # 实例化数据集对象
            pca.fit(data_scaled)  # 训练PCA
            vec = np.array(pca.eig_vec).T  # 获取变换矩阵A

            # 将变换矩阵A输出到表格控件中
            self.tableWidget.setRowCount(vec.shape[0])
            self.tableWidget.setColumnCount(vec.shape[1])
            for i in range(vec.shape[0]):
                for j in range(vec.shape[1]):
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(vec[i][j])))

            # 将PCA输出结果构建为html，展示到文字控件中
            s = ''
            for i in range((pca.cov.shape[0])):
                s += '<tr>'
                for j in range((pca.cov.shape[1])):
                    s += '<td>' + str(round(pca.cov[i][j], 3)) + '</td>'
                s += '</tr>'
            s = '<center><table border="1">' + s + '</table></center>'
            s = '<h3>协方差矩阵：</h3>' + s + '<h3>累计贡献率</h3>' + '<center>' +\
                str(np.around(pca.cumulative, decimals=4)) + '</center>'
            s = s + '<h3>特征根：</h3>' + '<center>' + str(np.around(pca.eig_val, decimals=4)) + '</center>'

            s1 = ''
            for i in range(pca.n_components.shape[0]):
                s1 += '<tr>'
                for j in range(pca.n_components.shape[1]):
                    s1 += '<td>' + str(round(pca.n_components[i][j], 3)) + '</td>'
                s1 += '</tr>'
            s1 = '<center><table border="1">' + s1 + '</table></center>'

            s = s + '<h3>主分量：</h3>' + s1
            self.cov.setText(s)

            tranform_data = pca.transform(data_scaled).T  # 对原始数据进行降维
            np.savetxt(newPath, tranform_data)  # 将降维数据保存

            fc = Figure_Canvas()
            fc.draw_pict(tranform_data.T)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(fc)
            self.pcaPict.setScene(graphicscene)
            self.pcaPict.show()

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "输入错误", self.tr("请输入正确的参数！"))  # 出现参数错误，弹出对话框提示

    @pyqtSlot()
    def on_selectData_clicked(self):
        """
        点击工具按钮，选择路径。
        :return: None
        """
        try:
            pth, _ = QFileDialog.getOpenFileName(self, '选择文件')
            print(pth)
            if pth:
                self.dataPath.setText(pth)
        except Exception as e:
            print(e)

    @pyqtSlot()
    def on_selectNew_clicked(self):
        """
        点击工具按钮，选择文件路径
        :return: None
        """
        try:
            pth, _ = QFileDialog.getOpenFileName(self, '选择文件')
            print(pth)
            if pth:
                self.newPath.setText(pth)
        except Exception as e:
            print(e)

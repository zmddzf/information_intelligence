# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pca_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pca_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.pca_btn.setFont(font)
        self.pca_btn.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"color:rgb(255,255,255)")
        self.pca_btn.setObjectName("pca_btn")
        self.verticalLayout_2.addWidget(self.pca_btn)
        self.fc_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.fc_btn.setFont(font)
        self.fc_btn.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"color:rgb(255,255,255)")
        self.fc_btn.setObjectName("fc_btn")
        self.verticalLayout_2.addWidget(self.fc_btn)
        self.sga_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.sga_btn.setFont(font)
        self.sga_btn.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"color:rgb(255,255,255)")
        self.sga_btn.setObjectName("sga_btn")
        self.verticalLayout_2.addWidget(self.sga_btn)
        self.pso_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.pso_btn.setFont(font)
        self.pso_btn.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"color:rgb(255,255,255)")
        self.pso_btn.setObjectName("pso_btn")
        self.verticalLayout_2.addWidget(self.pso_btn)
        self.ann_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.ann_btn.setFont(font)
        self.ann_btn.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"color:rgb(255,255,255)")
        self.ann_btn.setObjectName("ann_btn")
        self.verticalLayout_2.addWidget(self.ann_btn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "信息智能分析演示"))
        self.pca_btn.setText(_translate("MainWindow", "PCA"))
        self.fc_btn.setText(_translate("MainWindow", "模糊动态聚类"))
        self.sga_btn.setText(_translate("MainWindow", "遗传算法优化"))
        self.pso_btn.setText(_translate("MainWindow", "粒子群优化"))
        self.ann_btn.setText(_translate("MainWindow", "BP神经网络"))


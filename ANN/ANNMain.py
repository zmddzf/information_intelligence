from ANN.ANNUI import ANNUI
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from ANN.Figure_Canvas import Figure_Canvas
from ANN.ANN import *
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten

class LogicalUI(QMainWindow, ANNUI):
    def __init__(self, parent=None):
        super(LogicalUI, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.pushButton.clicked.connect(self.on_start_clicked)

    @pyqtSlot()
    def on_start_clicked(self):
        df = pd.read_excel('GDP_data.xlsx', index_col='Year')  # 读取数据
        df.GDP = (df.GDP - df.GDP.mean()) / df.GDP.std()  # 标准化

        data, target = data_format(df, 2)  # 格式化数据
        train_data = np.array(data[:35])  # 留出3个样本用于评估
        train_target = np.array(target[:35])

        model = Sequential()
        model.add(Dense(1, input_dim=2, init='uniform'))  # 输入层，Dense表示BP层
        model.add(Activation('linear'))  # 添加激活函数
        model.add(Dense(1, input_dim=1))  # 输出层
        model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
        model.summary()
        history = model.fit(train_data, train_target, nb_epoch=200, batch_size=10)
        loss_history = history.history['loss']
        loss_history = ['epoch {}:\nloss:{} '.format(ix, h) for ix, h in enumerate(loss_history)]
        loss_history = '\n'.join(loss_history)
        predict = model.predict(np.array(data))
        fc = Figure_Canvas()
        fc.draw_pict(df, train_target, target, predict)
        self.textBrowser.setText(loss_history)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(fc)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()
from PSO.PSOUI import PSOUI
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PSO.Figure_Canvas import Figure_Canvas
from PSO.PSO import *

class LogicalUI(QMainWindow, PSOUI):
    def __init__(self, parent=None):
        super(LogicalUI, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.start.clicked.connect(self.on_start_clicked)

    @pyqtSlot()
    def on_start_clicked(self):
        try:
            pso = PSO(0.7, 2, 2, 100, 1, [[0], [9]], 9, func)
            birds, best_fitness_hist, best_position_hist, s = pso.run(500)
            fc = Figure_Canvas()
            fc.draw_pict(best_fitness_hist)
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(fc)
            self.graphicsView.setScene(graphicscene)
            self.graphicsView.show()

            self.textBrowser.setText(s)
        except Exception as e:
            print(e)





from MainUI import MainUI
import sys
from PyQt5.QtWidgets import *
from PCA.PCAMain import LogicalUI as PCAL
from FuzzyCluster.FCMain import LogicalUI as FCL
from SGA.SGAMain import LogicalUI as SGA
from PSO.PSOMain import LogicalUI as PSO
from ANN.ANNMain import LogicalUI as ANN


class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

    def pca(self):
        self.dia1 = PCAL()
        self.dia1.show()

    def fc(self):
        self.dia2 = FCL()
        self.dia2.show()

    def sga(self):
        self.dia3 = SGA()
        self.dia3.show()

    def pso(self):
        try:
            self.dia4 = PSO()
            self.dia4.show()
        except Exception as e:
            print(e)

    def ann(self):
        try:
            self.dia5 = ANN()
            self.dia5.show()
        except Exception as e:
            print(e)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = Main()
    ui.pca_btn.clicked.connect(ui.pca)
    ui.fc_btn.clicked.connect(ui.fc)
    ui.sga_btn.clicked.connect(ui.sga)
    ui.pso_btn.clicked.connect(ui.pso)
    ui.ann_btn.clicked.connect(ui.ann)
    ui.show()

    sys.exit(app.exec_())
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow


# from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonrasst.clicked.connect(self.getResult)

    def getResult(self):
        try:
            n1 = self.ui.input_rasst1.text()
            n2 = int(self.ui.input_rasst2.text())
            s = int(n1, n2)
            self.ui.output_rasst2.setText(str(s))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from system import MyWin
from ui import Ui_MainWindow
import sqlite3


FILENAME_DB_VALUTES = 'bazad/valutess.db'


class NotFoundValute(Exception):
    pass


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CurrencyConv, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session = sqlite3.connect(FILENAME_DB_VALUTES)
        self.init_UI()

    def __del__(self):
        self.session.close()

    def getCurrentCource(self, valute):
        cur = self.session.cursor()
        try:
            result = cur.execute("""
                SELECT cources.value
                FROM cources
                INNER JOIN valutes
                    ON cources.valute = valutes.id
                WHERE valutes.title = ?
                ORDER BY cources.date DESC
                LIMIT 1            
            """, (valute,)).fetchone()
            return float(result[0])
        except BaseException as e:
            cur.close()
            raise NotFoundValute

    def init_UI(self):
        self.setWindowTitle('Перевод')
        self.ui.input_kursval1.setPlaceholderText('Из какой валюты:')
        self.ui.input_kursval2.setPlaceholderText('Ввод перевода:')
        self.ui.output_kursval1.setPlaceholderText('В какую валюту:')
        self.ui.output_kursval2.setPlaceholderText('Итог перевода:')
        self.ui.pushButtonkursval.clicked.connect(self.converter)

    def converter(self):
        try:
            input_currency = self.ui.input_kursval1.text().strip().upper()
            output_currency = self.ui.output_kursval1.text().strip().upper()
            input_cource = self.getCurrentCource(input_currency)
            output_cource = self.getCurrentCource(output_currency)

            input_amount = float(self.ui.input_kursval2.text().strip().replace(',', '.'))
            output_amount = round(input_amount * input_cource / output_cource, 2)
            self.ui.output_kursval2.setText(str(output_amount))
        except ValueError:
            self.ui.output_kursval2.setText("Не число")
        except NotFoundValute:
            self.ui.output_kursval2.setText("Неиз. валюта")


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Перевод')
        self.ui.input_rasst1.setPlaceholderText('Число')
        self.ui.input_rasst2.setPlaceholderText('Из системы счисления')
        self.ui.output_rasst2.setPlaceholderText('Итог перевода:')
        self.ui.pushButtonrasst.clicked.connect(self.getResult)

    def getResult(self):
        try:
            x = self.ui.input_rasst1.text()
            y = int(self.ui.input_rasst2.text())
            g = int(x, y)
            self.ui.output_rasst2.setText(str(g))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()


class UnionWindow(CurrencyConv, MyWin):
    def __init__(self, parent=None):
        super(UnionWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        CurrencyConv.init_UI(self)
        MyWin.init_UI(self)


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)


if __name__ == "__main__":
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook
    app = QtWidgets.QApplication(sys.argv)
    # application = CurrencyConv()
    # application.show()
    # myapp = MyWin()
    # myapp.show()
    window = UnionWindow()
    window.show()
    sys.exit(app.exec())

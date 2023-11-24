from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Programm')
        self.setGeometry(400, 300, 400, 300)

        self.new_text = QtWidgets.QLabel(self)


        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Это база.')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('Push me')
        self.btn.setStyleSheet('background: rgb(255, 0, 0);, color: rgb(255, 255, 255);')

        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('new Text')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()



def Application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Application()
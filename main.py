import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        a = randrange(5, 100)
        b = randrange(5, 100)
        qp.setBrush(QColor(255, 220, 51))
        qp.drawEllipse(50, 50, a, a)
        qp.setBrush(QColor(255, 220, 51))
        qp.drawEllipse(270, 70, b, b)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
from PyQt5.QtWidgets import QMainWindow,  QDesktopWidget, QApplication
import sys


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''initiates application UI'''

        self.statusbar = self.statusBar()
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        '''centers the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)


def main():
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

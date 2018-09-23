import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMainWindow, QAction, qApp
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from array import *
import random


class MainApplication(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        generateAct = QAction(QIcon('exit.png'), '&Generate', self)
        generateAct.setShortcut('Ctrl+R')
        generateAct.setStatusTip('Generate board')
        generateAct.triggered.connect(self.generate_board)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(generateAct)
        fileMenu.addAction(exitAct)

        self.browser = QWebEngineView()
        self.generate_board()
        self.browser.urlChanged.connect(self.generate_board)
        self.setCentralWidget(self.browser)
        
        self.setGeometry(300, 100, 800, 800)
        self.setWindowTitle('gh2 poison board practice by sgosiaco')    
        self.show()
    
    def generate_board(self):
        dawnglare = "http://pad.dawnglare.com/?height=6&width=7&patt="
        poison_pos = random.sample(range(0,42), 12)
        print(poison_pos)
        board = ''

        for orb in range(0, 42):
            if orb in poison_pos:
                board += 'P'
            else:
                board += 'G'
        #website = dawnglare+board
        self.browser.setUrl(QUrl(dawnglare+board))
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainApplication()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.mainui = MainUI(parent=self)
        self.setCentralWidget(self.mainui)
        
        bar = self.menuBar()
        
        file_menu = bar.addMenu('Widok')
        edit_menu = bar.addMenu('Edycja')
        help_menu = bar.addMenu('Pomoc')

        self.setWindowTitle('Kalkulator')
        self.setGeometry(300, 300, 250, 150)

class MainUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QtWidgets.QGridLayout(self)
        self.setLayout(grid)

        lcd = QtWidgets.QLCDNumber(self)
        lcd.setFixedHeight(60)
        button01 = QtWidgets.QPushButton('MC',self)
        button01.setFixedWidth(40)
        button01.setFixedHeight(40)
        button01.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button02 = QtWidgets.QPushButton('MR',self)
        button02.setFixedWidth(40)
        button02.setFixedHeight(40)
        button02.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button03 = QtWidgets.QPushButton('MS',self)
        button03.setFixedWidth(40)
        button03.setFixedHeight(40)
        button03.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button04 = QtWidgets.QPushButton('M+',self)
        button04.setFixedWidth(40)
        button04.setFixedHeight(40)
        button04.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button05 = QtWidgets.QPushButton('M-',self)
        button05.setFixedWidth(40)
        button05.setFixedHeight(40)
        button05.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)

        button11 = QtWidgets.QPushButton('<-',self)
        button11.setFixedWidth(40)
        button11.setFixedHeight(40)
        button11.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button12 = QtWidgets.QPushButton('CE',self)
        button12.setFixedWidth(40)
        button12.setFixedHeight(40)
        button12.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button13 = QtWidgets.QPushButton('C',self)
        button13.setFixedWidth(40)
        button13.setFixedHeight(40)
        button13.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button14 = QtWidgets.QPushButton('+-',self)
        button14.setFixedWidth(40)
        button14.setFixedHeight(40)
        button14.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button15 = QtWidgets.QPushButton('V',self)
        button15.setFixedWidth(40)
        button15.setFixedHeight(40)
        button15.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)

        button21 = QtWidgets.QPushButton('7',self)
        button21.setFixedWidth(40)
        button21.setFixedHeight(40)
        button21.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button22 = QtWidgets.QPushButton('8',self)
        button22.setFixedWidth(40)
        button22.setFixedHeight(40)
        button22.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button23 = QtWidgets.QPushButton('9',self)
        button23.setFixedWidth(40)
        button23.setFixedHeight(40)
        button23.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button24 = QtWidgets.QPushButton('/',self)
        button24.setFixedWidth(40)
        button24.setFixedHeight(40)
        button24.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button25 = QtWidgets.QPushButton('%',self)
        button25.setFixedWidth(40)
        button25.setFixedHeight(40)
        button25.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)

        button31 = QtWidgets.QPushButton('4',self)
        button31.setFixedWidth(40)
        button31.setFixedHeight(40)
        button31.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button32 = QtWidgets.QPushButton('5',self)
        button32.setFixedWidth(40)
        button32.setFixedHeight(40)
        button32.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button33 = QtWidgets.QPushButton('6',self)
        button33.setFixedWidth(40)
        button33.setFixedHeight(40)
        button33.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button34 = QtWidgets.QPushButton('*',self)
        button34.setFixedWidth(40)
        button34.setFixedHeight(40)
        button34.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button35 = QtWidgets.QPushButton('1/x',self)
        button35.setFixedWidth(40)
        button35.setFixedHeight(40)
        button35.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)

        button41 = QtWidgets.QPushButton('1',self)
        button41.setFixedWidth(40)
        button41.setFixedHeight(40)
        button41.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button42 = QtWidgets.QPushButton('2',self)
        button42.setFixedWidth(40)
        button42.setFixedHeight(40)
        button42.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button43 = QtWidgets.QPushButton('3',self)
        button43.setFixedWidth(40)
        button43.setFixedHeight(40)
        button43.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button44 = QtWidgets.QPushButton('-',self)
        button44.setFixedWidth(40)
        button44.setFixedHeight(40)
        button44.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button45 = QtWidgets.QPushButton('=',self)
        button45.setFixedWidth(40)
        button45.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)

        button51 = QtWidgets.QPushButton('0',self)
        button51.setFixedHeight(40)
        button51.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button52 = QtWidgets.QPushButton('.',self)
        button52.setFixedWidth(40)
        button52.setFixedHeight(40)
        button52.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        button53 = QtWidgets.QPushButton('+',self)
        button53.setFixedWidth(40)
        button53.setFixedHeight(40)
        button53.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)        
        
        grid.addWidget(lcd,0,0,1,5)
        grid.addWidget(button01,1,0)
        grid.addWidget(button02,1,1)
        grid.addWidget(button03,1,2)
        grid.addWidget(button04,1,3)
        grid.addWidget(button05,1,4)

        grid.addWidget(button11,2,0)
        grid.addWidget(button12,2,1)
        grid.addWidget(button13,2,2)
        grid.addWidget(button14,2,3)
        grid.addWidget(button15,2,4)
        
        grid.addWidget(button21,3,0)
        grid.addWidget(button22,3,1)
        grid.addWidget(button23,3,2)
        grid.addWidget(button24,3,3)
        grid.addWidget(button25,3,4)

        grid.addWidget(button31,4,0)
        grid.addWidget(button32,4,1)
        grid.addWidget(button33,4,2)
        grid.addWidget(button34,4,3)
        grid.addWidget(button35,4,4)

        grid.addWidget(button41,5,0)
        grid.addWidget(button42,5,1)
        grid.addWidget(button43,5,2)
        grid.addWidget(button44,5,3)
        grid.addWidget(button45,5,4,2,1)

        grid.addWidget(button51,6,0,1,2)
        grid.addWidget(button52,6,2)
        grid.addWidget(button53,6,3)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
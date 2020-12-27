import random
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class gameSinifi(QtWidgets.QWidget):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,150)
        self.setWindowTitle("Dice Roll")
        
        self.layout = QtWidgets.QGridLayout()
        
        self.spinBox = QtWidgets.QSpinBox()
        
        self.buttonBasla = QtWidgets.QPushButton('Start')
        self.buttonBasla.clicked.connect(self.start)
        
        self.buttonKapat = QtWidgets.QPushButton('Stop')
        self.buttonKapat.clicked.connect(self.close)
        
        
        self.label1 = QtWidgets.QLabel(" ")
        self.label1.setStyleSheet("Background-color:white")
        
        
        
        self.layout.addWidget(self.spinBox )
        self.layout.addWidget(self.buttonBasla)
        self.layout.addWidget(self.buttonKapat)
        self.layout.addWidget(self.label1)
        
        self.setLayout(self.layout)

    def start(self):
        
        zarDizisi = []
        for x in range(self.spinBox.value()):
            temp = random.randint(1, 6)
            zarDizisi.append(temp)  
        
        
        if len(zarDizisi) ==1:
            self.label1.setText(str(zarDizisi[0]))
            print(len(zarDizisi))
        if len(zarDizisi) ==2:
            self.label1.setText(str(zarDizisi[0])+" " +str(zarDizisi[1]))
        if len(zarDizisi) ==3:
            self.label1.setText(str(zarDizisi[0])+" " +str(zarDizisi[1])+" "+ str(zarDizisi[2]))
        if len(zarDizisi) >3:
            self.label1.setText("dice number : max 3, min 1")
        
                
     
      

  
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    uygulama = gameSinifi()
    uygulama.show()
    sys.exit(app.exec_())
    
    
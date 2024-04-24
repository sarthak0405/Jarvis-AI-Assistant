import sys
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from jarvis import Ui_mainGUI
import chat
import tkinter as tk
from tkinter import ttk
import os
class MainFile(QMainWindow):

    

    def __init__(self):
        super(MainFile, self).__init__()
        print("Main FILE")
        self.mainUI = Ui_mainGUI()
        self.mainUI.setupUi(self)

        def terminalPrint(self, text):
            self.mainUI.area.appendPlaintext(text)      



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainFile()
    ui.show()
    sys.exit(app.exec_())
    
    
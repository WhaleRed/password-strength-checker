from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog
import os

class Main(QMainWindow):
  def __init__(self):
    super().__init__()
    ui_path = os.path.join(os.path.dirname(__file__), 'main_window.ui')
    uic.loadUi(ui_path, self)

    #Load Dialog for results
    self.result = Results()
    self.calculateButton.setEnabled(False)

    #Calls allfilled if a line edit has new inputs
    self.passLineEdit.textChanged.connect(self.allFilled)
    self.gpsLineEdit.textChanged.connect(self.allFilled)

    #connect button
    self.calculateButton.clicked.connect(self.calculate)

  def allFilled(self):
    if (self.passLineEdit.text().strip() and self.gpsLineEdit.text().strip()):
      self.calculateButton.setEnabled(True)
    else:
      self.calculateButton.setEnabled(False)
  
  def calculate(self):
    print("calculating")
    

class Results(QDialog):
  def __init__(self):
    super().__init__()
    ui_path = os.path.join(os.path.dirname(__file__), 'results_dialog.ui')
    uic.loadUi(ui_path, self)
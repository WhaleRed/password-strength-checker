from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDialog
import os
from ..modules import calculations

class Main(QMainWindow):
  def __init__(self):
    super().__init__()
    ui_path = os.path.join(os.path.dirname(__file__), 'main_window.ui')
    uic.loadUi(ui_path, self)

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
    #Load Dialog for results
    self.result = Results(self.passLineEdit.text().strip(), self.gpsLineEdit.text().strip())
    self.result.show()
    

class Results(QDialog):
  def __init__(self, password, gps):
    super().__init__()
    ui_path = os.path.join(os.path.dirname(__file__), 'results_dialog.ui')
    uic.loadUi(ui_path, self)

    self.closeButton.clicked.connect(self.close)

    #Values
    self.combinations = calculations.possible_combinations(password)
    self.entropy = calculations.get_entropy(self.combinations)
    self.strength_value = self.strength(self.entropy)
    self.possible_passwords = calculations.possible_passwords(self.entropy)
    self.time = calculations.get_time(self.possible_passwords, gps)
    self.expected_time = calculations.get_expected_time(self.possible_passwords, gps)

    #Display values
    self.passResult.setText(str(self.strength_value))
    self.entropResult.setText(str(self.entropy))
    self.expectedResult.setText(str(self.expected_time))
    self.timeResult.setText(str(self.time))

  def strength(self, entropy):
    if entropy <= 35:
      return "Weak"
    elif entropy <= 59 and entropy >= 36:
      return "Average"
    elif entropy <= 119 and entropy >= 60:
      return "Strong"
    elif entropy >= 120:
      return "Very strong"
import sys
import constants
from permanentEmployee import PermanentEmployee
from temporalEmployee import TemporalEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class DismissEmployee(QDialog):
    staff = Staff()
    def __init__(self):
        super(DismissEmployee,self).__init__()
        loadUi("Forms\DismissEmployeeForm.ui",self)

        for job in constants.Contracts:
            self.comboBox.addItem(job)

        self.pushButton.clicked.connect(self.butClicked)

    def butClicked(self):
        if self.comboBox.currentIndex() == 0:
            employee = PermanentEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(0)
            ,str(0),str(0),str(0),str(0), str(0),str(0))
            self.staff.delete_permanent_employee(employee)
        elif self.comboBox.currentIndex() == 1:
            employee =TemporalEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(0),str(0),str(0),str(0))
            self.staff.delete_temporal__employee(employee)
        self.Name.setText("")
        self.Age.setValue(0)    


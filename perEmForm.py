import sys
import constants
from permanentEmployee import PermanentEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class PermanentEmployeeForm(QDialog):
    staff = Staff()
    def __init__(self):
        super(PermanentEmployeeForm,self).__init__()
        loadUi("Forms/permanentEmployeeForm.ui",self)

        #combox setup for occupation
        for job in constants.Occupations:
            self.comboBox.addItem(job)

        #the buttons
        self.HireEmployee.clicked.connect(self.HireEmployeePressed)
        self.UpdateEmployee.clicked.connect(self.UpdateEmployeePressed)    
        self.Marital_status.clicked.connect(self.MaritalStatusPressed)
        self.MuteEmployee.clicked.connect(self.mute_EmployeePressed)

        self.startDay.setMaximum(6)
        self.endDay.setMaximum(6)

        self.MonthBonus.setText("0")
        
        if not self.Marital_status.isChecked():
            self.Num_children.setVisible(False)
            self.MonthBonus.setVisible(False)
        else:
            self.Num_children.setVisible(True)
            self.MonthBonus.setVisible(True)         

    def MaritalStatusPressed(self):
        if not self.Marital_status.isChecked():
            self.Num_children.setVisible(False)
            self.MonthBonus.setVisible(False)
        else:
            self.Num_children.setVisible(True)
            self.MonthBonus.setVisible(True)

    def HireEmployeePressed(self):
        employee = PermanentEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.insert_permanent_employee(employee)

        self.Name.setText("")
        self.Age.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")
        self.comboBox.setCurrentIndex(0)

    def UpdateEmployeePressed(self):
        employee = PermanentEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.update_permanent_employee(employee)

        self.Name.setText("")
        self.Age.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")
        self.comboBox.setCurrentIndex(0)         

    def mute_EmployeePressed(self):
        employee = PermanentEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.mute_permanent_employee(employee) 

        self.Name.setText("")
        self.Age.setValue(0) 
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")
        self.comboBox.setCurrentIndex(0)        
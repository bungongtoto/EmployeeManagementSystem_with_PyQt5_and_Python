import sys
import constants
from temporalEmployee import TemporalEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication


class TemporalEmployeeForm(QDialog):
    staff = Staff()
    def __init__(self):
        super(TemporalEmployeeForm,self).__init__()
        loadUi("Forms/temporalEmployeeForm.ui",self)
        
        #Hire and update Button
        self.HireEmployee.clicked.connect(self.HireEmployeePressed)
        self.UpdateEmployee.clicked.connect(self.UpdateEmployeePressed)
        self.MuteEmployee.clicked.connect(self.mute_EmployeePressed)

        #combox setup for occupation
        for job in constants.Occupations:
            self.comboBox.addItem(job)

        self.startDay.setMaximum(6)
        self.endDay.setMaximum(6)    
    
    #def BackPressed(self):
        

    def HireEmployeePressed(self):
        employee = TemporalEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.insert_temporal_employee(employee) 

        self.Name.setText("")
        self.Age.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")
        self.comboBox.setCurrentIndex(0)



    def UpdateEmployeePressed(self):
        employee = TemporalEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.update_temporal_employee(employee)

        self.Name.setText("")
        self.Age.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")
        self.comboBox.setCurrentIndex(0)

    def mute_EmployeePressed(self):
        employee = TemporalEmployee(str(self.Name.toPlainText()),str(self.Age.value()),str(constants.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1])
        ,str(constants.Occupations[self.comboBox.currentIndex()]),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.mute_temporal_employee(employee) 

        self.Name.setText("")
        self.Age.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0)
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")
        self.comboBox.setCurrentIndex(0)
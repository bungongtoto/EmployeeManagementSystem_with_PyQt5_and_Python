import sys
import constants

from temEmForm import TemporalEmployeeForm 
from perEmForm import PermanentEmployeeForm
from DisEmplo import DismissEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("Forms\MainWindow.ui",self)

        self.PermTable.setColumnWidth(2,400)
        self.PermTable.setColumnWidth(5,100)
        self.TemTable.setColumnWidth(2,400)
        
        self.loadDataToTables()

        self.actionHire_Temporal_Employee.triggered.connect(self.actionHire_Temporal_EmployeePressed)
        self.actionHire_Permanent_Employee.triggered.connect(self.actionHire_Permanent_EmployeePressed) 
        self.actionDismiss_Employee.triggered.connect(self.actionDismiss_EmployeePressed) 
    
    def actionDismiss_EmployeePressed(self):
        window = DismissEmployee()
        window.setModal(True)
        window.exec()
        self.loadDataToTables()

    def actionHire_Temporal_EmployeePressed(self):
         window = TemporalEmployeeForm()
         window.setModal(True)
         window.exec() 
         self.loadDataToTables()
             
    def actionHire_Permanent_EmployeePressed(self):
        window = PermanentEmployeeForm()
        window.setModal(True)
        window.exec() 
        self.loadDataToTables()

    def loadDataToTables(self):
        self.PermTable.clearContents()
        self.TemTable.clearContents()
        connection = sqlite3.connect("database\staff.db")
        cur = connection.cursor()
        sqlquery1 = ("select * from PermanentEmployee limit 50")
        sqlquery2 = ("select * from TemporalEmployee limit 50")
        

        self.PermTable.setRowCount(50)
        self.TemTable.setRowCount(50)
        tableRow = 0
        tableRowt1 = 0

        for row in cur.execute(sqlquery1):
            self.PermTable.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.PermTable.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.PermTable.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.PermTable.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.PermTable.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.PermTable.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[5]))
            self.PermTable.setItem(tableRow,6,QtWidgets.QTableWidgetItem(row[6]))
            self.PermTable.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[7]))
            self.PermTable.setItem(tableRow,8,QtWidgets.QTableWidgetItem(row[8]))
            
            tableRow +=1

        for row in cur.execute(sqlquery2):
            self.TemTable.setItem(tableRowt1,0,QtWidgets.QTableWidgetItem(row[0]))
            self.TemTable.setItem(tableRowt1,1,QtWidgets.QTableWidgetItem(row[1]))
            self.TemTable.setItem(tableRowt1,2,QtWidgets.QTableWidgetItem(row[2]))
            self.TemTable.setItem(tableRowt1,3,QtWidgets.QTableWidgetItem(row[3]))
            self.TemTable.setItem(tableRowt1,4,QtWidgets.QTableWidgetItem(row[4]))
            self.TemTable.setItem(tableRowt1,5,QtWidgets.QTableWidgetItem(row[5]))
            
            tableRowt1 +=1
    
           
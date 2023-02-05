from employee import Employee
import constants

class PermanentEmployee(Employee):
    def __init__(self, name, age, workingDdays, occupation,number_of_worked_days,fixed_monthly_salary,num_children,marital_status,monthly_bonus) -> None:
        super().__init__(name, age, workingDdays, constants.Contracts[0] ,occupation)
        self.__number_of_worked_days = number_of_worked_days
        self.__fixed_monthly_salary = fixed_monthly_salary
        self.__num_children = num_children
        self.__marital_status = marital_status
        self.__monthly_bonus = monthly_bonus


    def get_num_of_worked_days(self):
        return self.__number_of_worked_days  
    def get_monthly_salary(self):
        return self.__fixed_monthly_salary
    def get_num_children(self):
        return self.__num_children
    def get_marital_status(self):
        return self.__marital_status
    def get_monthly_bonus(self):
        return self.__monthly_bonus
    def set_num_of_worked_days(self,toAdd):
        self.__number_of_worked_days = toAdd
    def set_monthly_salary(self,toAdd):
        self.__fixed_monthly_salary = toAdd   
    def set_num_children(self,toAdd):
        self.__num_children = toAdd  
    def set_marital_status(self,toAdd):
        self.__marital_status = toAdd  
    def set_monthly_bonus(self,toAdd):
        self.__monthly_bonus = toAdd         

import constants
from employee import Employee

class TemporalEmployee(Employee):
    def __init__(self, name, age, workingDdays, occupation,hourly_salary,number_of_worked_hours) -> None:
        super().__init__(name, age, workingDdays,constants.Contracts[1], occupation)
        self.__hourly_salary = hourly_salary
        self.__number_of_worked_hours = number_of_worked_hours

    def get_hourly_salary(self):
        return self.__hourly_salary
    def get_num_worked_hours(self):
        return self.__number_of_worked_hours    
    def set_hour_salary(self,toAdd):
        self.__hourly_salary = toAdd
    def set_num_worked_hours(self,toAdd):
        self.__number_of_worked_hours = toAdd    


        
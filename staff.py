import sqlite3
from permanentEmployee import PermanentEmployee
from temporalEmployee import TemporalEmployee
import constants

class Staff:
    conn = sqlite3.connect('database\staff.db')
    c = conn.cursor()
    def __init__(self) -> None:
        self.conn
    def insert_permanent_employee(self,employee:PermanentEmployee):
        self.c.execute("insert into PermanentEmployee values(?,?,?,?,?,?,?,?,?)",(employee.getName(),employee.getAge(),str(employee.getWorkingdays()),employee.getoccupation(),employee.get_num_of_worked_days(),employee.get_monthly_salary(),employee.get_num_children(),employee.get_marital_status(),employee.get_monthly_bonus()))
        self.conn.commit()
    def insert_temporal_employee(self,employee:TemporalEmployee):
        self.c.execute("insert into TemporalEmployee values(?,?,?,?,?,?)",(employee.getName(),employee.getAge(),str(employee.getWorkingdays()),employee.getoccupation(),employee.get_hourly_salary(),employee.get_num_worked_hours()))
        self.conn.commit()    
    def update_temporal_employee(self,employee:TemporalEmployee):
        with self.conn:
            self.c.execute("""update TemporalEmployee set age = :age , workingDdays = :workingDdays, occupation = :occupation,hourly_salary = :hourly_salary,number_of_worked_hours = :number_of_worked_hours
            where name = :name""",{'name': employee.getName(), 'age': employee.getAge(), 'workingDdays': str(employee.getWorkingdays()), 'occupation': employee.getoccupation(),'hourly_salary': employee.get_hourly_salary(),'number_of_worked_hours': employee.get_num_worked_hours()})
    def update_permanent_employee(self,employee:PermanentEmployee):
        with self.conn:
            self.c.execute("""update PermanentEmployee set age = :age , workingDdays = :workingDdays, occupation = :occupation,number_of_worked_days = :number_of_worked_days,fixed_monthly_salary = :fixed_monthly_salary,num_children = :num_children,marital_status = :marital_status,monthly_bonus = :monthly_bonus
            where name = :name""",{'name': employee.getName(), 'age': employee.getAge(), 'workingDdays': str(employee.getWorkingdays()), 'occupation': employee.getoccupation(),'number_of_worked_days':employee.get_num_of_worked_days(),'fixed_monthly_salary':employee.get_monthly_salary(),'num_children':employee.get_num_children(),'marital_status': employee.get_marital_status(),'monthly_bonus':employee.get_monthly_bonus()})
    def delete_permanent_employee(self,employee:PermanentEmployee):
        with self.conn:
            self.c.execute("""delete from PermanentEmployee 
            where name = :name and age = :age""",{'name': employee.getName(), 'age': employee.getAge()})
    def delete_temporal__employee(self,employee:TemporalEmployee):
        with self.conn:
            self.c.execute("""delete from  TemporalEmployee
            where name = :name and age = :age""",{'name': employee.getName(), 'age': employee.getAge()})
        
    def mute_permanent_employee(self,employee:PermanentEmployee):
        accumilator = int(employee.get_num_of_worked_days())*(float(employee.get_monthly_bonus())+ float(employee.get_monthly_salary()))/20
        hourlyPay = 2000
        numhoursW = accumilator/hourlyPay
        tempEmplo = TemporalEmployee(employee.getName(),employee.getAge(),employee.getWorkingdays(),employee.getoccupation(),str(hourlyPay),str(numhoursW))
        
        self.insert_temporal_employee(tempEmplo)
        self.delete_permanent_employee(employee)

    def mute_temporal_employee(self,employee:TemporalEmployee):
        MS = float(employee.get_hourly_salary())*int(employee.get_num_worked_hours()) 
        WDS = int(employee.get_num_worked_hours())/8
        pemEmplo = PermanentEmployee(employee.getName(),employee.getAge(),employee.getWorkingdays()
            ,employee.getoccupation(),str(WDS),str(MS),str(0), str("False"),str(0))

        self.insert_permanent_employee(pemEmplo)
        self.delete_temporal__employee(employee)    
# emplo = PermanentEmployee("kingsley",30,constants.chooce_working_days(),constants.chooce_occupation(),22,250000,1,True,4500)

#staff = Staff() 
# staff.update_permanent_employee(emplo)    
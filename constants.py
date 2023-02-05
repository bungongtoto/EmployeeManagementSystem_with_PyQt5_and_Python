DaysoftheWeek = ("Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
Contracts = ("Permanent", "Temporal")

Occupations = ("manager", "salesman", "accountant", "secretary")

def chooce_working_days()->tuple:
        count = 0
        for day in DaysoftheWeek:
            print(f"{count}.) {day} ")
            count += 1
        return DaysoftheWeek[int(input("Enter start day: ")): int(input("Enter end day number: "))+1]   
    
def chooce_contract_type():
        count = 0
        for contract_name in Contracts:
            print(f"{count}.) {contract_name} ")
            count += 1
        return Contracts[int(input("Enter contract number: "))] 
def chooce_occupation():
    count = 0
    for occupation in Occupations:
        print(f"{count}.) {occupation} ")
        count += 1
    return Occupations[int(input("Enter Occupation number: "))]  

PermanentTableHeaders = [ "Name", "Age", "Working Days", "Occupation","Days Worked","Monthly Salary","Number of Children","Marital Status","Monthly Bonus"]
def get_permanent_tableHeaderList()->list:
    return PermanentTableHeaders

import constants


class Employee:
    def __init__(self,name,age,workingDdays,contractType,occupation) -> None:
        self.__age = age
        self.__name = name
        self.__workingDays = workingDdays
        self.__contractType = contractType
        self.__occupation = occupation
        
    def getAge(self):
        return self.__age 
    def getName(self):
        return self.__name
    def getWorkingdays(self):
        return self.__workingDays
    def getContractType(self):
        return self.__contractType
    def getoccupation(self):
        return self.__occupation
    def setAge(self,age):
        self.__age = age 
    def setName(self,name):
        self.__name = name
    def setWorkingDays(self,workingDays):
        self.__workingDays = workingDays
    def setContractType(self,contractType):
        self.__contractType = contractType      
    def setOccupation(self, occupation):
        self.__occupation = occupation

    def __str__(self) -> str:
        return (f"name={self.__name}\nage={self.__age}\nworkingDays={self.__workingDays}\n contractType={self.__contractType}\noccupation={self.__occupation}  ")  
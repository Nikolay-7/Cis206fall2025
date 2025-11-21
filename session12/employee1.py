#class with variables
class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position
    
    #accessor functions
    def getName(self):
        return self.name
    
    def getIdNumber(self):
        return self.idNumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
    
    #mutator functions
    def setName(self, name):
        self.name = name
    
    def setIdNumber(self, idNumber):
        self.idNumber = idNumber
    
    def setDepartment(self, department):
        self.department = department
    
    def setPosition(self, position):
        self.position = position
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idNumber}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print()

#seperate test program
def main():
    #employee 1 
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    
    #employee 2
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    
    #employee 3
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    
    #display's all three employees
    print("Employee Information:")
    print("-" * 40)
    emp1.display()
    emp2.display()
    emp3.display()


if __name__ == "__main__":
    main()

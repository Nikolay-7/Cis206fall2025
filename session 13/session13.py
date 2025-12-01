#employee class
class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position
    
    def getName(self):
        return self.name
    
    def getIdNumber(self):
        return self.idNumber
    
    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position
    
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


#manager class inherits from employee class
class Manager(Employee):
    def __init__(self, name="", idNumber=0, department="", position="", salary=0.0):
        super().__init__(name, idNumber, department, position)
        self.salary = salary
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self, salary):
        self.salary = salary
    
    #new method that calculates annual bonus
    def calculateBonus(self):
        return self.salary * 0.10
    
    #overrides display method in employee class
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idNumber}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Annual Bonus: ${self.calculateBonus():,.2f}")
        print()


#demonstrates inherited class
def main():
    print("Base Employee Class:")
    print("")
    emp = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp.display()
    
    print("Inherited Manager Class:")
    print("")
    mgr = Manager("Robert Chen", 52001, "Sales", "Regional Manager", 85000.00)
    mgr.display()
    
    print("Bonus calculation display:")
    print(f"Bonus for {mgr.getName()}: ${mgr.calculateBonus():,.2f}")


if __name__ == "__main__":
    main()

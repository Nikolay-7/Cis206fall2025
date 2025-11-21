#class with variables
class Patient:
    def __init__(self, firstName, middleName, lastName, address, city, state, zipCode, phone, emergencyName, emergencyPhone):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.phone = phone
        self.emergencyName = emergencyName
        self.emergencyPhone = emergencyPhone
    
    #accessors functions
    def getFirstName(self):
        return self.firstName
    
    def getMiddleName(self):
        return self.middleName
    
    def getLastName(self):
        return self.lastName
    
    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZipCode(self):
        return self.zipCode
    
    def getPhone(self):
        return self.phone
    
    def getEmergencyName(self):
        return self.emergencyName
    
    def getEmergencyPhone(self):
        return self.emergencyPhone
    
    #mutator functions
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setMiddleName(self, middleName):
        self.middleName = middleName
    
    def setLastName(self, lastName):
        self.lastName = lastName
    
    def setAddress(self, address):
        self.address = address
    
    def setCity(self, city):
        self.city = city
    
    def setState(self, state):
        self.state = state
    
    def setZipCode(self, zipCode):
        self.zipCode = zipCode
    
    def setPhone(self, phone):
        self.phone = phone
    
    def setEmergencyName(self, emergencyName):
        self.emergencyName = emergencyName
    
    def setEmergencyPhone(self, emergencyPhone):
        self.emergencyPhone = emergencyPhone
    
    def display(self):
        print("Patient Information:")
        print(f"Name: {self.firstName} {self.middleName} {self.lastName}")
        print(f"Address: {self.address}, {self.city}, {self.state} {self.zipCode}")
        print(f"Phone: {self.phone}")
        print(f"Emergency Contact: {self.emergencyName}, {self.emergencyPhone}")
        print()

#class with variables
class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges
    
    #accessors functions
    def getName(self):
        return self.name
    
    def getDate(self):
        return self.date
    
    def getPractitioner(self):
        return self.practitioner
    
    def getCharges(self):
        return self.charges
    
    #mutator functions
    def setName(self, name):
        self.name = name
    
    def setDate(self, date):
        self.date = date
    
    def setPractitioner(self, practitioner):
        self.practitioner = practitioner
    
    def setCharges(self, charges):
        self.charges = charges
    
    def display(self):
        print(f"Procedure: {self.name}")
        print(f"Date: {self.date}")
        print(f"Practitioner: {self.practitioner}")
        print(f"Charges: ${self.charges:,.2f}")
        print()


#test program
def main():
    #patient data
    patient = Patient(
        "Marcus", 
        "T", 
        "Rivera", 
        "847 Oakwood Ave", 
        "Portland", 
        "OR", 
        "97204", 
        "503-782-4591", 
        "Elena Rivera", 
        "503-629-3847"
    )
    
    #all three procedures
    proc1 = Procedure("Physical Exam", "01/15/2024", "Dr. Johnson", 250.00)
    proc2 = Procedure("X-Ray", "01/15/2024", "Dr. Lee", 500.00)
    proc3 = Procedure("Blood Test", "01/15/2024", "Dr. Patel", 200.00)
    
    #display's patient info
    patient.display()
    
    #display's procedures info
    print("\nProcedures:\n")
    proc1.display()
    proc2.display()
    proc3.display()
    
    #calculates and display's total charges for procedures
    total = proc1.getCharges() + proc2.getCharges() + proc3.getCharges()
    print(f"Total Charges: ${total:,.2f}")


if __name__ == "__main__":
    main()

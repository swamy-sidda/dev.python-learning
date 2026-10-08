class Person:
    def __init__(self,name="NONE",age=18,address="madanapalli",father="NONE",mother="NONE"):
        self.name=name
        self.age=age
        self.address=address
        self.father=father
        self.mother=mother
    def printPerson(self):
        print(f"Person name : {self.name}")
        print(f"Person age : {self.age}")
        print(f"Person address : {self.address}")
        print(f"Person father : {self.father}")
        print(f"Person mother : {self.mother}")
    def printPerson2(self,name,age,address,father,mother):
        self.name=name
        self.age=age
        self.address=address
        self.father=father
        self.mother=mother


person = Person("Kumar", 22, "Madanapalli", "Munuswamy", "Mogilamma")
person.printPerson()

print("----------------------------------------------------------------------")

person1= Person()
person1.printPerson2("swamy",22,"Madanapalli","Munuswamy","Mogilamma")
person1.printPerson()
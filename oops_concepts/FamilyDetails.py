class FamilyDetails:
    def __init__(self, name="", age="", status="", father="", mother=""):
        self.name = name
        self.age = age
        self.status = status
        self.father = father
        self.mother = mother
    def printFamilyDetails(self):
        return f"name : {self.name}, age : {self.age}, status : {self.status}, father : {self.father}, mother : {self.mother}"

    def getFamilyDetails(self, name="", age="", status="", father="", mother=""):
        self.name = name
        self.age = age
        self.status = status
        self.father = father
class StudentInfo:
    def __init__(self,name="",age=0,school="ChildrenTree",stan=0):
        self.name = name
        self.age = age
        self.school = school
        self.stan = stan
    def getStudentInfo(self,name,age,stan):
        self.name = name
        self.age = age
        self.stan = stan
    def printStudentInfo(self):
        print(f"{self.name} is {self.age} years old. He is studying {self.stan} in {self.school}.")


student1 = StudentInfo()
student1.getStudentInfo("Kumarswamy",22,"MCA")
student1.printStudentInfo()

student2=StudentInfo(name="Swamy",age=21,stan=7)
student2.printStudentInfo()
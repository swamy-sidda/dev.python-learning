class Pet():
    def __init__(self, num):
        self.num = num
    def patternExample(self):
        for i in range(1,self.num+1):
            print("* "*i,end=" \n")

obj = Pet(5)
obj.patternExample()
obj=Pet(6)
obj.patternExample()

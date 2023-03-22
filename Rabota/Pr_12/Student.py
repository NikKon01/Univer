class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("GroupNumber: ", self.groupNumber)

nikolay = Student("Nikolay", 19, "11B")
nikolay.showInfo()
print(" --------------- ")

george = Student("George", 18, "11A")
george.showInfo()
print(" --------------- ")

alexey = Student("Alexey", 17, "10B")
alexey.showInfo()
print(" --------------- ")

ilya = Student("Ilya", 17, "10A")
ilya.showInfo()
print(" --------------- ")

kirill = Student("Kirill", 18, "10B")
kirill.showInfo()



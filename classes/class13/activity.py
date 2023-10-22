class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print(self):
        return f"Name: {self.name}, Grade: {self.grade}"
    
    def result(self):
        if self.grade < 5:
            return "You have failed"
        else:
            return "You have passed"


student1 = Student("Diego", 3)
student2 = Student("Cynthia", 9)

print(student1.print())
print(student1.result())
print("==============================")
print(student2.print())
print(student2.result())



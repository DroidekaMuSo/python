class Salary:
    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Salary: ${self.salary}"


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.salary = Salary(1200)

    def __str__(self):
        return f'Name: {self.name}, Position: {self.position}, Salary:{self.salary.__str__()}'


salary1 = Salary(200)
employee1 = Employee("Nico", "Teacher")

print(f"Result 1: {salary1.__str__()}")
print(f"Result 2: {employee1.__str__()}")
##############################################################################################
# Object Oriented Programing in Python
##############################################################################################

print('\n\nObject Oriented Programing in Python')

class Child:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avarage(self):
        return sum(self.grades) / len(self.grades)

student_one = Child('Ganesh', [10,45,78,10,14])

student_two = Child('Harshu', [10,74,56,95])

print(f'\nStudent One Avarage {student_one.avarage()}')
print(f'Student Two Avarage {student_two.avarage()}')

student_two = student_one

print(f'Student Two Avarage {student_two.avarage()}')


class Mark:
    marks = []
    numberOfSub = 1
    name = 'My Marks'
    def percentage(self):
        return sum(self.marks) / self.numberOfSub
    

name = 'Global Name'

markes = Mark()

markes.marks = [100,99,99,99,99,99]
markes.numberOfSub = len(markes.marks)

print(f'Mark Percentage: {markes.percentage()}')

print(f'Mark Percentage: {Mark.percentage(markes)}')


print(f'Mark Variable: {markes.name}')

print(f'Global Variable: {name}')


##############################################################################################
# Magic Methods in Python
##############################################################################################


print('\n\nMagic Methods in Python')

class Garage:
    cars = ['Focus']

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f'Garage {self.cars}'
        
    def __str__(self):
        return f'Garage with {len(self.cars)} cars'


ford = Garage()
ford.cars.append('Toyata')

print(f'\nCars in Garage: {ford.cars}')

print(f'Number of cars in Garage: { len(ford)}')

print(f'0th Car in Garage: {ford[0]}')

print('Print Cars using for loop')
for car in ford:
    print(car)


print(f'Printing Object: {ford}')


##############################################################################################
#Inheritance in Paython
##############################################################################################

print(f'\n\nInheritance in Paython')

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avarage(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    @property
    def weeklySalary(self):
        return self.salary * 37.5


ganesh = WorkingStudent('Ganesh','DYP',50.00)

print(f'\nWorking Student Salary: {ganesh.salary}')

ganesh.marks.append(45)
ganesh.marks.append(75)
ganesh.marks.append(41)
ganesh.marks.append(49)

print(f'Print Working Student Avarage: {ganesh.avarage()}')

print(f'Print Weekly Salary: {ganesh.weeklySalary}')

# student = Student('Harshu', 'Test')

# print(f'Printing Students Salary: {student.salary}: ') # 'Student' object has no attribute 'salary'


##############################################################################################
# Class Method and Static Method
##############################################################################################

print('\n\nClass Method and Static Method')

class Foo:
    @classmethod
    def hi(cls):
        print(f'\n{cls.__name__}')
    
my_object = Foo()

my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take arguments')

my_bar = Bar()

my_bar.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.45, 0.789)

print(f'FixedFloat Number: {new_number}')

class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'
    
    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'

dollar = Dollar(125.11)

dollar2 = Dollar.from_sum(124.5,124.2)

print(f'Print Dollar {dollar}')

print(f'Print Dollar Two: {dollar2}')



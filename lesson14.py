class Person:
    first_name = ''
    last_name = ''
    age = 18
    gender = 'male'

class Patient(Person):
    pass

class Driver(Emplyer):
    position = 'driver'
    license = ''


class Student(Person):
    student = {
        'first_name': 'Vasya',
        'last_name': 'Ivanov'
    }

class Emplyer(Person):
    salary = 100
    emergency_contact = '911'
    position = ''
    unit = 


class ShopClient(Person):
    pass

class Unit:

    def __init__(self, name):
        self.name = name
        self.emplyers = []



person = Person()
student = Student()
student.first_name

unit = Unit('Delivery')
emp = Emplyer(*args)
unit.emplyers.append(emp)
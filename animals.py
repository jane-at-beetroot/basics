class Animal:

    paws = 4
    tail = True
    ears = 2

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
   
    def voice(self):
        print('Bzzzzzzzzz!!!')


class Cat(Animal):

    def __eq__(self, other):
        return self.name == other.name

    @staticmethod
    def voice():
        print('MEOW!!!!!!!')


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    @staticmethod
    def voice():
        print('FFFFF!!!')


class Dog(Animal):

    weight = 0
    TOTAL_COUNT = 0

    def __init__(self, name='Tuzik', weight=10):
        super().__init__(name)
        self.weight = weight
        Dog.TOTAL_COUNT += 1

    def __eq__(self, other):
        if hasattr(other, 'weight'):
            return self.weight == other.weight
        else:
            return NotImplemented

    def __lt__(self, other):
        return self.weight < other.weight

    def voice(self):
        print('Bark! My name is {}'.format(self.name)) 

    @classmethod
    def get_total_count(cls):
        return cls.TOTAL_COUNT

    @classmethod
    def from_dict(cls, dict_data):
        obj = cls()  
        for key in dict_data:
            setattr(obj, key, dict_data[key])
        return obj

class CatDog(Dog, Cat):

    def voice(self):
        print('Meow! Bark!')


if __name__ == '__main__':
    dog1 = Dog()
#    print(dog1)
#    print(dog1.weight)
    dog_data = {'name': 'Joy', 'weight': 15}
    dog2 = Dog.from_dict(dog_data)
    print(dog2)
    print(dog2.weight)
#    cat = Cat('Murzik')
#    print(dog1 == cat)
#    print(cat == dog1)




















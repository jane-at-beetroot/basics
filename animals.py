class Animal:

    paws = 4
    _tail = True
    ears = 2

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
   
    def voice(self):
        print('Bzzzzzzzzz!!!')

    @property
    def tail(self):
        if self._tail:
            return 'This animal has tail'
        else:
            return 'This animal has no tail'
    
    @tail.setter
    def tail(self, tail):
        if type(tail) is bool:
            self._tail = tail
        if tail == 'Yes':
            self._tail = True
        elif tail == 'No':
            self._tail = False


class Cat(Animal):

    def __eq__(self, other):
        print('CAT EQ')
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

    TOTAL_COUNT = 0

    def __init__(self, name='Tuzik', weight=10):
        super().__init__(name)
        self.weight = abs(weight)
        Dog.TOTAL_COUNT += 1

    def __eq__(self, other):
        print('Dog EQ')
        if hasattr(other, 'weight'):
            return self.weight == other.weight
        else:
            print('Right operand has no weight')
            return NotImplemented

    def __lt__(self, other):
        if hasattr(other, 'weight'):
            return self.weight < other.weight
        else:
            return False

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

    def set_weight(self, weight):
        self._weight = abs(weight)

    def get_weight(self):
        return self._weight
        return '{} kg'.format(self._weight)

    weight = property(get_weight, set_weight)
    
class CatDog(Dog, Cat):

    def voice(self):
        print('Meow! Bark!')


if __name__ == '__main__':
#    dog1 = Dog('Murzik', -20)
#    print(dog1)
#    print(dog1.weight)
#    dog1.weight = -20
#    print(dog1.weight)
    bug = Animal('Bug')
    bug.tail = 'No'
    print(bug.tail)
#    dog_data = {'name': 'Joy', 'weight': 15}
#    dog2 = Dog.from_dict(dog_data)
#    print(dog2)
#    print(dog2.weight)
#    cat = Cat('Murzik')
#    print(dog1 < cat)
#    print(cat < dog1)




















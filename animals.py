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

    @staticmethod
    def voice():
        print('MEOW!!!!!!!')


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Dog(Animal):

    def voice(self):
        print('Bark! My name is {}'.format(self.name))    


class CatDog(Dog, Cat):

    def voice(self):
        print('Meow! Bark!')

print(dir(Cat))
kitty = Kitten('Kitty', '1 month')
kitty.voice()
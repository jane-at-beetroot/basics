class IterTen:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.limit:
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration

def my_first_generator():
    n = 0
    while n < 5:
        print('Generator invokation')
        n += 1
        yield n
        print('After yield')
    return 10

def my_second_generator():
    yield from [1, 2, 3, 4]
'''
gen = my_first_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''
for i in my_second_generator():
    print(i)

'''
it = IterTen(15)
my_iterator = iter(it)

for num in my_iterator:
    print(num)
'''
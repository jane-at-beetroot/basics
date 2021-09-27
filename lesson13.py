a = 1

def outer_func():
    a = 10
    def inner_func():
        print(a)
    return inner_func

def just_print(s):
    print(s)

def just_split(s):
    print(s.split(' '))

def wrap_func(func, s):
    if type(s) is str:
        print(func.__name__)
        func(s)
    else:
        s = str(s)
        print(func.__name__)
        func(s)

wrap_func(just_print, 6.7)
wrap_func(just_split, 6.7)

#print(a)
#f = outer_func()
#print(f)
#f()
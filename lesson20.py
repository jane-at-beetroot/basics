number = 10
n: int = 1


def say_hello(name: str):
    print('Hello {}'.format(name))

def say_len(sequence: str) -> int:
    print(len(sequence))
    return len(sequence)

'''
say_hello('World')
say_hello(30)
say_hello([1, 2, 3])
'''
say_len('World')
say_len([1, 2, 3])
say_len(30)
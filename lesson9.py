a = 1

def multiply(a, n):
    if type(n) is not int:
        return
    def multiply_by_n():
        print(a)
        print(n)
        return a*n
    return multiply_by_n()

b = 2

#print(__name__)

if __name__ == '__main__':
    print(multiply(b, 3))
    print(a)

    print(type(multiply))
    #print(type(multiply_by_n))
my_test_string = 'Hello!!!'

def sum_two_numbers(*args, **kwargs):
    '''Sums two ineger numbers'''

    print(args)
    print(kwargs.get('c'))
#    my_test_string = 'World'
#    print(my_test_string)
#    if type(a) is not int: #What's going here?!!!
#        return
#    if type(b) is not int:
#        return
#    result = a + b + sum(args)
    result = sum(args)
    return  result

#print('Bla-bla-bla!')
#TODO aplly normal fix

def print_hello_string(hello_sting):
    print(hello_sting)

print_hello_string(my_test_string)
print(sum_two_numbers(4, 4, 5, a=7, b=6, c=3))
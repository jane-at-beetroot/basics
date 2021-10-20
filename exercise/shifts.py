def linear_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    pass


def circular_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [4, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [3, 4, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [2, 3, 4, 1]
    '''
    pass


def nested_parentheses(incoming: str) -> bool:
    '''
    Функція отримує рядок, який складається тільки зі знаків "(" або ")"
    Рядок вважається таким, що містить коректно вкладені скобки, якщо для
    кожної скобки "(" існує відповідна ")". 
    Функція повертає булевську змінну, яка показує, чи містить вхідний рядок
    тільки правильно вкладені скобки - True, чи ні - False

    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
    '''
    pass


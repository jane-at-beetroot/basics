from math import pi as p

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1 = []


def transpose(initial):
    transposed = []

    for row in range(3):
        transposed.append([])
        for column in range(3):
            transposed[row].append(None)

    for row in range(3):
        for column in range(3):
            transposed[column][row] = initial[row][column]

    return transposed

transposed_matrix = transpose(matrix)

def circle(rad):
    return p*pow(rad, 2)

def circles_from_list(rads_list, return_type='dict'):
    if type(rads_list) is not list:
        return
    if return_type.lower() == 'dict':
        return {r:circle(r) for r in rads_list}
    else:
        return [circle(r) for r in rads_list]

rads1 = [1, 3, 5]
rads2 = [2, 4, 6, 8]

print(circles_from_list(rads1))

old_list = [1, 2, 3, 4]
new_list = [x for x in old_list]

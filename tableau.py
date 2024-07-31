#AUX Functions
from copy import deepcopy


def argmin(array):
    min_elem = min(array)
    return array.index(min_elem)

def transpose(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

def generate_identity_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for row in range(n):
        matrix[row][row] = 1
    
    return matrix

def sum_lists(a, b):
    return [sum(x) for x in zip(a,b)]

#Tableau Functions
def create_tableau(A, b, c):
    tableau = deepcopy(A)
    b = deepcopy(b)
    c = deepcopy(c)

    for i in range(len(tableau)):
        tableau[i].append(-b[i])

    identity_matrix = generate_identity_matrix(len(c) + 1)
    tableau.extend(identity_matrix)


    tableau.append(c + [0])
    tableau = transpose(tableau)


    return tableau


# def create_tableau2(A, b, c):
#     tableau = A
#
#     for i in range(len(tableau)):
#         tableau[i].append(-b[i])
#
#     # identity_matrix = generate_identity_matrix(len(c) + 1)
#     # tableau.extend(identity_matrix)
#     tableau = transpose(tableau)
#     for row in range(len(tableau)):
#         for col in range(len(tableau[row])):
#             if row == col:
#                 tableau[row].append(1)
#             else:
#                 tableau[row].append(0)
#         if row < len(c):
#             tableau[row].append(c[row])
#     tableau[-1].append(0)
#
#     return tableau
#

def tableau_has_finished(tableau):
    for elem in tableau[-1]:
        if elem < 0:
            return False
    return True

def get_next_tableau_part1(tableau):
    col = argmin(tableau[-1])
    
    ratios = []
    for row in range(len(tableau) - 1):
        if tableau[row][col] > 0:
            ratios.append(tableau[row][-1] / tableau[row][col])
        else:
            ratios.append(float('inf'))  
    
    # Todo
    if all(ratio == float('inf') for ratio in ratios):
        raise Exception("Problem is unbounded.")
    

    #encontrando a linha do pivo
    pivot_index = (argmin(ratios), col)
    return pivot_index

def get_next_tableau_part2(tableau, pivot_index):

    #normalizar a linha do pivo
    pivot_elem = tableau[pivot_index[0]][pivot_index[1]]
    tableau[pivot_index[0]]= [x/pivot_elem for x in tableau[pivot_index[0]]]

    for row in range(len(tableau)):
        if row == pivot_index[0]:
            continue
        current_row = tableau[row]
        coefficient = tableau[row][pivot_index[1]]
        pivot_row_multiplied = [x*-coefficient for x in tableau[pivot_index[0]]]

        new_row = sum_lists(current_row, pivot_row_multiplied)
        tableau[row] = new_row
    return tableau


c = [12, 32, 16, 11, 2, 9, 7, 20, 8, 7, 69, 14, 182, 12, 29, 75, 0.6, 6, 34, 9]

A = [
    [134.2, 77.5, 84.18, 115.28, 2.7, 30.24, 360, 491.4, 80, 110.16, 181.9, 330, 73, 13, 364.5, 141, 288, 296.8, 117, 150.2],
    [8.784, 3.75, 0.414, 1.572, 0.18, 0.648, 7.2, 15.68, 42, 34.56, 20.4, 16.8, 5.7, 0.17, 27.45, 29.25, 16.16, 16.4, 0, 0.2],
    [390.4, 137.5, 8.28, 60.26, 6, 25.2, 9, 33.60, 8, 10.24, 7, 10, 27, 0, 15, 40.5, 380, 120, 0, 3.8],
    [0, 0, 3.174, 5.633, 0.105, 1.296, 0.3, 0.56, 1.9, 0.32, 0, 0, 0, 0, 0, 0, 5.6, 3.2, 0, 0],
    [2.44, 1.25, 8.28, 78.6, 1.8, 4.32, 0, 0, 16, 0, 0, 1, 0, 0, 3, 0, 2.4, 1.6, 0, 0],
    [0.732, 0.125, 0.552, 0.9825, 0.24, 0.576, 1.4, 2.52, 0.9, 0.576, 1.59, 2.5, 1.25, 0.135, 2.7, 1.2, 9.52, 5.6, 0, 0.4],
    [5.856, 4.25, 0.414, 0.262, 0.03, 0.252, 0.6, 0.924, 0.1, 0.576, 11.05, 27.1, 13.55, 0, 21.75, 2.55, 1.12, 3.84, 2.6, 16.8],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1]
]
b = [2000, 60, 800, 35, 80, 14.4, 70, 2, -3, 3, -5, 3, -5, 4,-11, 1.5, -4.5, 1, -2, 1, -2]


tableau = create_tableau(A, b, c)
# tableau = create_tableau2(A, b, c)

while not tableau_has_finished(tableau):
    pivot_index = get_next_tableau_part1(tableau)
    get_next_tableau_part2(tableau, pivot_index)

for i,x in enumerate(tableau[-1][21:]):
    print(f"x{i}: {x}")

    
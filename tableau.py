#AUX Functions
from copy import deepcopy
import auxiliar as aux
import data

#Tableau Functions
def create_tableau(A, b, c):
    tableau = deepcopy(A)
    b = deepcopy(b)
    c = deepcopy(c)

    for i in range(len(tableau)):
        tableau[i].append(-b[i])

    identity_matrix = aux.generate_identity_matrix(len(c) + 1)
    tableau.extend(identity_matrix)


    tableau.append(c + [0])
    tableau = aux.transpose(tableau)


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
    col = aux.argmin(tableau[-1])
    
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
    pivot_index = (aux.argmin(ratios), col)
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

        new_row = aux.sum_lists(current_row, pivot_row_multiplied)
        tableau[row] = new_row
    return tableau

tableau = create_tableau(data.A, data.b, data.c)
# tableau = create_tableau2(A, b, c)

while not tableau_has_finished(tableau):
    pivot_index = get_next_tableau_part1(tableau)
    get_next_tableau_part2(tableau, pivot_index)

for i,x in enumerate(tableau[-1][21:]):
    print(f"x{i}: {x}")

    
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
#         for pivot_col in range(len(tableau[row])):
#             if row == pivot_col:
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

def get_next_tableau(tableau):
    pivot_col = aux.argmin(tableau[-1])
    
    ratios = []
    for row in range(len(tableau) - 1):
        if tableau[row][pivot_col] > 0:
            ratios.append(tableau[row][-1] / tableau[row][pivot_col])
        else:
            ratios.append(float('inf'))  
    
    # Todo
    if all(ratio == float('inf') for ratio in ratios):
        raise Exception("Problem is unbounded.")
    

    #encontrando a linha do pivo
    pivot_row = aux.argmin(ratios)

    #normalizar a linha do pivo
    pivot_elem = tableau[pivot_row][pivot_col]
    tableau[pivot_row]= [x/pivot_elem for x in tableau[pivot_row]]

    for row in range(len(tableau)):
        if row == pivot_row:
            continue
        current_row = tableau[row]
        coefficient = tableau[row][pivot_col]
        pivot_row_multiplied = [x*-coefficient for x in tableau[pivot_row]]

        new_row = aux.sum_lists(current_row, pivot_row_multiplied)
        tableau[row] = new_row
        
    return ratios, pivot_col, pivot_row


def solve_simplex(tableau):
    headers = [f'y{i}' for i in range(len(data.b))]
    headers.extend([f'x{i}' for i in range(len(data.c))])
    headers.extend(['P', 'Solution', 'TR'])
    
    basis = [f'x{i}' for i in range(len(data.c))]
    basis.append('P')
    
    tableau_copy = deepcopy(tableau)
    tableaus_data = [
        {'tableau': tableau_copy, 'headers': headers, 'basis': basis, 'tr': None}
    ]

    tableau_copy = deepcopy(tableau)
    tableaus_data.append({'tableau': tableau_copy, 'headers': headers, 'basis': basis, 'tr': None})

    while not tableau_has_finished(tableau):
        ratios, pivot_header, pivot_basis = get_next_tableau(tableau)
        tableau_copy = deepcopy(tableau)
        basis_copy = basis[:]
        basis_copy[pivot_basis] = headers[pivot_header]
        tableaus_data[-1].update({
            'pivot_header': pivot_header, 'pivot_basis': pivot_basis, 'tr': ratios
        })
        tableaus_data.append({'tableau': tableau_copy, 'headers': headers, 'basis': basis_copy, 'tr': None})

        
    return tableaus_data


tableau = create_tableau(data.A, data.b, data.c)
tableaus_data = solve_simplex(tableau)

last_tableau = tableaus_data[-1]["tableau"]
portions = last_tableau[-1][len(data.b): len(data.b)+len(data.c)]
tableau_summary = {
    'cost': f'R$ {last_tableau[-1][-1] / 100:.2f}'.replace('.',','),
    'foods': {data.food_names[i]: round(portions[i]*data.food_portions[i]) for i in range(len(data.food_names))}
}

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
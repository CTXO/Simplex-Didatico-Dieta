from typing import List
import numpy as np
from scipy.optimize import linprog

foods :List[str] = [
    "Leite magro",
    "Iogurte",
    "Maçãs",
    "Laranjas",
    "Alface",
    "Cenoura",
    "Arroz",
    "Esparguete",
    "Batata",
    "Pão",
    "Atum (enlatado)",
    "Salsichas (enlatado)",
    "Ovos",
    "Fiambre",
    "Frango",
    "Pescada",
    "Feijão",
    "Grão de Bico",
    "Azeite",
    "Manteiga"
]

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
c = np.array([12, 32, 16, 11, 2, 9, 7, 20, 8, 7, 69, 14, 182, 12, 29, 75, 0.6, 6, 34, 9])

A = np.array([
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
]) * -1
b = np.array([2000, 60, 800, 35, 80, 14.4 , 70, 2, -3, 3, -5, 3, -5, 4,-11, 1.5, -4.5, 1, -2, 1, -2]) * -1


result = linprog(c, A_ub=A, b_ub=b, method='highs')

print("Optimal value:", result.fun)
print("Optimal solution:", result.x)
# print("Optimal solution len:", len(result.x))

# print("Success:", result.success)
# print("Status:", result.status)

x = np.array(result.x)

c_a = c[:, None].T
# x_a = x[:, None]
# print(c_a.shape)
# print(x_a.shape)
# f = c_a @ x_a
# print(f)

# sum = 0
# for k in range(21):
#     for i in range(len(result.x)):
#         sum+= result.x[i] * A[k][i]
#     print(f"sum {sum*-1} limit: {b[k]*-1}")
#     sum =0
    
# print(sum)


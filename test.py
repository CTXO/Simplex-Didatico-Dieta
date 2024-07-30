from scipy.optimize import linprog

# Coefficients of the objective function (to minimize)
c = [12, 32, 16, 11, 2, 9, 7, 20, 8, 7, 69, 14, 182, 12, 29, 75, 0.6, 6, 34, 9]

# Coefficients of the inequality constraints (Ax <= b)
A_ub = [
    [-134.2, -77.5, -84.18, -115.28, -2.7, -30.24, -360, -491.4, -80, -100.16, -181.9, -330, -73, -13, -364.5, -141, -288, -296.8, -117, -150.2],
    [-8.784, -3.75, -0.414, -1.572, -0.18, -0.648, -7.2, -15.68, -42, -34.56, -20.4, -16.8, -5.7, -0.17, -27.45, -29.25, -16.16, -16.4, 0, -0.2],
    [-390.4, -137.5, -8.28, -60.26, -6, -25.2, -9, -33.60, -8, -10.24, -7, -10, -27, 0, -15, -40.5, -380, -120, 0, -3.8],
    [0, 0, -3.174, -5.633, -0.105, -1.296, -0.3, -0.56, -1.9, -0.32, 0, 0, 0, 0, 0, -5.6, -3.2, 0, 0, 0],
    [2.44, 1.25, 8.28, 78.6, 1.8, 4.32, 0, 0, 16, 0, 0, 1, 0, 0, 3, 0, 2.4, 1.6, 0, 0],
    [0.732, 0.125, 0.552, 0.9825, 0.24, 0.576, 1.4, 2.52, 0.9, 0.576, 1.598, 2.5, 1.25, 0.135, 2.7, 1.2, 9.52, 5.6, 0, 0.4],
    [-5.856, -4.25, -0.414, -0.262, -0.03, -0.252, -0.6, -0.924, -0.1, -0.576, -11.05, -27.1, -13.55, 0, -21.75, -2.55, -1.12, -3.84, -2.6, -16.8]
]

b_ub = [
    -2000, -60, -800, -35, 80, -14.4, -70
]

# Coefficients of the equality constraints (Ax = b)
A_eq = [
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

b_eq = [2, -3, 3, -5, 3, -5, 4, -11, 1.5, -4.5, 1, -2, 1, -2]

# Bounds for each variable
x_bounds = [(0, None)] * 20

# Solve the problem
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=x_bounds, method='simplex')

# Print results
if result.success:
    print("Optimal value:", result.fun)
    print("Optimal solution:", result.x)
else:
    print("No solution found.")
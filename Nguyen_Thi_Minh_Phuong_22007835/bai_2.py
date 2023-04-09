# gọi a là số ha trong ca phe
# gọi b là số ha trồng điều
# tìm lợi nhuận tối đa nên ta phải cực đại 5a + 3b nghĩa là cực tiểu -5a - 3b
# với các điều kiện a + b = 12, 2a + b <= 16, a + 4b <= 32, 0<=a,b<=12

import numpy as np
from scipy.optimize import linprog
#buoc 1
c = np.array([-5,-3])
#buoc 2.1
A_ub = np.array([[2,1],
                [1,4]])
b_ub = np.array([16,32])
#buoc 2.2
A_eq = np.array([[1,1]])
b_eq = np.array([12])
#buoc 3
a = (0, 12)
b = (0, 12)
bounds = [a, b]
result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
print(result)
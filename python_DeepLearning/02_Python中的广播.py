import numpy as np

# A = np.array([[56.0, 0.0, 4.4, 68.0],
#               [1.2, 104.0, 52.0, 8.0],
#               [1.8, 135.0, 99.0, 0.9]])
#
# cal = A.sum(axis=0)
# print(cal)
#
# percentage = 100*A/cal.reshape(1, 4)
# print(percentage)

# 广播的例子
# B = np.array([[1, 2, 3],
#               [4, 5, 6]])
# C = np.array([100, 200, 300])
# D = B + C
# print(D)

# 案列3
# 不建议这么写
# A = np.random.rand(5)
# print(A)  # [0.66539202 0.17149269 0.69222193 0.30271694 0.37071579]
# print(A.shape)
# print(A.T)
# print(np.dot(A.T, A))

# 建议写法
# A = np.random.rand(5, 1)  # 表明A是一个5*1的矩阵
# print(A)
# assert(A.shape == (5, 1))  # 如果A不是一个5*1的矩阵则会报错
# print(A.T)
# print(np.dot(A, A.T))
# B = A.reshape(5, 1)  # 如果A是一个5*5的矩阵，则会ValueError: cannot reshape array of size 25 into shape (5,1)
# a = np.random.rand(3, 3)
# b = np.random.rand(3, 1)
# c1 = np.dot(a, b)
# c2 = a * b
# print(c2)



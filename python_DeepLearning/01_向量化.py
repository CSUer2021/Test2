import numpy as np  # 导入numpy库
import time  # 导入时间库

# 样例1：使用numpy库中的dot方法
# x = w = np.array([1, 2, 3, 4])
# b = 1
# # print(a)  # [1 2 3 4]
#
# z = np.dot(w, x) + b
# print(z)  # 31

# 样例2：比较for循环计算矩阵相乘与numpy库的dot方法计算矩阵相乘
# a = np.random.rand(1000000)
# b = np.random.rand(1000000)
#
# tic = time.time()
# c1 = np.dot(a, b)
# toc = time.time()
#
# print(c1)
# print("向量版：" + str(1000*(toc-tic)) + "ms")
#
# c2 = 0
# tic1 = time.time()
# for i in range(1000000):
#     c2 += a[i]*b[i]
# toc1 = time.time()
#
# print(c2)
# print("for循环版：" + str(1000*(toc1-tic1)) + "ms")

# 样例3
# v = [i for i in range(1, 10)]
# # print(np.maximum(v, 0))  # MaxiMun方法是求出v中所有元素和0之间相比的最大值
#
# u = np.exp(v)

# 样例4
a = np.random.rand(4, 3)
# axis 用来指明将要进行的运算是沿着哪个轴执行，在 numpy 中，0 轴是垂直的，也就是列，而 1 轴是水平的，也就是行。
b = np.sum(a, axis=1, keepdims=True)
print(a)
print(b)
print(b.shape)



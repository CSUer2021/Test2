import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.figure()  # 定义一个图像窗口

# 画出y=2x+1和y=x^2的图像
# x = np.linspace(-1, 1, 50)  # 定义x数据范围
# y1 = 2*x+1  # 定义y数据范围
# y2 = x**2
# plt.plot(x, y2)  # plot()画出曲线
# plt.show()  # 显示图像

# 画出sigmoid函数
def sigmoid(x1):
    return 1.0 / (1.0 + np.exp(-x1))

x = np.linspace(-10, 10)
y1 = sigmoid(x)
plt.xlim(-11, 11)
plt.ylim(0, 1.1)
plt.plot(x, y1)
plt.show()




import numpy as p
import matplotlib.pyplot as plt
import pandas as pd
import random

from pip._vendor.msgpack.fallback import xrange
from scipy.linalg import solve,inv

def read_data(file_name):
    train_data = pd.read_excel(file_name)  # 得到一个数据框（每一列代表一个实例）
    return[list(train_data.ix[0]), list(train_data.ix[1]), list(train_data.ix[2]), list(train_data.ix[3])]
###算法##
# 1 对数几率回归
def func(x, y, w):
    #'x为样本，y为样本类别，w为权重+偏向'
    n = len(x[0])   # 训练集个数
    m = len(x)   # 每个实例的属性个数 m-1
    result = 0
    for i in xrange(n):
        s = 0
        for j in xrange(m):
            s += x[j][i] * w[j]
        result += -y[i] * (s) + p.log(1 + p.exp(s))
    return result

def p1(x, w):
    # 后验概率估计
    wx = 0
    for i in xrange(len(x)):
        wx += w[i] * x[i]
    return p.exp(wx) / (1 + p.exp(wx))


def dfunc(x, y, w):
    # 一阶导数
    df = p.zeros(len(x))
    for i in xrange(len(x[0])):
        df += x[:, i] * (y[i] - p1(x[:, i], w))
    return -df


def d2func(x, y, w):
    # 二阶导数
    n = len(x[0])
    d2f = p.zeros((n, n))
    for i in xrange(len(x[0])):
        d2f[i][i] = (1 - p1(x[:, i], w)) * p1(x[:, i], w)
    return p.mat(x) * p.mat(d2f) * p.mat(x.transpose())


# 牛顿法
def newtown(x, y, w, error, n):
    i = 1
    while i < n:
        d1 = dfunc(x, y, w)
        if p.dot(d1, d1) < error:
            print ('牛顿法： 迭代 ' + str(i) + '步：w=', w)
            return w
            break
        w = w - solve(d2func(x, y, w), dfunc(x, y, w))
        i += 1


# 梯度下降法
def gradienet_down(x, y, w, error, n):
    i = 1
    h = 0.1
    while i < n:
        start1 = func(x, y, w)
        df = dfunc(x, y, w)
        w = w - h * df
        start2 = func(x, y, w)
        if abs(start1 - start2) < error:
            print ('梯度下降法：迭代' + str(i) + '步：w=', w)
            return w
            break
        i += 1
#可视化
def result_plot(x,y,w_min):
     x1 = p.arange(0, 0.8, 0.01)
     y1 = [-(w_min[2] + w_min[0] * x1[k]) / w_min[1] for k in xrange(len(x1))]
     color = ['r'] * y.count(1.) + ['b'] * y.count(0.)
     plt.scatter(x[0], x[1], c=color)
     plt.plot(x1, y1)


if __name__ == '__main__':
     file_name = '3.0alpha.xls'
     data = read_data(file_name)
     x = data[:3]  # 各实例的属性值
     x = p.array(x)
     y = data[-1] # 类别标记
     w = [1, 1, 1]  # 初始值
     error = 0.0001  # 误差
     n = 1000  # 迭代步数

     w_min=newtown(x,y,w,error,n)

     w_min1= gradienet_down(x, y, w, error, n)

     w_min11=SGD(x, y, w, error, n)

     w_min2=LDA(x, y)

     w_min2=[w_min2[0,0],w_min2[1,0],0]
     # 可视化
     plt.figure(1)
     plt.subplot(221)
     result_plot(x,y,w_min)
     plt.title(u'牛顿法')
     plt.subplot(222)
     result_plot(x,y,w_min1)
     plt.title(u'梯度下降法')
     plt.subplot(223)
     result_plot(x,y,w_min11)
     plt.show()

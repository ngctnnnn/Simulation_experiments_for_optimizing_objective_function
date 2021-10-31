import numpy as np
import math
def Sphere(ind):
    sum = 0
    for i in ind:
        sum += i**2
    return sum

def Rastrigin(ind):
    sum = 10 * len(ind)
    for i in ind:
        sum += i**2 - 10 * np.cos(2*np.pi*i)
    return sum 

def Rosenbrock(ind):
    sum = 0
    for i in range(len(ind) - 1):
        sum += 100 * (ind[i + 1] - ind[i]**2)**2 + (ind[i] - 1)**2
    return sum 

def Griewank(d):
    sum_1 = 0
    for i in d:
        sum_1 += (i*i)/4000
    sum_2 = 1
    for i in range(len(d)):
        sum_2 *= np.cos(d[i]/math.sqrt(i + 1))
    return sum_1 - sum_2 + 1

def Ackley(d):
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = 0
    sum2 = 0
    for i in range(len(d)):
        sum1 += d[i] ** 2
        sum2 += np.cos(c * d[i])
    term1 = -a * np.exp(-b * np.sqrt(sum1 / len(d)))
    term2 = -np.exp(sum2 / len(d))

    return term1 + term2 + a + np.exp(1)
    
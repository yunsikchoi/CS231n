import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0,20,0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = 0.01x^2 + 0.1x")
plt.plot(x,y)
plt.show()

print(numerical_diff(function_1,5))  # 0.199999
print(numerical_diff(function_1,10)) # 0.299999
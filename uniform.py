import matplotlib.pyplot as plt
import numpy as np
rad = 10
num = 1000
t = np.random.uniform(0.0, 2.0*np.pi, num)
r = rad * np.sqrt(np.random.uniform(0.0, 1.0, num))
x = r * np.cos(t)
y = r*np.sin(t)

print(t)
print(r)
print(x)
print(y)

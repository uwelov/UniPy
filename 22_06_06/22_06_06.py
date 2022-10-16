import math
from tkinter import N

#1
print('#1')
def mult(a, b):
    return a * b
print(mult(3, 4))

#2
print('#2')
def square (a, b):
    return math.pow(a, 2) + math.pow(b, 2)
print(square(2, 2))

#3
print('#3')
def equat(x):
    return (math.pow(x, 3)) - (2 * math.pow(x, 2)) + 1
print(equat(3))

n = 153
print(len(n))
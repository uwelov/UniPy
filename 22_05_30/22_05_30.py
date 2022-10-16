print('Ex 1')
#1
import math
#import numpy as np


for i in range(11):
    print(i)
 
print('')   
print('Ex 2')
#2
for i in range(0,21):
    print(i)

print('')
print('Ex 3')
#3
for i in range(1, 16):
    print(math.pow(i,2))

print('')
print('Ex 4')
#4
n = 6
value_n = 1
for i in range(1, n+1):
    value_n = i *value_n
    print(value_n)

print('')    
print('Ex 5')
#5
for i in range(-20,10):
    if i % 2 == 0:
        print(i)

print('')        
print('Ex 6')
#6
a = 8
old_cat = 0

for i in range(1, a+1):
    if i == 1:
        old_cat+=15
    elif i == 2:
        old_cat+=9
    else:
        old_cat+=4
print(old_cat)

print('')
print('Ex 7')
#7(?)
for i in range(0, 11):
    print(i/10)

print('')
print('Ex 8')
#8
for x in range(-10, 11):
    n = math.pow(x,3)-6*math.pow(x,2)+11*x
    print(n)

print('')
print('Ex 9')
#9
for i in range(11):
    print(i, end =' ')
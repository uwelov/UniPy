#test
import math

print("test")
i = 0 
while i < 21:
    if i %2 == 0:
        print(i)
    i+=1


print(" ")
#1
print("#1")
n = 100
i = 2
kol = 1
while i < n:
    print(i, "степінь", kol)
    i*=2
    kol+=1
print(i, "степінь", kol)


print(" ")
#2
print("#2")
n = 81
a = 1
while a*a <= n:
    if a*a == n:
      print(a, "*", a, "=", n)
    else:  
        print(a, "*", a, "=", a*a, "<", n)
    a+=1

print(" ")
#3
print("#3")
v = 0 #швидкість
transmiss = 1
while v <= 150: 
    if v == 15:
        transmiss +=1
    elif v == 35:
        transmiss +=1
    elif v == 50:
        transmiss +=1
    elif v == 65:
        transmiss +=1
    elif v == 80:
        transmiss +=1
    print( v, "км\год", transmiss, "передача")
    v+=5
    
print(" ")
#4
print("#4")
base_tank = int(input()) #цестерня
track_tank = int(input()) #бензовоз
while base_tank >= 0:
    print("цистерна", base_tank, ", бензовоз", track_tank)
    if track_tank <= 10000:
        track_tank+=100
        base_tank-=100
    else:
        break
print(" ")
#5
print("#5")
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a-=b
    elif a < b:
        b-=a
print(a)

print(" ")
#6
print("#6")
border_negative = -10
border_positive = 10
middle = 0
func_value = 0
while middle >= 0.1:
    middle = (border_negative + border_positive)/ 2
    func_value = middle*middle*middle + middle*middle -1
    if func_value <= 0:
      negative_border = middle
    elif func_value > 0:
        positive_border = middle
print(func_value)
print(middle)
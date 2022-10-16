#append +
#remove -
import math
import random

#1
print("1")
a = list()
for i in range (1, 11):
    a.append(i)
print(a)

#2
print("")
print("2")
b = list()
for i in range(4, 21):
    if i % 2 == 0:
        b.append(i)
print(b)

#3
print("")
print("3")
c = list()
kv = list()
for i in range (1, 11):
    if i % 2 == 0:
        num = math.pow(i,2)
        kv.append(num)
    c.append(i)
print(c)
print(kv)

#4
print("")
print("4")
def many():
    mas = list()
    txt = "a"
    for i in range(1, 11):
        mas.append(txt)
        txt += "a"
    return mas
print(many())

#5
print("")
print("5")
def letter():
    mas = list()
    txt = ""
    for i in range(1, 11):
        if i % 2 != 0:
            txt+="a"
            mas.append(txt)
        else:
            txt+="b"
            mas.append(txt)
    return mas
print(letter())

#6
print("")
print("6")
def concl_rand(a, b):
    l = list()
    for i in range(10):
        chis = random.randint(a, b)
        l.append(chis)
    print(l)
    
    l1 = list()
    for j in l:
        if j % 2 == 0:
            l1.append(j)
    return l1
print(concl_rand(1, 101))

#7
print("")
print("7")
def concl_sq(a, b):
    l = list()
    for i in range(10):
        chis = random.randint(a, b)
        l.append(chis)
    print(l)
    l1 = list()
    for j in l:
        num = math.pow(j, 2)
        l1.append(num)
    return l1
print(concl_sq(1, 101))


rev = 5
print(len(str(rev)))
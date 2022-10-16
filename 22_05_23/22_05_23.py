#1
from tkinter.messagebox import YES


n = 200
girl = n * 0.6
boy = n - girl
print("boys:", boy, ", girl:", girl)

#2
name = "Alice"
age = 16
print("Hi", name, ". You are", age, "years old")

#3
n = 10
if (n % 2 ==0):
    print("even")
else:
    print("odd")
    
#4
s = "rfgwuruv"
if (len(s) < 6):
    print("too short")
elif (len(s) > 20):
    print("too long")
else:
    print("pass")
    
#5
a = 5
b = 5
c = 5
print("cos A =", ((a*a + b*b - c*c)/(2 * a * b)))

#if, and, or, not, ==, !=
#8
n = 8
if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
    print("not a prime number")
elif (n == 2 or n == 3 or n == 5):
    print("prime number")

    
#9
number = "+380506321315"
if(len(number) == 13 and number[0] == "+"):
    print("YES")
else:
    print("NO")

#10
n = 15
if(n % 3 == 0 and n % 5 == 0):
    print(151515)
elif(n % 5 == 0 ):
    print(555555)
elif(n % 3 == 0):
    print(3333333)




def Prime(x):
    if x > 1:
        for i in range (2, x-1):
            if x % i == 0:
                return True
            else:
                return False
    else:
        return False
#print(Prime(int(input())))
#2
print("#2")
n = 10
mas = [0]
for i in range(2, n):
    if len(mas) == "0":
        mas.append(1)
    else:
        for j in mas:
            if i % j == 0:
                break
            else:
                mas.append(i)
print(mas)
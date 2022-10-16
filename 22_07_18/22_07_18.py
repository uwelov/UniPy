#2
def fun3(): 
    s = input("")
    dov = len(s)
    if dov > 20:
        return "too long"
    elif dov < 6:
        return "too short"
    else:
        return "pass"
#print(fun3())
#3
def funD():
    base_tank = int(input()) 
    track_tank = int(input()) 
    while base_tank >= 0:
        print("цистерна", base_tank, ", бензовоз", track_tank)
        if track_tank <= 10000:
            track_tank+=100
            base_tank-=100
        else:
            break
funD()

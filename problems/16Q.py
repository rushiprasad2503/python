
def number(xy):
    n = len(xy)
    for i in range(n//2) :
            if xy[i] != xy[n-i-1]:
                return False
            
    return True
xyz = input("")
xyz = str(xyz)
hello = number(xyz)
print(hello)
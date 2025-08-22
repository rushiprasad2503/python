def y(x):
    if x==1:
        return 1
    else :
        return (x*y(x-1))
    
num = int(input(""))
print("factorial:",y(num))
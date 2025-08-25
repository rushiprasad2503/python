def number(n):
    if n==0:
        return "0"
    result = ''
    while n > 0:
        result = str(n%2)+result
        n//=2
    return result

umn= int(input(""))
num = number(umn)
print(num)
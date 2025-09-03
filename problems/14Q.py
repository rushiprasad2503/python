
def number(num1,symbol,num2):
    if symbol =='+':
        print(num1+num2)
    elif symbol =='-':
        print(num1-num2)
    elif symbol =='*':
        print(num1*num2)
    elif symbol =='/':
        if num2 =='0':
            print("Error(cannot divide by zero)")
        else:
            print(num1/num2)
    else:
        print("wrong symbol")

num11 = float(input(""))
symbol1 = input("")
num22 = float(input(""))
calculator = number(num11,symbol1,num22)
print(calculator)
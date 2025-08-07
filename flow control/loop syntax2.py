num = (1,2,3)
for nu in num:
    if nu == 2:
       break
    print(nu)
for num2 in num:
    if num2 == 2 :
       continue
    print(num2)
num1= (5,6)
for num3 in num:
    for num4 in num1:
         print(num3,num4)
    print('--')    
for _ in range(0,4):
    print('hi')
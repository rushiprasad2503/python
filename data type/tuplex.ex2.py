num = ('1', '2', '3')
print(type(num))
for i in num:
    print(i)   
del num
print(num) # This will raise an error since num is deleted
def check_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        else :
            return True

num = int(input(""))
hello = check_prime(num)
print(hello)
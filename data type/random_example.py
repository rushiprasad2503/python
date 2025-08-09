import random
print(random.randrange(10,100))# random from 10 to 100
num = [1,2,3,4,5,6,7]
print(random.choice(num))#random element
random.shuffle(num)#shuffling the list
print(num)#shuffled list
print(random.random())#random float

s = {'apple', 'banan dsxaf^so', 'banan dsxaf@'}
for index, value in enumerate(s):
    print(index, value)
print(enumerate(s))
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
#print(sum(s)) for only numbers
s.add('jje')
print(s)
hj = sorted(s)
print(hj)
s.add('xx')
print(s)
s.clear()
print(s)#set() will be output
s.add('added')
print(s)
s.add("asd")#take only one argument
print(s)
s.discard("asd")
print(s)
s.discard('other')
print(s)



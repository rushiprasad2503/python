f = 'hellO'
print(f.upper())
print(f.lower())
h =f.partition(" ")#if no separator is found,it returns the original string and two empty strings 
print(h)
hj = 'hola amigo'
we = hj.partition(" ")#separator is found,returns a tuple
print(we)
qu = "hola"
jde = qu.replace('la','df')#1st is deleting and 2nd is adding
#needed atleast 2 arguments in replace()
print(jde)
w ='rushi pawale. '
x = w.find('pawale')#returns the lowest index of substring,otherwise -1
print(x)
e = w.rstrip('')#removes spaces from right end of string
print(e)
t = "hello world!"
r = t.rstrip('!')#removes symbols
print(r)
y = t.rstrip('ld!')#removes anythoing from right end of string
print(y)
u = '123he 5'
i = u.rstrip('5')
print(i)
o = t.split()#split a string into list . by default by whitespace
print(o)
p =t.split("o")#split by character
print(p)
print(t.startswith("hello"))#checking if string starts with given in bracket
print(t.startswith("e"))
print(t.isnumeric())#checking if string contains numeric character
print(t.index('o'))# returns the lowest index of given in bracket
# if not present ,then typeError
print(t.index('he'))
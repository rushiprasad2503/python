s = {'apple', 'banan dsxaf^so', 'banan dsxaf@'}
x= {'apple','1','2','3'}
s.intersection_update(x)
print(s)
y = {'4','5'}
print(x.isdisjoint(y))#returns true if both have null intersection
z= {'1','2','3','4','apple'}
print(x.issubset(z))# true if x is subset of z
print(z.issubset(x))
print(x<=z)#true if x is subset of z
print(z.issuperset(x))#true if z is superset of x

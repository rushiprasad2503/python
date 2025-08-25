abcd = str(input(''))
abd =abcd.lower()
output = int(0)
for x in abd:
    if 'a' in x:
        output+=1
    if 'e' in x:
        output+=1
    if 'i' in x:
        output+=1
    if 'o' in x:
        output+=1
    if 'u' in x:
        output+=1
print(output)

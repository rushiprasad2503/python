def vowel(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for xi in string:
        if xi in vowels:
            count+=1
    return count
enter = input('')
result = vowel(enter)
print(result)
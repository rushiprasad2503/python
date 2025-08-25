def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Example usage:
text = input("")
result = count_vowels(text)
print(result)  # Output: 3

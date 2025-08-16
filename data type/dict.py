cou = {
    "csk":"ruturaj",
    "rcb":"rajat"
}
print(cou)
r = {
    'mi':'hardik',
    'dc':'rishabh'
}
print(r)
# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict1 = {(1, 2): "one two", 3: "three"}

# invalid dictionary
# Error: using a list as a key is not allowed
#my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict2 = {"USA": ["Chicago", "California", "New York"]}

print(my_dict)
print(my_dict1,my_dict2)
print(my_dict[1])

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",#,will be ignored
}
print(file_types)

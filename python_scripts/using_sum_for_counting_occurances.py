#count all the uppercase letters in a string
result = sum(1 for char in "BaNaNa" if char.isupper())
print(result)

#count all the uppercase letters in a file
num_upper = sum(1 for line in open("file.txt","r") for char in line if char.isupper())
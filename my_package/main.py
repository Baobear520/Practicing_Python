
def count_upper_in_file(filename):
    # Reading the file and counting uppercase letters
    with open(filename) as f:
        #Using generator expression
        num_uppercase = sum(1 for line in f for character in line if character.isupper())
    print(num_uppercase)

if __name__ == "__main__":

    file_content = """Hello World!
    This is a test file.
    Python is Fun!"""
    # Writing the example content to the file for demonstration purposes
    with open('filename.txt', 'w') as f:
        f.write(file_content)

    count_upper_in_file('filename.txt')
    


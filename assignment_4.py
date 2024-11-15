# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

""" with open('testfile.txt', 'r') as file:
    content = file.read()
    print(content)
    
newContent = content.title()    

    
with open('testfile2.txt', 'w') as file2:
    file2.write(newContent)
print("File have been modified") """


# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

fileName = input("Enter the name of the file: ")

try:
    with open(fileName, 'r') as file:
        content = file.read()
        print("The file have been read and it's output is displayed below\n")
        print(content)
except FileNotFoundError:
    print('The file name was not found')
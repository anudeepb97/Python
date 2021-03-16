'''
FILE IO - File Input & Output

Any File can be accessed using File IO methods
'''

# To read a file
my_file = open('a.txt','r')
my_file.seek(0)
print(my_file.read())
my_file.close() # It's best practice to close a file once it is opened

# To read a file using with statement
with open('a.txt', 'r') as my_file2: # advantage of with statement, it automatically closes the file
    print(my_file2.read())

# To write a file using with statement
with open('a.txt', 'w') as my_file3:
    print(my_file3.read())


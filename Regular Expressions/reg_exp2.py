import re

# Email Validation
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
#
# string = input('Enter a email address: ')
# a = pattern.search(string)
# print(a)

# Password validation
pattern2 = re.compile(r"([a-zA-Z0-9\b$%#@]{8,}\d)")
string2 = input('Enter your password: ')
b = pattern2.fullmatch(string2)
print(b)
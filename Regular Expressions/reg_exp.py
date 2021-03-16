import re

string = 'Search this inside of this text please!'

# 1
print(re.search('this', string))

# 2
a = re.search('this', string)

print(a.span())
print(a.start())
print(a.end())

# 3

pattern = re.compile('this')
a = pattern.search(string)
print(a.group())

# Multiple searches
b = pattern.findall(string)
print(b)

# 4 Only Full Match
pattern1 = re.compile('Search this inside of this text please!')
c = pattern1.fullmatch(string)
print(c)

# 5 Match ( looks for start of the string and doesn't care about what comes afterwards
string1 = 'Anudeep Search this inside of this text please!'
pattern2 = re.compile('Search this inside of this text please!')
d = pattern2.match(string1)
print(d)

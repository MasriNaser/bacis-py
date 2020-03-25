"""
"""

name = 'Naser'
age = 34

# concatenate
print('hello,my name is ' + name + ' and I am ' + str(age))

# Arguments by position
print('my name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
print(f'Hello, my name is {name} and I am {age}')

# string method
s = 'hello world'
# to Cap string the first letter
print(s.capitalize())

#Get lenth
print(len(s))

#split
print(s.split())
#
print(s.split('r'))

#find pos
print(s.find('o'))

#is alphanumeric
print(s.isalnum())


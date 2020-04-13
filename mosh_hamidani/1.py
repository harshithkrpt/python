# full_name = "John Smith"
# age = 20
# is_new = True

# print(full_name[0:-2])

# first = 'Harshith'
# last = 'Kurapati'
# msg = f'{first} [{last}] is a programmer'
# print(msg)

# --------- String Methods ------------------

import openpyxl
from packages.shipping import clac_shipping
import math
from pathlib import Path
course = 'Python for Beginners'
print('Length : '+str(len(course)))
print("Upper Method : "+course.upper())
print("Lower Method : "+course.lower())
print("Find Method : "+str(course.find('Beg')))
print("Replace Method : " + str(course.replace('Beg', 'Exp')))
print("Replace Method : " + str(course.replace('n', 'p')))
print('Python' in course)


# --------- Number Functios ------------------
x = 2.9
print("Round of 2.9  " + str(round(x)))
print("abs of 2.9 " + str(abs(-2.9)))

print("Ceil of 1.3 = " + str(math.ceil(1.3)))
print("Log = " + str(math.log(2)))
print("Math.frexp(2*3)"+str(math.frexp(2*3)))
print('GCD of 20 10 ' + str(math.gcd(10, 20)))


# Loops
# while
i = 1
while i <= 5:
    print(i)

    i += 1

secret_number = 23
guess_count = 0
guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won')
#         break
# else:
#     print('You Lost')

# FOR Loop
for i in 'harshith':
    print(i)
for i in ['apple', 'bike', 'car', 'dog']:
    print(i)
for i in range(10):
    print(i)
print('5 to 10')
for i in range(5, 11):
    print(i)
print('5 to 10 (2) string : ')
for i in range(5, 11, 2):
    print(i)

for x in range(4):
    for y in range(5):
        print(f'({x},{y})')


names = ['John', 'Bob', 'Mosh', 'Sarah']
print(names)
print(names[-1])
print(names[2:])
print(names[1:3])
print(names[0:3:2])  # 0 index to 3-1 index and 2 steps


# List Methods
numbers = [5, 2, 1, 7, 4]
numbers.sort()
print("Numbers (Sorted) : " + str(numbers))
numbers.append(13)
print("Append : " + str(numbers))
numbers.insert(2, 134)
print("Insert : " + str(numbers))
numbers.sort()
numbers.reverse()
print("Numbers (Sorted) Descending Order : " + str(numbers))
numbers.remove(134)
print("Numbers : " + str(numbers))
# numbers.clear()
# print(numbers)
numbers.pop()
print(numbers)
print("Index of 2 in numbers is : " + str(numbers.index(2)))
print('in operator 5 in numbers : ' + str(5 in numbers))
# copy of a list
numbers2 = numbers.copy()
numbers2.append(10)
print('numbers2 : '+str(numbers2))
print('numbers  : '+str(numbers))
# remove duplicates
num = [1, 2, 3, 2, 4, 9, 2, 9]

# mosh approach
uniques = []
for number in num:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# tuples - immutable
numbers = (1, 23, 32, 1, 1, 1, 1)
print(numbers.count(1))
print(numbers.index(1))

# unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print('x:'+str(x))
print('y:'+str(y))
print('z:'+str(z))
cords = [1, 2, 3]
x, y, z = cords
print('x:'+str(x))
print('y:'+str(y))
print('z:'+str(z))


# Dictionaries
dictionary = {'name': 'Harshith', 'email': 'harshith.krpt@gmail.com'}
print(dictionary.get('name'))
print(dictionary['name'])
print(dictionary.get('names'))
dictionary['name'] = 'Sadvika'
print(dictionary)

phone = input('Phone : ')
digits_mapping = {
    "1": 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


# Classses

# ----------- OOP---------------
class EmailClient:
    def __init__(self):
        print(self)

    def walk(self):
        print('hello')


class Pass(EmailClient):
    pass


pa = Pass()
pa.walk()


# Absolute Path
# Relative Path
p = Path('package')
print(p.exists())
p.mkdir()

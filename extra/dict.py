# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

# print(eggs == ham)

# spam = {'name': 'Zophie', 'age': 7}
# print(spam['color'])

import pprint
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name : (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of '+name)
    else:
        print("I don't have birthday information for "+name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')


# keys() , values() and items() Methods :

spam = {'color': 'red', 'age': 42}

print('The VAlues : ')
# for values

for v in spam.values():
    print(v)

print('\n')
print('The Keys')

for k in spam.keys():
    print(k)
print('\n')

# items return tuples
for i in spam.items():
    print(i)
    print(type(i))


# in
spam = {'name': 'Zohie', 'age': 7}
print('name' in spam.keys())


# get method
prinxItems = {'apples': 5, 'cups': 2}
print('I am bringing '+str(prinxItems.get('cups', 0))+' items')

print('I am bringing ' + str(prinxItems.get('eggs', 0)) + ' eggs.')


# setdefault
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)
# for same key only once you can set the default value
spam.setdefault('color', 'white')
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# pretty printing

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1

# normal print
print(count)

# pretty
pprint.pprint(count)


theBoard = {'top-L': 'X', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': '0', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn For '+turn+'. Move on which white space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

printBoard(theBoard)


# nested dictionaries and lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)

    return numBrought


print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

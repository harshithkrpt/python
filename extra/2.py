# from random import randint
# import random
# for i in range(5):
#     print(random.randint(1, 10))

# print(randint(1, 2))


# import sys

# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You Typed '+response+'.')


# def hello():
#     print('Howard !')
#     print('Howard !!!')
#     print('Hello There')


# hello()
# hello()
# hello()

# span = print('Hello!')
# if None == span:
#     print(True)


# def span():
#     global eggs
#     eggs = 'Globall change'
#     print(eggs)


# def bacon():
#     eggs = 'bacon eggs'
#     print(eggs)
#     span()
#     print(eggs)


# eggs = 'global'
# bacon()
# print(eggs)


# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid Argument')


# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


# catNames = []
# while True:
#     print('Enter the '+str(len(catNames)+1) +
#           ' Cat Name of Enter Nothing to stop.')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]

# print('The Cat Names are : ')
# for name in catNames:
#     print(' ' + name)


# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i in range(len(supplies)):
#     print('Index '+str(i)+' in supplies is : '+supplies[i])


# myPets = ['Zophie', 'Pooks', 'Fat-tail']
# print('Enter a pet name : ')
# name = input()
# if name not in myPets:
#     print('I dont have a pet named '+name)
# else:
#     print(name + ' is my pet')


cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

a = 10
b = 20
a, b = b, a
print('a'+str(a))
print('b'+str(b))


span = 42
span = span + 1
span

span = 42
span += 1
span

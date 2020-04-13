# import os

# # file
# passwordFile = open('SecretPassword.txt')
# secretPassword = passwordFile.read()
# print("Enter your Password : ")
# typePassword = input()
# if typePassword == secretPassword:
#     print('access Granted')
#     if typePassword == '12345':
#         print('That password is one that an idiot puts on their luggage')
# else:
#     print('Access Denied')

# print(os.getcwd())

# for x in 'span':
#     print(x)


# print("Hello World")
# print('what is your name')
# myName = input()
# print('The Length of your name is : ')
# print(len(myName))
# print('What is your age ?  ')
# myAge = input()
# print('You will be '+str(int(myAge)+1) + ' in a year .')

# name = ''                           # (1)
# while name != 'your name':          # (2)
#     print('Please type your name.')
#     name = input()                  # (3)
# print('Thank you!')                 # (4)


# while True:
#     print("Who are You?")
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello Joe What is the password ? Hint : it is a fish')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access Grante.')

# name = ''
# while not name:
#     print('Enter Your Name : ')
#     name = input()
# print('How many guests will you have ?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be Sure to have enough room for all your guests.')
# print('Done')


print("My Name is : ")
for i in range(5):
    print('Jimmy Five Times ('+str(i)+')')


for i in range(12, 16):
    print(i)


# increment by 2 upto 9
for i in range(0, 10, 2):
    print(i)


# decrement by -1 upto 0
for i in range(5, -1, -1):
    print(i)

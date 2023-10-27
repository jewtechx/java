#Get name of program user
identity = input('What is your name, man? ')
name = identity.split(" ")
#print a welcoming message
print(f' \t \t Your name is {identity}?.  Wow! nice meeting you {name[0]}' , '. I am MysteryBot created by JewTech - X.')

#Get user's issue

help = input(f'How can I help you {name[0]}')

#remove white spaces infront and at the back of help
helpMain = help.strip()

"""
Render the approprait help to the user. Sometimes you will have to redirect the user to the documentation okay!!
"""

surnames = name[1:]

def surname(*args):
    names = []
    for name in args:
        names.append(name)
    return names

surnamesFormat = surname(*surnames)
printsurname = print(*surnamesFormat)

#condition to check the value of main
if helpMain == 'docs': print(f'{name[1]} , Kindly go to docs.python.com and read the documentation. You will probably find an answer. Hope this helped. In contrast \n you can visit \'JewTech - X\' website to find a full docs on python')
else : print(f'bye bye, Mr.{printsurname}')
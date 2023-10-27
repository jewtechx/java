
from createplayer import createPlayer,Score
import csv
details = []
with open('players.csv')as file:
    reader = csv.DictReader(file)
    for detail in reader:
        details.append({"pname":detail["playName"],"prole":detail["playRole"],"pheight":detail["playHeight"],"pweight":detail["playWeight"],"pcolor":detail["playColor"],"pskills":detail["playSkills"]})

    playerId = len(details) - 1
    specificPlayer = details[playerId]
    #logging to console
    create = createPlayer(specificPlayer["pname"],specificPlayer["prole"],specificPlayer["pheight"],specificPlayer["pweight"],specificPlayer["pcolor"],specificPlayer["pskills"])

    remark = Score(specificPlayer["pname"],specificPlayer["prole"],specificPlayer["pheight"],specificPlayer["pweight"],specificPlayer["pcolor"],specificPlayer["pskills"],1,'102122 points','Distinction')

    print(create.physic())
    print(create.skills())
    print(remark.status())



# name = input('Enter your name')
# product = input('Enter the product you want to buy ')

# order = "Hello JewMarts, I am {}. I want to buy {}"
# print(order.format(name,product).center(90," "))

# list = ('Jew','larbi','Danquah')

# if 'Jew' in list:
#    print('Jew is in the list of billonaires')
# for i in list:
#    print(i)

# def students_detail(*details):
#     return details
# name,level,program = students_detail('Jew','L100','Physics and Computer Science')
# details = 'This are the details of  {}. He is in {} offering {}'
# print(details.format(name,level,program))
# #tri_recursion

# # def tri_recursion(k):
# # #     if k > 0:
# # #         print('Your machine is about crashin')
# # #         k += -1
# # #     else:
# # #         print('Youre damn lucky')
# # # tri_recursion(10)
# a= 1
# b=2
# print(lambda a,b : a + b)



"""
Classes/Objects
"""
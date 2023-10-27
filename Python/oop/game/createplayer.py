import csv
# creating classes
class createPlayer:
    def __init__(player,name,role,height,weight,color,skills):
        player.name = name
        player.role = role
        player.height = height
        player.weight = weight
        player.color = color
        player.abilities = skills 
    
    def physic(phys):
        return f"{phys.name} is the player you created and he plays the role of a {phys.role}. He is {phys.height} feet(s) tall and weights {phys.weight}. He is {phys.color} in complexion"
    
    def skills(skill):
        return f"{skill.name} has these skills: {skill.abilities}"


class Score(createPlayer):
    def __init__(player, name, role, height, weight, color, skills,level,score,remark):
        super().__init__(name, role, height, weight, color, skills)
        player.level = level
        player.score = score
        player.remark = remark

    def status(status):
        return f"In level {status.level}, your player {status.name} scored {status.score}. That is {status.remark} buh a player of height {status.height} feets(s) should do better"
 
 #Game initialization
print("Hey there! Warm greetings to you. You're welcome to mickeyPool online gaming")
name = input('Enter your name ')

print(f'Alright {name}, you\'re successfully registered for this tournament')
print("Create your player by providing player details in spaces below")

#creating player
playerName = input('Name of player ')
playerRole = input('What role do you want to assign your player to ')
playerHeight = input('Height of player ')
playerWeight= input('Weight of player ')
playerColor = input('What is the complexion of your player ')
playerSkills = input('What skills do you want your player to have ')

#creating a file to save players
with open('players.csv','a') as file:
    writer = csv.DictWriter(file,lineterminator='\n', fieldnames=["playName","playRole","playHeight","playWeight","playColor","playSkills"])
    writer.writerow({"playName":playerName,"playRole":playerRole,"playHeight":playerHeight,"playWeight":playerWeight,"playColor":playerColor,"playSkills":playerSkills
        }
    )
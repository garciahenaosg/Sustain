import random
import time

def displayIntro():
    print("In October 2018, the Intergovernment on Climate Change released a special report on the climate.")
    time.sleep(0)
    print("The special report stated that if the world wanted to avoid catastrophic climate levels, they had to cut emissions 50 percent by 2030")
    time.sleep(0)
    print("The world didn't take heed to the warning. Many tried to solve the problems individually but due to freerider mentality, they didn't make it in time.")
    time.sleep(0)
    print("With no cooperation, scientists were not able to reverse the damage. Three woman, however, were able to create a time traveling device.")
    time.sleep(0)
    print("With the irrefutable evidence they brought back in time, countries were forced to listen.")
    time.sleep(0)
    print("Every country on Earth signed the \'UNLESS\' Act, stating that any citizens exceeding a carbon footprint of .012 tons of CO2 a day would be executed.")
    time.sleep(0)
    print("Desperate times, it seems, call for desperate measures")
    time.sleep(0)
    print("Now you have to live everyday thinking:")
    time.sleep(0)
    print("What is best for me?")
    time.sleep(0)
    print("What is best for the environment?")

displayIntro()

total_carbon = 0


def wakeup():
    path = ""
    while path != "get up" and path != "get out of bed" : # input validation
        path = input ("You wake up bright and early one morning. >")
    return path

wakeup()

print("You get out of bed.")

def lookaround():
    path = ""
    while path != "look" : # input validation
        path = input (">")
    return path

lookaround()

print("You can\'t see anything- it\'s still dark outside")

def searcharound():
    path = ""
    while path != "search": # input validation
        path = input (">")
    return path

searcharound()

print("You find a light switch and blinds")

# The first decision
while True:
    path_1 = input(">")
    if path_1 == "turn on light":
        print ("light is on. +.01 Carbon")
        total_carbon = (total_carbon + 0.01)
        print("Total Carbon: {0}".format(total_carbon))
        time.sleep(2)
        print("unless your house runs of renenwable energy, using electricity increases your carbon footprint.")
        break
    if path_1 == "open blinds":
        print ("light fills the room")
        break
    
    print("Try something else")



def lookaround():
    path = ""
    while path != "look" : # input validation
        path = input (">")
    return path

lookaround()

print ("You see a door and a closet.")

while True:
    path_2 = input(">")
    if "open door":
        print("You walk out naked into the hallway.")
        break

    if path_2 =="open closet":
        print ("Search through clothes")
        time.sleep(3)
        print ("You are out of clothing.")
        break

path_3 = input(">")

if path_3 == "go back":
    print("You walk back into your room, unnoticed.")

path_4 = input (">")

if path_4 =="open closet":
    print ("Search through clothes")
    time.sleep(3)
    print ("You are out of clothing.")

path_6 = input (">")

if path_6 == "wash clothes":
    print("You wash your clothes")
    time.sleep(3)
    print ("+.06 Carbon")

if path_6 == "wear dirty clothes":
    print ("You smell bad")

if path_6 == "buy new clothes":
    print ("You call your mom and she buys you new clothing.")
    time.sleep(3)
    print ("+.01 Carbon")























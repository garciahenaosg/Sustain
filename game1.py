#print(input("What's your name? *"))
player_name = input("what's your name? *")
#print("Your name is {}.".format(player_name))

import time

print("hi {}.".format(player_name))
care_1 = input("are you ready to save the Earth? *")
if care_1 == "yes":
    print ("great")
elif care_1 == "no":
    print ("too bad. choice is an illusion")
else:
    care_2 = input("we don't capitalize here. are you ready to save the Earth? *")
    if care_2 == "yes":
        input(print ("great. let's get started. *"))
    elif care_1 == "no":
        input(print ("too bad. choice is an illusion. *"))
    else:
        input("we don't capitalize here. are you ready to save the Earth? *")
        

time.sleep(1)
print("you come to in a grassy field. there is a forest to the south, and a house to the north.")
path_1 = input("what direction do you want to go? *")

#south path (1)
if path_1 == "south":
    print("the smell of the trees remind you of summers when you were younger.")
    time.sleep(1)
    print("you instantly grow bitter at the loss of your youth, and grumble aloud.")
    time.sleep(1)
    print("you hear a voice behind you. ")
    time.sleep(1)
    print("\"we have been waiting far too long for you to arrive \" *")
    time.sleep(1)
    path_1a = input("do you turn around or run away? *")
    if path_1a == "turn around":
        print("you see three women who are barefoot and draped in tunics. they remind you of the goddesses in myths you used to read.  *")
    if path_1a == "run away":
        print("you don't make it far before your body betrays you. while gasping to catch your breath, you trip on a small stick and go flying. ")
        time.sleep(1)
        print("you hear clapping behind you and slowly turn around")
        time.sleep(1)
        print("\"way to go\". your face turns red as you realize the voice belongs to the most beautiful woman you've ever seen. ")
        time.sleep(1)
        print("she grabs you by the collar of your shirt and drags you towards two other beautiful women. ")

    time.sleep(1)
    print(input("the woman on the left speaks first. \"we are the daughters of gaia, born to protect the earth and all of its inhabitants.\" * "))

    path_1b = input("they stare at you expectantly, and you question what the proper etiquette is for greeting goddesses. do you bow or speak to them? *")
    if path_1b == "bow":
        print("the goddesses giggle at you. \"freak\" mutters the one in the middle. ")
    if path_1b == "speak":
        print("before you get a noise out of your mouth, the goddess on the right smacks you in the face. \"disrespectful humans\" she mutters. ")

    time.sleep(1)
    print("the woman on the right speaks up. \"we are coming to you because we are deseparate. our mother is getting angry.\" ")
    time.sleep(1)
    print("they see the confusion on your face. our mother, earth, is getting sick. she is considering a detox.\" ")
    time.sleep(1)
    print("\" she says that if she isn't feeling atleast 50 percent better by 2030, she will begin the process of flushing out humans.\"  ")
    time.sleep(1)
    print("\" that is only 11 years away. we are in the process of contacting all humans, but it will take effort from each of you to keep our mother from getting too angry\" ")

    path_1c = input("\" will you do your part? \" * ")
    if path_1c == "yes":
        print("\" then all you have to do is wake up. \" ")
    if path_1c == "no":
        print("\" it is not possible to be a free rider any longer- this is life or death. wake up and get to work. \" ")


#north path (2)
if path_1 == "north":
    print("you approach a small house that looks abandoned.")

path_2 = input("what do you do? *")
if path_2 == "open door":
    path_2a = input("the door creaks open slowly. you see a cluttered room filled with documents and books. *")
    if path_2a == "examine books":
        path_2b = input("the books range from new to old, scientific to not. you recognize the titles \'small is beautiful\', and \'the lorax\'. *")
        if path_2b == "examine small is beautiful":
            print("\"any intelligent fool can make things bigger, more complex, and more violent.")
            input("it takes a touch of genius — and a lot of courage — to move in the opposite direction.\" *")
        if path_2b == "examine the lorax":
            input("\" unless someone like you cares a whole awful lot, nothing is going to get better- it\'s not.\" *")
    if path_2a == "examine documents":
        path_2c = input(" there are a scattering of documents that hold scientific data. you see one that says \"IPCC Special Report.\" * ")
        if path_2c == "examine IPCC special report":
            print("intergovernmental panel on climate change")
            print("human activities are estimated to have caused approximately 1.0°C of global warming above pre-industrial levels, with a likely range of 0.8°C to 1.2°C. Global warming is likely to reach 1.5°C between 2030 and 2052 if it continues to increase at the current rate.")
            print("climate models project robust differences in regional climate characteristics between present-day and global warming of 1.5°C, and between 1.5°C and 2°C.8 These differences include increases in mean temperature in most land and ocean regions, hot extremes in most inhabited regions, heavy precipitation in several regions, and the probability of drought and precipitation deficits in some regions")









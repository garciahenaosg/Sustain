current_room = "bedroom"
bedroom_light_bulb = "off"
bathroom_light = "off"
shower = "off"
faucet = "off"
bed_blinds = "closed"
bath_blinds = "closed"
clothing = "dirty"
clothed = "no"
new_clothes = "clean"
total_carbon = 0
teeth = "dirty"
hands = "clean"
import time

def displayIntro():
    print("In October 2018, the Intergovernment on Climate Change released a special report on the climate.")
    time.sleep(2)
    print("The special report stated that if the world wanted to avoid catastrophic climate levels, they had to cut emissions 50 percent by 2030")
    time.sleep(2)
    print("The world didn't take heed to the warning. Many tried to solve the problems individually but due to freerider mentality, they didn't make it in time.")
    time.sleep(2)
    print("With no cooperation, scientists were not able to reverse the damage. Three woman, however, were able to create a time traveling device.")
    time.sleep(2)
    print("With the irrefutable evidence they brought back in time, countries were forced to listen.")
    time.sleep(2)
    print("Every country on Earth signed the \'UNLESS\' Act, stating that any citizens exceeding a carbon footprint of .012 tons of CO2 a day would be executed.")
    time.sleep(2)
    print("Desperate times, it seems, call for desperate measures")
    time.sleep(2)
    print("Now you have to live everyday thinking:")
    time.sleep(2)
    print("What is best for me?")
    time.sleep(2)
    print("What is best for the environment?")

displayIntro()

total_carbon = 0
print("test")
def wakeup():
    path = ""
    while path != "get up" and path != "get out of bed" : # input validation
        path = input ("You wake up bright and early one morning. >")
    return path

wakeup()

print("You get out of bed.")
def can_see_in_bedroom():
    global bedroom_light_bulb
    global bed_blinds

    return (bedroom_light_bulb == "on" or bed_blinds == "open")

def can_see_in_bathroom():
    global bathroom_light
    global bath_blinds

    return (bathroom_light == "on" or bath_blinds == "open")


def make_decision():
    global bedroom_light_bulb
    global total_carbon
    global shower
    global faucet
    global bathroom_light
    if bedroom_light_bulb == "on":
        total_carbon = (total_carbon + 0.01)
    if bathroom_light == "on":
        total_carbon = (total_carbon + 0.01)
    if shower == "on":
        total_carbon = (total_carbon + 0.02)
        print("The shower is on.")
    if faucet == "on":
        total_carbon = (total_carbon + 0.01)
        print("The faucet is on.")
    if bathroom_light == "on" or bedroom_light_bulb == "on":
        print("The light is on.")
    print("Total Carbon: {0}".format(total_carbon))
    if total_carbon >.1:
        print("You die")
        current_room = "end game"



def mom_cloth():
    global new_clothes
    global clothing
    global total_carbon
    if new_clothes == "clean":
        clothing == "clean"
        total_carbon = total_carbon + 0.02


# Bedroom
#  turn on or blind
#  closet
#  leave to hallway
def do_bedroom():
    global bedroom_light_bulb
    global total_carbon
    global current_room
    global bed_blinds
    global clothing
    global new_clothes
    global total_carbon
    global clothed
    while True:
        path_1 = input(">")

        if path_1 == "quit":
            current_room = "end game"
            break

        if (path_1 == "look" and can_see_in_bedroom()):
            print("You see a door and a closet.")
            make_decision
            continue

        if (path_1 == "look" and not can_see_in_bedroom()):
            print("It\'s dark.")
            make_decision
            continue

        if (path_1 == "turn on light" and bedroom_light_bulb == "off"):
            print ("light is on. +.01 Carbon")
            time.sleep(3)
            print("** unless your house runs of renenwable energy, using electricity increases your carbon footprint.")
            bedroom_light_bulb = "on"
            make_decision()
            continue

        if (path_1 == "turn off light" and bedroom_light_bulb == "on"):
            print ("light is off.")
            time.sleep(3)
            bedroom_light_bulb = "off"
            make_decision()
            continue

        if path_1 == "open blinds":
            print ("Light fills the room")
            bed_blinds = "open"
            make_decision()
            continue

        if path_1 == "open door" and can_see_in_bedroom():
            if clothed == "no":
                print("You walk out naked into the hallway.")
                current_room = "hallway"
                time.sleep(3)
                make_decision()
                break
            else:
                print("You walk into the hallway")
                current_room = "hallway"
                make_decision()
                break


        if path_1 == "open closet" and can_see_in_bedroom():
            print ("Search through clothes")
            time.sleep(3)
            print ("You are out of clothing.")
            make_decision
            continue

        if path_1 == "wash clothes" and can_see_in_bedroom() and "clothing=dirty":
            print ("You wash your clothes, and now your underwear smells like roses")
            time.sleep(3)
            print("+.06 Carbon")
            total_carbon = (total_carbon + 0.06)
            print( "Total Carbon: {0}".format(total_carbon))
            time.sleep(3)
            print("Washing your laundry every two weeks results in .2 tons of CO2 emmisions a month.")
            clothing = "clean"
            make_decision
            continue 

        if path_1 == "buy clothes" and mom_cloth():
            print("How old are you?")
            time.sleep(3)
            print("Spending $100 every month is equivalent to .001 tons of CO2 a day")
            print("+.01 Carbon")
            total_carbon = (total_carbon + 0.01)
            print( "Total Carbon: {0}".format(total_carbon))
            continue

        if path_1 == "wear clothes" and can_see_in_bedroom() and clothing == "dirty":
            print ("You smell.")
            make_decision
            clothed = "yes"
            make_decision()
            continue 

        if path_1 == "wear clothes" and can_see_in_bedroom() and "clothing=clean":
            print ("You're looking fly- but at what cost?")
            mom_cloth
            clothed = "yes"
            continue

        print("Try something else")



# Hallway
def hallway():
    print("You are in the hallway.")

    while True:
        path_2 = input(">")

        if path_2 == "quit":
            current_room = "end game"
            break

        if (path_2 == "look"):
            print("You see a door in front of you and the hallway continues to the left.")
            continue

        if (path_2 == "open door"):
            print("You open the bathroom door")
            current_room == "bathroom"
            do_bathroom()
            break

        if (path_2 == "walk left"):
            print("Coming soon")
            continue

        if (path_2 == "go back"):
            do_bedroom()
            break

        print("Try something else.")

def do_bathroom():
    global bath_blinds
    global bathroom_light
    global shower
    global toilet
    global faucet
    global teeth
    global hands
    global total_carbon
    print ("You are in the bathroom. Do your morning routine.")
    while True:
        path_3 = input(">")

        if path_3 == "quit":
            current_room = "end game"
            break

        if (path_3 == "look" and can_see_in_bathroom()):
            print("You see a shower, a toilet, and a sink") 
            make_decision()
            continue

        if (path_3 == "look" and not can_see_in_bathroom()):
            print("It is dark") 
            make_decision()
            continue

        if (path_3 == "turn on light"):
            print("You turn on light")
            make_decision()
            continue

        if (path_3 == "open blinds"):
            print("Light fills the room")
            bath_blinds = "open"
            make_decision()
            continue

        if (path_3 == "get in shower"):
            print("You get in the shower")
            make_decision()
            continue

        if (path_3 == "turn on shower" and clothed=="no"):
            print("You turn on the shower.")
            time.sleep(3)
            print("scrub a dub dub")
            shower = "on"
            make_decision()
            continue

        if (path_3 == "turn on shower" and clothed=="yes"):
            print("You turn on the shower. You are still fully dressed")
            time.sleep(3)
            print("idiot")
            shower = "on"
            make_decision
            continue

        if (path_3 == "turn off shower"):
            print ("You turn off the shower.")
            shower = "off"
            make_decision
            continue

        if (path_3 == "get out of shower"):
            print("You get out of the shower.")
            make_decision
            continue

        if (path_3 == "use toilet"):
            bowels = input("1,2, or both? >")
            if bowels == "1":
                print ("You pee.")
                hands = "dirty"
                total_carbon = (total_carbon + 0.001)
                make_decision()
                continue

            if bowels == "2" or "both":
                print ("Congrats on your bowel movement")
                hands = "dirty"
                total_carbon = (total_carbon + 0.01)
                print("Total Carbon: {0}".format(total_carbon))
                make_decision()
                continue

        if (path_3 == "turn on sink"):
            print("You turn on sink.")
            faucet = "on"
            make_decision()
            continue

        if (path_3 == "turn off sink"):
            print ("You turn off the sink.")
            faucet = "off"
            make_decision()
            continue

        if (path_3 == "wash hands" and faucet=="off"):
            print("The sink isn't on.")
            make_decision()
            continue

        if (path_3 == "wash hands" and faucet=="on"):
            print("You wash your hands.")
            hands = "clean"
            make_decision()
            continue

        if (path_3 == "brush teeth" and faucet=="off"):
            print("The sink isn't on.")
            make_decision()
            continue

        if (path_3 == "brush teeth" and faucet=="on"):
            print("You brush your teeth")
            teeth = "clean"
            make_decision()
            continue

        if (path_3 == "leave bathroom"):
            if teeth == "dirty":
                print ("You didn't brush your teeth... ew")
            if hands == "dirty":
                print("You didn't wash your hands??")
            if teeth == "clean" and hands == "clean":
                print ("You left the bathroom")
                current_room = "hallway"
            make_decision()
            continue

        

        print("Try something else.")

# Kitchen



while True:
    if current_room == "bedroom":
        do_bedroom()
        continue
    if current_room == "hallway":
        hallway()
        continue
    if current_room == "bathroom":
        do_bathroom()
        continue

    if current_room == "end game":
        print("Thank you for playing")
        exit()





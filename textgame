current_room = "bedroom"
bedroom_light_bulb = "off"
hallway_light= "off"
bed_blinds = "closed"
hallway_blinds = "closed"
clothing = "dirty"
clothed = "no"
new_clothes = "clean"
total_carbon = 0
import time

def can_see_in_bedroom():
    global bedroom_light_bulb
    global bed_blinds


    return (bedroom_light_bulb == "on" or bed_blinds == "open")

def can_see_in_hallway():
    global  hallway_light
    global bed_blinds
    return (hallway_light == "on" or blinds == "open")

def make_decision():
    global bedroom_light_bulb
    global total_carbon
    if bedroom_light_bulb == "on":
        total_carbon = (total_carbon + 0.01)
    if hallway_light == "on":
        total_carbon = (total_carbon + 0.01)
    if hallway_light == "on" or bedroom_light_bulb == "on":
        print("The light is on.")
    print("Total Carbon: {0}".format(total_carbon))


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

        if path_1 == "open door" and can_see_in_bedroom() and clothed == "no":
            print("You walk out naked into the hallway.")
            current_room = "hallway"
            time.sleep(3)
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
    global hallway_light
    time.sleep(3)
    print ("You are in the hallway")
    while True:
        path_2 = input(">")
        if (path_2 == "turn on light" and hallway_light == "off"):
            hallway_light = "on"
            print(" The hallway light is on.")
            make_decision
            continue




# Kitchen



while True:
    if current_room == "bedroom":
        do_bedroom()
        continue
    if current_room == "hallway":
        hallway()
        continue





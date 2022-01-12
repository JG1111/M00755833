import opc
import time
from time import sleep
client = opc.Client('localhost:7890')

red_colour = [(255,0,0)]
green_colour = [(0,255,0)]
blue_colour = [(0,0,255)]
fade_amount = 10

###-----------------------------------------------------------------------------
###-----------------------------------------------------------------------------

def pulse(colour):

    fade_amount = 10
    leds = [(255,0,0)]*360
    client.put_pixels(leds)
    client.put_pixels(leds)
    for led in range(len(leds)):
        leds[led] = (0, 255, 0)
        time.sleep(.1)
        client.put_pixels(leds)



###-----------------------------------------------------------------------------
###------------------------------Pokemon-Type-----------------------------------

def pokemon(main_select):
    print("-------------------------------------------------------------------------")
    if main_select == 1:
        userinput = int(input('''Choose a pokemon type:
        ----------------------
        1.Fire
        2.Water
        3.Grass
        ----------------------'''))
        print("-------------------------------------------------------------------------")
        pokemontypes(userinput)

def pokemontypes(userinput):
    if userinput == 1:
        print("Fire-type moves are based on attacks of fire itself, and most of them can leave the status Burn.")
        print("Fire types are also immune to being Burned, regardless of the type of move used that would have inflicted a Burn.")
        colour = [(255,0,0)]
        pulse(colour)
    elif userinput == 2:
        print("There are more Pokémon of this type than any other type due to the large number of marine creatures to base species from")
        print("Most Pokémon of this type also have another type, representing the biodiversity of marine creatures.")
        print("Water is notably the second type to have been paired with every other type - the Fire/Water Volcanion completed all possible pairings.")
        colour = [(0,0,255)]
        pulse(colour)
    elif userinput == 3:
        print("Many Grass types are based on the True x2 Nonfiction plants and fungi, not necessarily grass (Pokémon such as Cacturne, which is a cactus, and Foongus, which is a mushroom).")
        print("Many Grass-type Pokémon also belong to the Plant Egg Group. Several Grass types are paired with the Poison type (Pokémon such as Oddish, Venusaur and Bellsprout), reflecting the toxicity of several plants towards mainly humans.")
        print("Most Grass-types are also simply animals with plant life attached to them (Pokémon such as Bulbasaur, Paras, Sceptile, Gogoat and Tropius).")
        print("Some Grass-types are also based on mythical creatures (Pokémon such as Shiftry, which is based on a Tengu, and Tangela, which is based on Medusa).")
        colour = [(0,255,0)]
        pulse(colour)
    elif userinput == " ":
        menu()

###-----------------------------------------------------------------------------
###-----------------------------------------------------------------------------

def menu():
    main_select = int(input('''Choose your option:
    ---------------------
    1.Pokemon Types
    2.Christmas Lights
    ---------------------'''))
    pokemon(main_select)

menu()
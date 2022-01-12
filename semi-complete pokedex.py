import opc
import time
from time import sleep
client = opc.Client('localhost:7890')

red_colour = [(255,0,0)]
green_colour = [(0,255,0)]
blue_colour = [(0,0,255)]
fade_amount = 10

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def pulse(colour):
    fade_amount = 10
    leds = [(0,0,0)]*360
    for led in range(len(leds)): #for each of the 360 LEDs
        leds[led] = colour  #change the colour
        time.sleep(.00001)           #wait a minute
        client.put_pixels(leds)  #then reflect the change



#-----------------------------------------------------------------------------
#------------------------------Pokemon-Type-----------------------------------

def pokemon(main_select):
    print("-----------------------------------------------------------------------------")
    if main_select == 1:
        userinput = int(input('''Choose a Pokemon Type:
        ----------------------
        1.Normal
        2.Fire
        3.Water
        4.Grass
        5.Eletric
        6.Ice
        7.Fighting
        8.Poison
        9.Ground
        10.Flying
        ----------------------'''))
        print("-----------------------------------------------------------------------------")
        pokemontypes(userinput)

def pokemontypes(userinput):
    if userinput == 1:
        print("More moves are Normal type than any other type; however, many of these moves are status moves that don't inflict any damage.")
        print("Prior to Generation IV, all Normal-type moves that dealt damage were physical attacks; today, the majority of Normal attacks remain physical,")
        print("with only a few special-attacking Normal moves introduced plus a handful of previous attacks being changed to special-attacking.")
        print("Normal moves are widely distributed among the majority of species of Pokémon, with several capable of being learned by every species that can learn TMs and HMs, or Move Tutor moves.")
        print("-----------------------------------------------------------------------------")
        colour = (157,149,131)
        pulse(colour)
    elif userinput == 2:
        print("Fire-type moves are based on attacks of fire itself, and most of them can leave the status Burn.")
        print("Fire types are also immune to being Burned, regardless of the type of move used that would have inflicted a Burn.")
        print("-----------------------------------------------------------------------------")
        colour = (238,59,45)
        pulse(colour)
    elif userinput == 3:
        print("There are more Pokémon of this type than any other type due to the large number of marine creatures to base species from")
        print("Most Pokémon of this type also have another type, representing the biodiversity of marine creatures.")
        print("Water is notably the second type to have been paired with every other type - the Fire/Water Volcanion completed all possible pairings.")
        print("-----------------------------------------------------------------------------")
        colour = (52,137,251)
        pulse(colour)
    elif userinput == 4:
        print("Many Grass types are based on the True x2 Nonfiction plants and fungi, not necessarily grass (Pokémon such as Cacturne, which is a cactus, and Foongus, which is a mushroom).")
        print("Many Grass-type Pokémon also belong to the Plant Egg Group. Several Grass types are paired with the Poison type (Pokémon such as Oddish, Venusaur and Bellsprout), reflecting the toxicity of several plants towards mainly humans.")
        print("Most Grass-types are also simply animals with plant life attached to them (Pokémon such as Bulbasaur, Paras, Sceptile, Gogoat and Tropius).")
        print("Some Grass-types are also based on mythical creatures (Pokémon such as Shiftry, which is based on a Tengu, and Tangela, which is based on Medusa).")
        print("-----------------------------------------------------------------------------")
        colour = (110,197,71)
        pulse(colour)
    elif userinput == 5:
        print("Electric-type Pokémon have varied habitats, from forests, prairies, cities and power plants.")
        print("Electric-type Pokémon are usually fast, and many of their attacks may paralyze the target.")
        print("Some Electric-type Pokémon also resemble artificial objects used by humans that can relate to electricity (the Magnemite and Voltorb evolution lines and Rotom).")
        print("-----------------------------------------------------------------------------")
        colour = (0,26,79,1)
        pulse(colour)
    elif userinput == 6:
        print("Ice-type Pokémon stand out for being able to endure very low temperatures, as well as adapting to freezing weathers. They control ice at will.")
        print("heir habitats go from the top of mountains, frozen caves and caverns or even the poles.")
        print("Many Ice-type moves have chances of freezing the target, which prevents them from attacking until they thaw out.")
        print("-----------------------------------------------------------------------------")
        colour = (82,196,222)
        pulse(colour)
    elif userinput == 7:
        print("Most Fighting-type Pokémon have a human-like body shape because they represent practitioners of various martial arts, which tend to be real-world humans.")
        print("Some Fighting-type Pokémon are represented by looking like fighters (Machamp looks like a bodybuilder and Crabrawler looks like a French-wrestler)")
        print("while other are represented by being based on a certain type of fighting style (Hitmontop is based on capoeira fighting and Gallade is based on sword-fighting).")
        print("A considerable number of Fighting-type Pokémon are predominantly or exclusively male.")
        print("-----------------------------------------------------------------------------")
        colour = (144,63,47)
        pulse(colour)
    elif userinput == 8:
        print("These Pokémon have a natural toxic quality; some directly represent real-world species known for their venom, such as snakes, and some even represent pollution itself.")
        print("They normally live in caves, marshes or similar places.")
        print("Most Poison-type Pokémon are based on poisonous or venomous animals")
        print("Most dual Poison-type Pokémon have Bug type or Grass type as their other type. This reflects how, in real life, many insects and plants are poisonous or venomous.")
        print("-----------------------------------------------------------------------------")
        colour = (163,68,147)
        pulse(colour)
    elif userinput == 9:
        print("Ground-type Pokémon have powers and abilities related to control of ground and earth.")
        print("Ground-type Pokémon are afraid of water, like Rock-type Pokémon, unless they are Water type.")
        print("Many Ground Pokémon are also partially Rock type.")
        print("These Pokémon are normally found in caves or rocky terrains, with the exceptions of some dual typed Pokémon.")
        print("-----------------------------------------------------------------------------")
        colour = (173,138,63)
        pulse(colour)
    elif userinput == 10:
        print("Pokémon of this type can fly, many of them live at high altitudes, even. Most of them are based on birds and insects.")
        print("Their power is mostly related with aerial and wind-related moves.")
        print("Most of them have wings, but there are also some of them that just float without wings, like Rayquaza and Gyarados.")
        print("Flying has been paired with every other Pokémon type to create a species; the introduction of Fighting/Flying Hawlucha completed all possible pairings.")
        print("-----------------------------------------------------------------------------")
        colour = (140,156,242)
        pulse(colour)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def menu():
    main_select = int(input('''Choose your option:
    ---------------------
    1.Pokemon Types
    2.Christmas Lights
    ---------------------'''))
    pokemon(main_select)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


menu()
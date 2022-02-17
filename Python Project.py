import tkinter as tk
from tkinter import *
from tkinter import ttk
import opc
import time
import random

leds = [(0,0,0)]*360 #white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

window = tk.Tk()
processdone = 0

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def pulseflash(colour):

    #This function loads the colour in one led at a time, then once the entire
    #list is filled out, it'll flash twice to signify that it's complete

    leds = [(0,0,0)]*360
    for led in range(len(leds)): #for each of the 360 LEDs
        leds[led] = colour       #change the colour
        time.sleep(.00001)       #wait a minute
        client.put_pixels(leds)  #then reflect the change
    if leds[200] == colour:
        for n in range(2):                  #Repeat two times
            pitchblack = [(0,0,0)]*360      #Show a completley black screen
            client.put_pixels(pitchblack)
            time.sleep(.5)
            client.put_pixels(leds)         #Then put out a completely coloured screen
            time.sleep(.5)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def pokeballshake():
    for x in range(random.randint(4,6)):                                        #For a random amount of times between 4 and 6
        leds = [(0,0,0)]*360
#--------------------------------------------Row One Red
        leds[25] = (255,0,0)
        leds[26] = (255,0,0)
        leds[27] = (255,0,0)
        leds[28] = (255,0,0)
        leds[29] = (255,0,0)
        leds[30] = (255,0,0)
        leds[31] = (255,0,0)
        leds[32] = (255,0,0)
        leds[33] = (255,0,0)
        leds[34] = (255,0,0)
#--------------------------------------------Row Two Red
        leds[83] = (255,0,0)
        leds[84] = (255,0,0)
        leds[85] = (255,0,0)
        leds[86] = (255,0,0)
        leds[87] = (255,0,0)
        leds[92] = (255,0,0)
        leds[93] = (255,0,0)
        leds[94] = (255,0,0)
        leds[95] = (255,0,0)
        leds[96] = (255,0,0)
#--------------------------------------------Row Three
        leds[142] = (255,0,0)
        leds[143] = (255,0,0)
        leds[144] = (255,0,0)
        leds[145] = (255,0,0)
        leds[146] = (255,0,0)
        leds[149] = (255,255,255)
        leds[150] = (255,255,255)
        leds[153] = (255,0,0)
        leds[154] = (255,0,0)
        leds[155] = (255,0,0)
        leds[156] = (255,0,0)
        leds[157] = (255,0,0)
#-------------------------------------------Row Four
        leds[202] = (255,255,255)
        leds[203] = (255,255,255)
        leds[204] = (255,255,255)
        leds[205] = (255,255,255)
        leds[206] = (255,255,255)
        leds[209] = (255,255,255)
        leds[210] = (255,255,255)
        leds[213] = (255,255,255)
        leds[214] = (255,255,255)
        leds[215] = (255,255,255)
        leds[216] = (255,255,255)
        leds[217] = (255,255,255)
#-------------------------------------------Row Five
        leds[263] = (255,255,255)
        leds[264] = (255,255,255)
        leds[265] = (255,255,255)
        leds[266] = (255,255,255)
        leds[267] = (255,255,255)
        leds[272] = (255,255,255)
        leds[273] = (255,255,255)
        leds[274] = (255,255,255)
        leds[275] = (255,255,255)
        leds[276] = (255,255,255)
#-------------------------------------------Row Six
        leds[325] = (255,255,255)
        leds[326] = (255,255,255)
        leds[327] = (255,255,255)
        leds[328] = (255,255,255)
        leds[329] = (255,255,255)
        leds[330] = (255,255,255)
        leds[331] = (255,255,255)
        leds[332] = (255,255,255)
        leds[333] = (255,255,255)
        leds[334] = (255,255,255)
        client.put_pixels(leds)

        time.sleep(0.3)
                                                                                #Animate the original pokeball, then animate it to move slightly left.
        leds = [(0,0,0)]*360
#--------------------------------------------Row One Red
        leds[26] = (255,0,0)
        leds[27] = (255,0,0)
        leds[28] = (255,0,0)
        leds[29] = (255,0,0)
        leds[30] = (255,0,0)
        leds[31] = (255,0,0)
        leds[32] = (255,0,0)
        leds[33] = (255,0,0)
        leds[34] = (255,0,0)
        leds[35] = (255,0,0)
#--------------------------------------------Row Two Red
        leds[84] = (255,0,0)
        leds[85] = (255,0,0)
        leds[86] = (255,0,0)
        leds[87] = (255,0,0)
        leds[88] = (255,0,0)
        leds[93] = (255,0,0)
        leds[94] = (255,0,0)
        leds[95] = (255,0,0)
        leds[96] = (255,0,0)
        leds[97] = (255,0,0)
#--------------------------------------------Row Three
        leds[143] = (255,0,0)
        leds[144] = (255,0,0)
        leds[145] = (255,0,0)
        leds[146] = (255,0,0)
        leds[147] = (255,0,0)
        leds[150] = (255,255,255)
        leds[151] = (255,255,255)
        leds[154] = (255,0,0)
        leds[155] = (255,0,0)
        leds[156] = (255,0,0)
        leds[157] = (255,0,0)
        leds[158] = (255,0,0)
#-------------------------------------------Row Four
        leds[203] = (255,255,255)
        leds[204] = (255,255,255)
        leds[205] = (255,255,255)
        leds[206] = (255,255,255)
        leds[207] = (255,255,255)
        leds[210] = (255,255,255)
        leds[211] = (255,255,255)
        leds[214] = (255,255,255)
        leds[215] = (255,255,255)
        leds[216] = (255,255,255)
        leds[217] = (255,255,255)
        leds[218] = (255,255,255)
#-------------------------------------------Row Five
        leds[264] = (255,255,255)
        leds[265] = (255,255,255)
        leds[266] = (255,255,255)
        leds[267] = (255,255,255)
        leds[268] = (255,255,255)
        leds[273] = (255,255,255)
        leds[274] = (255,255,255)
        leds[275] = (255,255,255)
        leds[276] = (255,255,255)
        leds[277] = (255,255,255)
#-------------------------------------------Row Six
        leds[326] = (255,255,255)
        leds[327] = (255,255,255)
        leds[328] = (255,255,255)
        leds[329] = (255,255,255)
        leds[330] = (255,255,255)
        leds[331] = (255,255,255)
        leds[332] = (255,255,255)
        leds[333] = (255,255,255)
        leds[334] = (255,255,255)
        leds[335] = (255,255,255)
        client.put_pixels(leds)

        time.sleep(0.3)
                                                                                #Animate the pokeball to the left, then move it back to the middle.
        leds = [(0,0,0)]*360
#--------------------------------------------Row One Red
        leds[27] = (255,0,0)
        leds[28] = (255,0,0)
        leds[29] = (255,0,0)
        leds[30] = (255,0,0)
        leds[31] = (255,0,0)
        leds[32] = (255,0,0)
        leds[33] = (255,0,0)
        leds[34] = (255,0,0)
        leds[35] = (255,0,0)
        leds[36] = (255,0,0)
#--------------------------------------------Row Two Red
        leds[85] = (255,0,0)
        leds[86] = (255,0,0)
        leds[87] = (255,0,0)
        leds[88] = (255,0,0)
        leds[89] = (255,0,0)
        leds[94] = (255,0,0)
        leds[95] = (255,0,0)
        leds[96] = (255,0,0)
        leds[97] = (255,0,0)
        leds[98] = (255,0,0)
#--------------------------------------------Row Three
        leds[144] = (255,0,0)
        leds[145] = (255,0,0)
        leds[146] = (255,0,0)
        leds[147] = (255,0,0)
        leds[148] = (255,0,0)
        leds[151] = (255,255,255)
        leds[152] = (255,255,255)
        leds[155] = (255,0,0)
        leds[156] = (255,0,0)
        leds[157] = (255,0,0)
        leds[158] = (255,0,0)
        leds[159] = (255,0,0)
#-------------------------------------------Row Four
        leds[204] = (255,255,255)
        leds[205] = (255,255,255)
        leds[206] = (255,255,255)
        leds[207] = (255,255,255)
        leds[208] = (255,255,255)
        leds[211] = (255,255,255)
        leds[212] = (255,255,255)
        leds[215] = (255,255,255)
        leds[216] = (255,255,255)
        leds[217] = (255,255,255)
        leds[218] = (255,255,255)
        leds[219] = (255,255,255)
#-------------------------------------------Row Five
        leds[265] = (255,255,255)
        leds[266] = (255,255,255)
        leds[267] = (255,255,255)
        leds[268] = (255,255,255)
        leds[269] = (255,255,255)
        leds[274] = (255,255,255)
        leds[275] = (255,255,255)
        leds[276] = (255,255,255)
        leds[277] = (255,255,255)
        leds[278] = (255,255,255)
#-------------------------------------------Row Six
        leds[327] = (255,255,255)
        leds[328] = (255,255,255)
        leds[329] = (255,255,255)
        leds[330] = (255,255,255)
        leds[331] = (255,255,255)
        leds[332] = (255,255,255)
        leds[333] = (255,255,255)
        leds[334] = (255,255,255)
        leds[335] = (255,255,255)
        leds[336] = (255,255,255)
        client.put_pixels(leds)

        time.sleep(0.3)
                                                                                #Then once it's centred, move it to the right.
        leds = [(0,0,0)]*360
#--------------------------------------------Row One Red
        leds[26] = (255,0,0)
        leds[27] = (255,0,0)
        leds[28] = (255,0,0)
        leds[29] = (255,0,0)
        leds[30] = (255,0,0)
        leds[31] = (255,0,0)
        leds[32] = (255,0,0)
        leds[33] = (255,0,0)
        leds[34] = (255,0,0)
        leds[35] = (255,0,0)
#--------------------------------------------Row Two Red
        leds[84] = (255,0,0)
        leds[85] = (255,0,0)
        leds[86] = (255,0,0)
        leds[87] = (255,0,0)
        leds[88] = (255,0,0)
        leds[93] = (255,0,0)
        leds[94] = (255,0,0)
        leds[95] = (255,0,0)
        leds[96] = (255,0,0)
        leds[97] = (255,0,0)
#--------------------------------------------Row Three
        leds[143] = (255,0,0)
        leds[144] = (255,0,0)
        leds[145] = (255,0,0)
        leds[146] = (255,0,0)
        leds[147] = (255,0,0)
        leds[150] = (255,255,255)
        leds[151] = (255,255,255)
        leds[154] = (255,0,0)
        leds[155] = (255,0,0)
        leds[156] = (255,0,0)
        leds[157] = (255,0,0)
        leds[158] = (255,0,0)
#-------------------------------------------Row Four
        leds[203] = (255,255,255)
        leds[204] = (255,255,255)
        leds[205] = (255,255,255)
        leds[206] = (255,255,255)
        leds[207] = (255,255,255)
        leds[210] = (255,255,255)
        leds[211] = (255,255,255)
        leds[214] = (255,255,255)
        leds[215] = (255,255,255)
        leds[216] = (255,255,255)
        leds[217] = (255,255,255)
        leds[218] = (255,255,255)
#-------------------------------------------Row Five
        leds[264] = (255,255,255)
        leds[265] = (255,255,255)
        leds[266] = (255,255,255)
        leds[267] = (255,255,255)
        leds[268] = (255,255,255)
        leds[273] = (255,255,255)
        leds[274] = (255,255,255)
        leds[275] = (255,255,255)
        leds[276] = (255,255,255)
        leds[277] = (255,255,255)
#-------------------------------------------Row Six
        leds[326] = (255,255,255)
        leds[327] = (255,255,255)
        leds[328] = (255,255,255)
        leds[329] = (255,255,255)
        leds[330] = (255,255,255)
        leds[331] = (255,255,255)
        leds[332] = (255,255,255)
        leds[333] = (255,255,255)
        leds[334] = (255,255,255)
        leds[335] = (255,255,255)
        client.put_pixels(leds)
                                                                                #Then since it loops, the loop starts
                                                                                #over and it'll be back in the middle
        time.sleep(0.3)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

def pokeball():
#--------------------------------------------Row One Red
    leds[26-20] = (255,0,0)
    leds[27-20] = (0,0,255)
    leds[28-20] = (0,0,255)
    leds[29-20] = (0,0,255)
    leds[30-20] = (0,0,255)
    leds[31-20] = (0,0,255)
    leds[32-20] = (0,0,255)
    leds[33-20] = (0,0,255)
    leds[34-20] = (0,0,255)
    leds[35-20] = (255,0,0)
#--------------------------------------------Row Two Red
    leds[84-20] = (0,0,255)
    leds[85-20] = (255,0,0)
    leds[86-20] = (255,0,0)
    leds[87-20] = (255,0,0)
    leds[88-20] = (255,0,0)
    leds[93-20] = (255,0,0)
    leds[94-20] = (255,0,0)
    leds[95-20] = (255,0,0)
    leds[96-20] = (255,0,0)
    leds[97-20] = (0,0,255)
#--------------------------------------------Row Three
    leds[143-20] = (0,0,255)
    leds[144-20] = (0,0,255)
    leds[145-20] = (0,0,255)
    leds[146-20] = (0,0,255)
    leds[147-20] = (255,0,0)
    leds[150-20] = (255,255,255)
    leds[151-20] = (255,255,255)
    leds[154-20] = (255,0,0)
    leds[155-20] = (0,0,255)
    leds[156-20] = (0,0,255)
    leds[157-20] = (0,0,255)
    leds[158-20] = (0,0,255)
#-------------------------------------------Row Four
    leds[203-20] = (255,255,255)
    leds[204-20] = (255,255,255)
    leds[205-20] = (255,255,255)
    leds[206-20] = (255,255,255)
    leds[207-20] = (255,255,255)
    leds[210-20] = (255,255,255)
    leds[211-20] = (255,255,255)
    leds[214-20] = (255,255,255)
    leds[215-20] = (255,255,255)
    leds[216-20] = (255,255,255)
    leds[217-20] = (255,255,255)
    leds[218-20] = (255,255,255)
#-------------------------------------------Row Five
    leds[264-20] = (255,255,255)
    leds[265-20] = (255,255,255)
    leds[266-20] = (255,255,255)
    leds[267-20] = (255,255,255)
    leds[268-20] = (255,255,255)
    leds[273-20] = (255,255,255)
    leds[274-20] = (255,255,255)
    leds[275-20] = (255,255,255)
    leds[276-20] = (255,255,255)
    leds[277-20] = (255,255,255)
#-------------------------------------------Row Six
    leds[326-20] = (255,255,255)
    leds[327-20] = (255,255,255)
    leds[328-20] = (255,255,255)
    leds[329-20] = (255,255,255)
    leds[330-20] = (255,255,255)
    leds[331-20] = (255,255,255)
    leds[332-20] = (255,255,255)
    leds[333-20] = (255,255,255)
    leds[334-20] = (255,255,255)
    leds[335-20] = (255,255,255)
    client.put_pixels(leds)

#-----------------------------------------------------------------------------
#------------------------------Pokemon-Type-----------------------------------

def pokedex():
    def pokedexwipe():
                                                                                #Functioned used to remove all the buttons after a choice has been selected.
        choosepokemon.pack_forget()
        normal.pack_forget()
        fire.pack_forget()
        water.pack_forget()
        grass.pack_forget()
        electric.pack_forget()
        ice.pack_forget()
        fighting.pack_forget()
        poison.pack_forget()
        ground.pack_forget()
        flying.pack_forget()

    choosepokemon = tk.Label(text = '''
    Choose a Pokemon Type''')
    choosepokemon.pack()

    normal = Button(window, text ="Normal", command = lambda:[pokedexwipe(),normaltype()])
    normal.pack()
    fire = tk.Button(window, text = "Fire", command = lambda:[pokedexwipe(),firetype()])
    fire.pack()
    water = tk.Button(window, text = "Water", command = lambda:[pokedexwipe(),watertype()])
    water.pack()
    grass = tk.Button(window, text ="Grass", command = lambda:[pokedexwipe(),grasstype()])
    grass.pack()
    electric = tk.Button(window, text ="Electric", command = lambda:[pokedexwipe(),electrictype()])
    electric.pack()
    ice = tk.Button(window, text ="Ice", command = lambda:[pokedexwipe(),icetype()])
    ice.pack()
    fighting = tk.Button(window, text ="Fighting", command = lambda:[pokedexwipe(),fightingtype()])
    fighting.pack()
    poison = tk.Button(window, text ="Posion", command = lambda:[pokedexwipe(),poisontype()])
    poison.pack()
    ground = tk.Button(window, text ="Ground", command = lambda:[pokedexwipe(),groundtype()])
    ground.pack()
    flying = tk.Button(window, text ="Flying", command = lambda:[pokedexwipe(),flyingtype()])
    flying.pack()
    print("-----------------------------------------------------------------------------")


def normaltype():
    print('''More moves are Normal type than any other type; however, many of these moves are status moves that don't inflict any damage.
Prior to Generation IV, all Normal-type moves that dealt damage were physical attacks; today, the majority of Normal attacks remain physical,
with only a few special-attacking Normal moves introduced plus a handful of previous attacks being changed to special-attacking.
Normal moves are widely distributed among the majority of species of Pokémon, with several capable of being learned by every species that can learn TMs and HMs, or Move Tutor moves.
-----------------------------------------------------------------------------''')
    colour = (157,149,131)
    pulseflash(colour)
def firetype():
    print('''Fire-type moves are based on attacks of fire itself, and most of them can leave the status Burn.
Fire types are also immune to being Burned, regardless of the type of move used that would have inflicted a Burn.
-----------------------------------------------------------------------------''')
    colour = (238,59,45)
    pulseflash(colour)
def watertype():
    print('''There are more Pokémon of this type than any other type due to the large number of marine creatures to base species from,
Most Pokémon of this type also have another type, representing the biodiversity of marine creatures.
Water is notably the second type to have been paired with every other type - the Fire/Water Volcanion completed all possible pairings.
-----------------------------------------------------------------------------''')
    colour = (52,137,251)
    pulseflash(colour)
def grasstype():
    print('''Many Grass types are based on the True x2 Nonfiction plants and fungi, not necessarily grass (Pokémon such as Cacturne, which is a cactus, and Foongus, which is a mushroom)
Many Grass-type Pokémon also belong to the Plant Egg Group. Several Grass types are paired with the Poison type (Pokémon such as Oddish, Venusaur and Bellsprout), reflecting the toxicity of several plants towards mainly humans.
Most Grass-types are also simply animals with plant life attached to them (Pokémon such as Bulbasaur, Paras, Sceptile, Gogoat and Tropius)
Some Grass-types are also based on mythical creatures (Pokémon such as Shiftry, which is based on a Tengu, and Tangela, which is based on Medusa)
-----------------------------------------------------------------------------''')
    colour = (110,197,71)
    pulseflash(colour)
def electrictype():
    print('''Electric-type Pokémon have varied habitats, from forests, prairies, cities and power plants.
Electric-type Pokémon are usually fast, and many of their attacks may paralyze the target.
Some Electric-type Pokémon also resemble artificial objects used by humans that can relate to electricity (the Magnemite and Voltorb evolution lines and Rotom)
-----------------------------------------------------------------------------''')
    colour = (0,26,79,1)
    pulseflash(colour)
def icetype():
    print('''Ice-type Pokémon stand out for being able to endure very low temperatures, as well as adapting to freezing weathers. They control ice at will.
heir habitats go from the top of mountains, frozen caves and caverns or even the poles.
Many Ice-type moves have chances of freezing the target, which prevents them from attacking until they thaw out.
-----------------------------------------------------------------------------''')
    colour = (82,196,222)
    pulseflash(colour)
def fightingtype():
    print('''Most Fighting-type Pokémon have a human-like body shape because they represent practitioners of various martial arts, which tend to be real-world humans.
Some Fighting-type Pokémon are represented by looking like fighters (Machamp looks like a bodybuilder and Crabrawler looks like a French-wrestler)
while other are represented by being based on a certain type of fighting style (Hitmontop is based on capoeira fighting and Gallade is based on sword-fighting.
A considerable number of Fighting-type Pokémon are predominantly or exclusively male.
-----------------------------------------------------------------------------''')
    colour = (144,63,47)
    pulseflash(colour)
def poisontype():
    print('''These Pokémon have a natural toxic quality; some directly represent real-world species known for their venom, such as snakes, and some even represent pollution itself.
They normally live in caves, marshes or similar places. Most Poison-type Pokémon are based on poisonous or venomous animals.
Most dual Poison-type Pokémon have Bug type or Grass type as their other type. This reflects how, in real life, many insects and plants are poisonous or venomous.
-----------------------------------------------------------------------------''')
    colour = (163,68,147)
    pulseflash(colour)
def groundtype():
    print('''Ground-type Pokémon have powers and abilities related to control of ground and earth.
Ground-type Pokémon are afraid of water, like Rock-type Pokémon, unless they are Water type.
Many Ground Pokémon are also partially Rock type.
These Pokémon are normally found in caves or rocky terrains, with the exceptions of some dual typed Pokémon.
-----------------------------------------------------------------------------''')
    pack_forget()
    colour = (173,138,63)
    pulseflash(colour)
def flyingtype():
    print('''Pokémon of this type can fly, many of them live at high altitudes, even. Most of them are based on birds and insects.
Their power is mostly related with aerial and wind-related moves.
Most of them have wings, but there are also some of them that just float without wings, like Rayquaza and Gyarados.
Flying has been paired with every other Pokémon type to create a species; the introduction of Fighting/Flying Hawlucha completed all possible pairings.
-----------------------------------------------------------------------------''')
    colour = (140,156,242)
    pulseflash(colour)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def explosion(colour):
                                                                                #The First animation shows the initial explosion
    leds = [(0,0,0)]*360
    blue = 255
    leds = [(0,0,0)]*360
    leds[149] = colour
    leds[150] = colour
    leds[209] = colour
    leds[210] = colour
    client.put_pixels(leds)
    time.sleep(.001)
                                                                                #Then with each animation the pixels move further out
    leds = [(0,0,0)]*360
    leds[89] = colour
    leds[90] = colour
    leds[148] = colour
    leds[151] = colour
    leds[208] = colour
    leds[211] = colour
    leds[269] = colour
    leds[270] = colour
    client.put_pixels(leds)
    time.sleep(.001)
                                                                                #Then the pixels move even further outwards
    leds = [(0,0,0)]*360
    leds[29] = colour
    leds[30] = colour
    leds[88] = colour
    leds[91] = colour
    leds[147] = colour
    leds[152] = colour
    leds[207] = colour
    leds[212] = colour
    leds[268] = colour
    leds[271] = colour
    leds[329] = colour
    leds[330] = colour
    client.put_pixels(leds)
    time.sleep(.001)

    left = 1
    right = 1
    fadeleft = 1                                                                #Here variables are created to be itterated
                                                                                #on which move the pixels outwards from the
                                                                                #origin.
    faderight = 1
    count = 0

    leds = [(0,0,0)]*360
    for x in range(27):
        leds[29-left] = colour                                                  #27 times, the pixels will either move left or right
        leds[30+right] = colour                                                 #and the variables itterate at the end of each loop.
        leds[88-left] = colour
        leds[91+right] = colour
        leds[147-left] = colour
        leds[152+right] = colour
        leds[207-left] = colour
        leds[212+right] = colour
        leds[268-left] = colour
        leds[271+right] = colour
        leds[329-left] = colour
        leds[330+right] = colour
        left += 1
        right += 1
        client.put_pixels(leds)
        time.sleep(.0001)                                                       #With a small delay between each loop
        count +=1

        if left >= 4:                                                           #Also, with each loop after the fourth itteration,
            leds[29-fadeleft] = (0,0,0)                                         #the leds will chase after the previous loop.
            leds[30+faderight] = (0,0,0)                                        #However, this time it'll be black, which gives the
            leds[88-fadeleft] = (0,0,0)                                         #animation a blade-like effect.
            leds[91+faderight] = (0,0,0)
            leds[147-fadeleft] = (0,0,0)
            leds[152+faderight] = (0,0,0)
            leds[207-fadeleft] = (0,0,0)
            leds[212+faderight] = (0,0,0)
            leds[268-fadeleft] = (0,0,0)
            leds[271+faderight] = (0,0,0)
            leds[329-fadeleft] = (0,0,0)
            leds[330+faderight] = (0,0,0)
            fadeleft += 1
            faderight += 1
            client.put_pixels(leds)
            time.sleep(.0001)
    leds = [(0,0,0)]*360
    client.put_pixels(leds)


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def released():
    escape = tk.Label(window, text = '''
    It escaped into the high grass!''')
    escape.pack()
    blue = 255
    colour = (blue,blue,blue)
    leds = [colour]*60
    client.put_pixels(leds)
    time.sleep(.1)
    hibar = 1
    lobar = hibar + 1
    for x in range(5):
        leds = [(0,0,0)]*(60*hibar)
        client.put_pixels(leds)
        leds = [colour]*(60*lobar)
        client.put_pixels(leds)
        hibar += 1
        lobar = hibar + 1
        time.sleep(.05)
    for x in range(6):
        leds = [(0,blue,0)]*360
        client.put_pixels(leds)
        time.sleep(.1)
        blue = blue - 51


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def screenclear():                                                              #Presents a fully black screen, seemed more
    leds = [(0,0,0)]*(360)                                                      #organised to make it a function.

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def capture():
    pokeballshake()                                                             #First shake the pokeball,
    capturechance = random.randint(0,1)                                         #Then randomize whether it's caught or not
    if capturechance == 0:                                                      #If it's caught, play an explosion, clear the screen and congratulate the player.
        explosion((255,255,255))
        screenclear()
        congrats = tk.Label(
            window,
            text = '''You caught the Pokemon! Nice Work!''',
            width = 30,
            height = 2
        )
        congrats.pack()
        screenclear()
        time.sleep(.5)
    elif capturechance == 1:                                                    #If it isn't caught, play an animation and say the pokemon escaped.
        unlucky = tk.Label(
            window,
            text = '''The Pokemon got away, unlucky :<''',
            width = 30,
            height = 2
        )
        unlucky.pack()
        leds = [(255,0,0)]*360
        client.put_pixels(leds)
        time.sleep(.5)
        for x in range(4):
            leds = [(0,0,0)]*360
            client.put_pixels(leds)
            time.sleep(.1)
            leds = [(255,0,0)]*360
            client.put_pixels(leds)
            time.sleep(.1)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def emptyscan():
    blue = 255
    colour = (blue,blue,blue)
    leds = [colour]*60
    client.put_pixels(leds)
    time.sleep(.1)
    hibar = 1
    lobar = hibar + 1
    for x in range(5):
        leds = [(0,0,0)]*(60*hibar)
        client.put_pixels(leds)
        leds = [colour]*(60*lobar)
        client.put_pixels(leds)
        hibar += 1
        lobar = hibar + 1
        time.sleep(.05)
    for x in range(6):
        leds = [(blue,0,0)]*360
        client.put_pixels(leds)
        time.sleep(.1)
        blue = blue - 51

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def pokemoncatcherx():
    #Displaying a scanning animation
    #Functioned used to remove all the buttons after a choice has been selected.
    def pokecatchwipe():
        appearance.pack_forget()
        catch.pack_forget()
        release.pack_forget()
#Displaying a scanning animation
    #Gives the loading time a randomized value, as it is in the Pokemon games
    loading = random.randint(2,4)
    for i in range(loading*2):
        leds = [(0,0,0)]*360
        blue = 0
        speed = 0.01
        for led in range(60):

#Left Bar Animation
            leds[60] = (0,0,0)
            leds[led+59] = (0,0,0)
            leds[led+60] = (0,0,blue)
            leds[led+61] = (0,0,blue)
            leds[led+119] = (0,0,0)
            leds[led+120] = (0,0,blue)
            leds[led+121] = (0,0,blue)
            leds[led+179] = (0,0,0)
            leds[led+180] = (0,0,blue)
            leds[led+181] = (0,0,blue)
            leds[led+239] = (0,0,0)
            leds[led+240] = (0,0,blue)
            leds[led+241] = (0,0,blue)

#Right Bar Animation
            leds[118-led] = (0,0,blue)
            leds[119-led] = (0,0,blue)
            leds[120-led] = (0,0,0)
            leds[178-led] = (0,0,blue)
            leds[179-led] = (0,0,blue)
            leds[180-led] = (0,0,0)
            leds[238-led] = (0,0,blue)
            leds[239-led] = (0,0,blue)
            leds[240-led] = (0,0,0)
            leds[298-led] = (0,0,blue)
            leds[299-led] = (0,0,blue)
            leds[300-led] = (0,0,0)

            blue = blue + 2.5

            client.put_pixels(leds)     #place the latest frame on screen.
            time.sleep(speed)            #delay the frame a bit
    #This gives half a chance for the scanner to pick up on a pokemon, or not
    chance = random.randint(0,1)
    pokemon = ["Pikachu", "Charizard", "Blastoise", "Ivysaur", "Mew", "Mewtwo", "Arceus" , "Dialga", "Palkia"]

    if chance == 0:
        emptyscan()
        breather = tk.Label(
            window,
            text = '''Nothing appeared... Maybe take a break for a while, scanner off.''',
            width = 50,
            height = 2
        )
        breather.pack()

    elif chance == 1:
        appearance = tk.Label (
            window,
            text = "A Wild "+ pokemon[random.randint(0,8)] + " appeared!",
            width = 20,
            height = 2
        )
        appearance.pack()
        decide = tk.Frame()
        catch = tk.Button(window,
            text ="Catch it",
            command = lambda:[pokecatchwipe(),capture()],
            width = 8,
            height = 2,
            fg = "white",
            bg = "green"
        )
        release = tk.Button(
            window,
            text ="Release it",
            command = lambda:[pokecatchwipe(),released()],
            width = 8,
            height = 2,
            fg = "white",
            bg = "red"
        )
        catch.pack()
        release.pack()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

Credits = tk.Label(
    text = '''Jaden Gooding M00755XXX''',
    fg = "white",
    bg = "black",
    width = 40,
    height = 2
)
Title = tk.Label(
    text = '''Choose your option:''',
    width = 20,
    height = 2
)
Button1 = tk.Button(
    window,
    text = '''PokemonCatcher X''',
    command = pokemoncatcherx,
    fg = "white",
    bg = "blue",
    width = 20,
    height = 2
)
Button2 = tk.Button(
    window,
    text = '''Pokedex''',
    command = pokedex,
    fg = "white",
    bg = "blue",
    width = 20,
    height = 2
)
Button0 = tk.Button(
    window,
    text = '''Quit''',
    command = window.destroy,
    fg = "black",
    bg = "white",
    width = 20,
    height = 2
)

Credits.pack()
Title.pack()
Button1.pack()
Button2.pack()
Button0.pack()
window.mainloop()
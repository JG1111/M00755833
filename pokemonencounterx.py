import opc
import time
import random

leds = [(0,0,0)]*360 #white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def pokemoncatcherx():
    loading = random.randint(2,6)
    print("SCANNING FOR POKEMON IN THE SURROUNDING AREA...")
    for i in range(loading*2):
        leds = [(0,0,0)]*360                    #do this forever
        blue = 0
        speed = 0.01
        for led in range(60):

#Left Bar
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

# Right Bar
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
    print(" ")
    chance = random.randint(0,1)
    pokemon = "pikachu"
    if chance == 0:
        print("Nothing appeared...")
        print("Maybe take a break for a while, scanner off.")
        print(" ")

    elif chance == 1:
        print ("A wild " + pokemon + " appeared!")
        print(" ")
        action = int((input('''Catch it [1] or Let it Go [2]?!''')))
        if action == 1:
            print(" ")
            print("I haven't programmed this yet, give me some time...")
            print(" ")
            print(" ")
            pokemoncatcherx()
        elif action == 2:
            print(" ")
            print("the wild " + pokemon + " escaped into the high grass...")
            print(" ")
            print(" ")
            pokemoncatcherx()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
pokemoncatcherx()

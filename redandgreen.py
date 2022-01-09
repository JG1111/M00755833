import opc
import time
client = opc.Client('localhost:7890')

red_colour=[(255,0,0)]
green_colour=[(0,255,0)]
led_colour= (red_colour * 10) + (green_colour * 10)
print (enumerate(led_colour))




client.put_pixels(led_colour)

#need to send it twice if not constantly sending values
#due to interpolation setting on fadecandy




###print (led_colour)
#Require to use bitio, a micro:bit I/O library: https://github.com/whaleygeek/bitio
#This file and other supplements need to run in Raspberry Pi.
#This file needs to be put in the src file of the bitio library.
#Require to install mpd/mpc and some mp3 files to LXTerminal.
#Require to connect Raspberry Pi to a BBC micro:bit and a sound speaker.
#Not require the Internet and Bluetooth.

import microbit
import random
import time
import os

playing = True
microbit.display.scroll("Hi")   #Let users to know that juckbox is started.
order = random.randint(1,4) #Song number. Total 4 songs.
os.system("mpc play "+ str(order))  #For LXTerminal using. Require to install mpd/mpc first.
microbit.display.show(str(order))   #BBC microbit displays a number of a song which is playing now.

while playing:

    if microbit.button_a.was_pressed():
        print("To the previous song")   #Press button A to the previous song
        order = order-1
        if order <1:
           order = 4
        os.system("mpc play "+str(order))   #By using the BBC microbit, users can select a song from LXTerminal.
        microbit.display.show(str(order))

    if microbit.button_b.was_pressed():
        print("To the next song")   #Press button B to the next song
        order = order+1
        if order > 4:
           order = 1
        os.system("mpc play "+ str(order))
        microbit.display.show(str(order))

    if microbit.pin1.is_touched():
        print("Shuffle music")  #Touch pin1 to shuffle music.
        order = random.randint(1,4)
        os.system("mpc play "+ str(order))
        microbit.display.show(str(order))

    if microbit.pin0.is_touched():
        print("shutdown")   #Touch pin0 to shutdown.
        microbit.display.scroll("See you")
        playing = False #Interrupt playing music.

    time.sleep(0.8)

os.system("mpc stop")


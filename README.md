# Atmosmakers

## A Brief Description

Atmosmaker, this project, aims at helping people enhance a family atmosphere and strengthen their relationship. Atmosmakesr can be put in anywhere in users’ home. In this project, there is two separate parts. One is an inductive household nightlight and the other is a jukebox.

## Instructions

### About the inductive household nightlight

Inside of the inductive household nightlight, there is a light sensor connected to the BBC micro:bit, and it will measure the surrounding amount of light. After the surrounding light input in the light sensor, the BBC micro:bit will automatically be triggered to output the light from its LEDs by Python 3. When the light sensor detects a darker environment, the BBC micro:bit will output a higher light level, and vice versa.

### How to use the inductive household nightlight
when people use this inductive household nightlight in a dark walkway or a dark staircase, the nightlight will automatically light up to help people find their way and avoid an accident. For example, the inductive household nightlight can help people to find a way to a bathroom without hardly finding any light switch to turn on when they get up in midnight. 

Users can put two AAA batteries in the BBC micro:bit’s battery holder or use USB cable to supply the power to the nightlight. The night light will be activated directly without press any button as soon as it is plugged in. At the same time, night lights automatically adjust their own light according to the light intensity of the surrounding environment. If the light in the surrounding environment is bright, the nightlight will not shine but will show a dim pattern of  a heart. If users want to turn off the whole nightlight, they can simply unplug the power supply.

[To see the demonstration](https://vimeo.com/334234977)

### About the jukebox

Raspberry Pi connects to the BBC micro:bit and a JBL Flip 4 speaker. In this part of the project, the Raspberry Pi is like a computer containing several songs and the BBC micro:bit is like a remote controller controlling the playing order of songs and shutting down the jukebox. In order to customize a music playlist, the Raspberry Pi needs to install Music Player Daemon (MPD), which is a free and open server-side application for playing music, via LXTerminal. MPD is controlled by mpc which is a minimalist command line interface to MPD. When the MPD was installed, I used the mpc add command to add the mp3. In addition, Raspberry Pi also needs to download the bitio library so it will work. For building a remote controller, the BBC micro:bit is coded by Python 3. This code also connects with mpc, therefore, the BBC micro:bit can help users to select a song from the playlist in MPD in LXTerminal. Raspberry Pi connects to the JBL Flip 4 speaker via 3.5 mm phone jack in order to output sound.

### How to use the jukebox
When Raspberry Pi connects to the power supply and the jukebox is activated, users will see “Hi” displaying on the BBC micro:bit through LEDs and the first song is preset to be played randomly. The LEDs of the BBC micro:bit will display the number of the song which is playing now. Users can press the buttons of the micro:bit to switch songs. When users press A button, they will be led to the previous song. When they press B button, they will be led to the next song. In addition, when users touch pin1 on the BBC micro:bit, the playlist will shuffle and the music will be played at random again. When users touch pin0, they can shutdown the jukebox and will see the BBC micro:bit displaying “See you”.

[To see the demonstration](https://vimeo.com/334234344)


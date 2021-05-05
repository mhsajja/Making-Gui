from gpiozero import LED
from time import sleep
import tkinter.font
import RPi.GPIO as GPIO
from tkinter import *
GPIO.setmode(GPIO.BCM)


yellow = LED(18)
red = LED(22)
blue = LED(27)

                                             


window = Tk()
window.title("TOGGLE THE LED")
myFont = tkinter.font.Font(family = 'Calibri', size = 10, weight = "bold")


def toggleblue():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn BLUE LED on"
    else:
        blue.on()
        blueButton["text"] = "Turn BLUE LED off"

def toggleyellow():
    if yellow.is_lit:
        yellow.off()
        yellowButton["text"] = "Turn YELLOW LED on"
    else:
        yellow.on()
        yellowButton["text"] = "Turn YELLOW LED off"
        
def togglered():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn RED lED on"
    else:
        red.on()
        redButton["text"] = "Turn RED LED off"





blueButton = Button(window, text = 'Turn BLUE LED On', font = myFont, command = toggleblue, bg = 'blue', height = 1, width = 15)
blueButton.grid(row=3,column=1)

redButton = Button(window, text = 'Turn RED LED On', font = myFont, command = togglered, bg = 'red', height = 1, width = 15)
redButton.grid(row=1,column=0)

yellowButton = Button(window, text = 'Turn YELLOW LED On', font = myFont, command = toggleyellow, bg = 'yellow', height = 1, width = 15)
yellowButton.grid(row=1,column=3)
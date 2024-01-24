MORSE_TABEL = [

    ["A", [1, 2]],
    ["B", [2, 1, 1, 1]],
    ["C", [2, 1, 2, 1]],
    ["D", [2, 1, 1]],
    ["E", [1]],
    ["F", [1, 1, 2, 1]],
    ["G", [2, 2, 1]],
    ["H", [1, 1, 1, 1]],
    ["I", [1, 1]],
    ["J", [1, 2, 2, 2]],
    ["K", [2, 1, 2]],
    ["L", [1, 2, 1, 1]],
    ["M", [2, 2]],
    ["N", [2, 1]],
    ["O", [2, 2, 2]],
    ["P", [1, 2, 2, 1]],
    ["Q", [2, 2, 1, 2]],
    ["R", [1, 2, 1]],
    ["S", [1, 1, 1]],
    ["T", [2]],
    ["U", [1, 1, 2]],
    ["V", [1, 1, 1, 2]],
    ["W", [1, 2, 2]],
    ["X", [2, 1, 1, 2]],
    ["Y", [2, 1, 2, 2]],
    ["Z", [2, 2, 1, 1]],

]





TIME_LINE = 3

TIME_DOT = 6

TIME_BETWEEN = 2

TIME_AFTER = 10



from machine import Pin

from utime import sleep

#use unstable firmware of the w-version  !!!!

PIN_LED = 21

_led = Pin (PIN_LED, Pin.OUT)





def on(): #functie

    _led.on()

    

def off():

    _led.off()



def line():

    on()

    sleep(TIME_LINE)

    off()

    

    



def dot():

    on()

    sleep(TIME_DOT)

    off()

    

    

def morse2_led2(character):

    global MORSE_TABEL

    character = (ord(character) - 65)   # ascii waarde van character - 65 dan : A == 0 en B == 1 e.c.t

    list_item = MORSE_TABEL[character]

    list_item = list_item[1]

    for i in range(len(list_item)):

        print(list_item[i])

        if list_item[i] == 1:

            line()

            off()

            sleep(TIME_BETWEEN)

        

        elif list_item[i] == 2:

            dot()

            off()

            sleep(TIME_BETWEEN)

    sleep(TIME_AFTER)

    print("pause")



    

    

    

morse2_led2("H")

morse2_led2("A")

morse2_led2("L")

morse2_led2("L")

morse2_led2("O")

on()









    







    





    




from time import sleep
import panda
import threading

panda = panda.Panda()


def panda_live():
    while panda.is_alive:
        panda.panda_live()
        # if panda.food <= 0:
        #     panda.is_alive = False
        # if panda.happiness <= 0:
        #     panda.is_alive = False
        if panda.tired >= 100:
            panda.is_tired = True
        if panda.food <= 50:
            panda.is_hungry = True
        if panda.happiness <= 50:
            panda.is_bored = True
        if panda.tired <= 50:
            panda.is_tired = False
        if panda.happiness >= 50:
            panda.is_happy = True
        if panda.food >= 50:
            panda.is_hungry = False
        # Sleep for 1 second

        sleep(1)
# Ayanabha
from gui_part import *


def slelect_random_word():
    import random

    myWords = []
    myWords2 = {"india": "country", "ferrari": "car"}
    list = ["india", "ferrari"]

    random_items = random.choice(list)
    print(myWords2[random_items])
    pass


def check_score():
    pass  # returns score (how many times won,lost)


def check_letter():
    pass  # returns true when letter in word else returns false


def check_rem_attempts():
    pass  # returns remaining no of attempts


def main():
    pass  # main game(loop)


# call take_input when input is required no need to define it it is defined in gui_part
a = slelect_random_word()

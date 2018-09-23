from array import *
import random
import webbrowser

dawnglare = "http://pad.dawnglare.com/?height=6&width=7&patt="

def generate_board():
    poison_pos = random.sample(range(0,42), 12)
    print poison_pos
    board = ''

    for orb in range(0, 42):
        if orb in poison_pos:
            board += 'P'
        else:
            board += 'G'
    return dawnglare+board

webbrowser.open_new(generate_board())



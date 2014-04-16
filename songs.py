import piano
import pyglet
#from pyglet.window import key
import time
clocks = [101,117,103,101,117,103,101,117,119,117,102,97,117,116,119,117,119,117,102,119,117,102,119,117,97,121,102,97,121,102,97,121]
def play_song(somelist):
    if not somelist:
        return
    piano.on_key_press(somelist[0],0)
    time.sleep(.17)
    return play_song(somelist[1:])
#play_song(clocks)
#play_song(clocks)
#play_song(clocks)
#play_song(clocks)

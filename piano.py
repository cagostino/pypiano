import pyglet
from pyglet.window import key
from pyglet import image
import time
regular_notes = ['c4.wav','d4.wav','e4.wav','f4.wav','g4.wav','a4.wav','b4.wav','c5.wav']
sharps = ['c#.wav','d#.wav','f#.wav','g#.wav','a#.wav']
los_keys = ['white-key.png', 'white-key-down.png', 'black-key.png', 'black-key-down.png']

white = pyglet.resource.image(los_keys[0])
white_down = pyglet.resource.image(los_keys[1])
black = pyglet.resource.image(los_keys[2])
black_down =pyglet.resource.image(los_keys[3])

window = pyglet.window.Window(8*white.width, white.height)
class Piano(object):
    def __init__(self, natural_notes, sharp_notes):
        self.natural_notes = natural_notes
        self.sharp_notes = sharp_notes
    def play_piano(self):
        """This function contains all the regular piano functions."""
        def draw_regular_down(index_key):
            """This draws whichever regular key has been pressed down"""
            @window.event
            def on_draw():
                window.clear()
                for i in range(len(self.natural_notes)):
                    if i == index_key:
                        white_down.blit(i*white.width,0)
                    else:
                        white.blit(i*white.width,0)
                for i in range(len(self.sharp_notes)):
                    if i <2:
                        black.blit(i*white.width+3*white.width/4,117)
                    else:
                        black.blit(i*white.width+7*white.width/4,117)
        def draw_sharp_down(index_key):
            """This draws whichever sharp key has been pressed down"""
            @window.event
            def on_draw():
                window.clear()
                for i in range(len(self.natural_notes)):
                    white.blit(i*white.width,0)
                for i in range(len(self.sharp_notes)):
                    if i == index_key and i <2:
                            black_down.blit(3*white.width/4 +white.width*i,117)
                    elif i == index_key:
                        black_down.blit(7*white.width/4+white.width*i,117)
                    elif i<2:
                        black.blit(i*white.width+3*white.width/4,117)
                    else:
                        black.blit(i*white.width+7*white.width/4,117)
        def draw_board():
            """ This homie just draws the initial board."""
            @window.event
            def on_draw():
                window.clear()  
                for i in range(len(self.natural_notes)):
                    white.blit(i*white.width,0)
                for i in range(len(self.sharp_notes)):
                    if i >= 2:
                        black.blit(7*white.width/4.+i*white.width,117 )
                    else:
                        black.blit(3*white.width/4 + white.width*i,117)
        draw_board()
        def play_song(self,somelist):
            """Given some arbitrary list of key combos it can play a simple piano tune."""
            if not somelist:
                return
            on_key_press(somelist[0],0)
            time.sleep(.19)
            return play_song(self,somelist[1:])
        play_song(self,clocks)
        @window.event
        def on_key_press(symbol, modifiers):
            useful_regular_keys = [key.A,key.S, key.E, key.D, key.F, key.G, key.H, key.J, key.K]
            useful_sharp_keys = [key.W, key.E, key.T, key.Y, key.U]
            if symbol in useful_regular_keys:
                draw_regular_down(useful_regular_keys.index(symbol))
                pyglet.resource.media(self.natural_notes[useful_regular_keys.index(symbol)])
            if symbol in useful_sharp_keys:
                draw_sharp_down(useful_sharp_keys.index(symbol))
                pyglet.resource.media(self.natural_notes[useful_sharp_keys.index(symbol)])
        @window.event
        def on_key_release(symbol, modifiers):
            """This function redraws the board after a key has been released so it looks normal again"""
            useful_keys = [key.A, key.S, key.W, key.E, key.D, key.F,key.G,key.T,key.H,key.Y,key.U,key.J, key.K]
            if symbol in useful_keys:
                draw_board()
        
clocks = [101,117,103,101,117,103,101,117,119,117,102,97,117,116,119,117,119,117,102,119,117,102,119,117,97,121,102,97,121,102,97,121]
new_piano = Piano(regular_notes, sharps)
new_piano.play_piano()
pyglet.app.run()

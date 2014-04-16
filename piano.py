import pyglet
from pyglet.window import key
from pyglet import image
import time
regular_notes = {'a': 'a4.wav','b':'b4.wav','c4':'c4.wav','d':'d4.wav','e':'e4.wav','f':'f4.wav','g':'g4.wav','c5':'c5.wav'}
sharps = {'asharp':'a#.wav','csharp':'c#.wav','dsharp':'d#.wav','fsharp':'f#.wav','gsharp':'g#.wav'}
los_keys = ['white-key.png', 'white-key-down.png', 'black-key.png', 'black-key-down.png']

white = pyglet.resource.image(los_keys[0])
white_down = pyglet.resource.image(los_keys[1])
black = pyglet.resource.image(los_keys[2])
black_down =pyglet.resource.image(los_keys[3])
window= pyglet.window.Window(8*white.width,white.height)

@window.event
def on_draw():
    window.clear()  
    for i in range(len(regular_notes.keys())):
        white.blit(i*white.width,0)

    for i in range(len(sharps.keys())):
        if i >= 2:
            black.blit(7*white.width/4.+i*white.width,117 )
        else:
            black.blit(3*white.width/4 + white.width*i,117)
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        pyglet.resource.media(regular_notes['c4']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==0:
                    white_down.blit(0,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)

    if symbol == key.W:
        pyglet.resource.media(sharps['csharp']).play()
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >=2:
                    black.blit(7*white.width/4.+i*white.width,117)
                elif i==0:
                    black_down.blit(3*white.width/4,117)
                else:
                    black.blit(3*white.width/4+white.width*i,117)
    if symbol == key.S:
        pyglet.resource.media(regular_notes['d']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==1:
                    white_down.blit(white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.E:
        pyglet.resource.media(sharps['dsharp']).play()
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >=2:
                    black.blit(7*white.width/4.+i*white.width,117)
                elif i==1:
                    black_down.blit(3*white.width/4+i*white.width,117)
                else:
                    black.blit(3*white.width/4+white.width*i,117)
    if symbol == key.D:
        pyglet.resource.media(regular_notes['e']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==2:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.F:
        pyglet.resource.media(regular_notes['f']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==3:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.T:
        pyglet.resource.media(sharps['fsharp']).play()
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >2:
                    black.blit(7*white.width/4.+i*white.width,117)
                elif i==2:
                    black_down.blit(7*white.width/4+i*white.width,117)
                else:
                    black.blit(3*white.width/4+white.width*i,117)
    if symbol == key.G:
        pyglet.resource.media(regular_notes['g']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==4:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.Y:
        pyglet.resource.media(sharps['gsharp']).play()
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i <2:
                    black.blit(3*white.width/4.+i*white.width,117)
                elif i==3:
                    black_down.blit(7*white.width/4+i*white.width,117)
                else:
                    black.blit(7*white.width/4+white.width*i,117)
    if symbol == key.H:
        pyglet.resource.media(regular_notes['a']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==5:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)

            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.U:
        pyglet.resource.media(sharps['asharp']).play()
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i <2:
                    black.blit(3*white.width/4.+i*white.width,117)
                elif i==4:
                    black_down.blit(7*white.width/4+i*white.width,117)
                else:
                    black.blit(7*white.width/4+white.width*i,117)
    if symbol == key.J:
        pyglet.resource.media(regular_notes['b']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==6:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
    if symbol == key.K:
        pyglet.resource.media(regular_notes['c5']).play()
        @window.event
        def on_draw():
            window.clear()
            for i in range(len(regular_notes.keys())):
                if i ==7:
                    white_down.blit(i*white.width,0)
                else:
                    white.blit(i*white.width,0)
            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)
@window.event
def on_key_release(symbol, modifiers):
    useful_keys = [key.A, key.S, key.W, key.E, key.D, key.F,key.G,key.T,key.H,key.Y,key.U,key.J, key.K]
    if symbol in useful_keys:
        @window.event
        def on_draw():
            window.clear()  
            for i in range(len(regular_notes.keys())):
                white.blit(i*white.width,0)

            for i in range(len(sharps.keys())):
                if i >= 2:
                    black.blit(7*white.width/4.+i*white.width,117 )
                else:
                    black.blit(3*white.width/4 + white.width*i,117)    
clocks = [101,117,103,101,117,103,101,117,119,117,102,97,117,116,119,117,119,117,102,119,117,102,119,117,97,121,102,97,121,102,97,121]
def play_song(somelist):
    if not somelist:
        return
    on_key_press(somelist[0],0)
    time.sleep(.19)
    return play_song(somelist[1:])

pyglet.app.run()

play_song(clocks)
play_song(clocks)
play_song(clocks)
play_song(clocks)

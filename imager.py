import pyglet
import random

window = pyglet.window.Window()
image = pyglet.resource.image('1.jpg')

@window.event
def on_draw():
	window.clear()
	image.blit(0, 0)

pyglet.app.run()

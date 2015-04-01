import pygame
from pygame import *
from random import Random
import random
import time
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._randnum = random.Random()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((700,25), pygame.NOFRAME)
        self._running = True
	self._RECT = self.slider()
        #self._image_surf = pygame.image.load("myimage.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def slider(self):
	x = 0
	y = 0
	a = 0
	b = 0
	return [0,0,400,30]

    def on_render(self):
	lr = self._randnum
	event = pygame.event.poll()
        pygame.draw.rect(self._display_surf, (200, lr.randint(1,30), 220), self._RECT)
	#self._display_surf.blit()
        pygame.display.flip()
	pygame.display.update()
	self._display_surf.fill((0,249,80))
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
	    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
		self._RECT[2], y = event.pos
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

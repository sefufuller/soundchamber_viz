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
        self._display_surf = pygame.display.set_mode((700,400), pygame.NOFRAME)
        self._running = True
        #self._image_surf = pygame.image.load("myimage.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
	lr = self._randnum
        pygame.draw.lines(self._display_surf, (lr.randint(203, 244),lr.randint(2, 200),lr.randint(1, 80)), False, [(lr.randint(1,100), lr.randint(53, 60)), (lr.randint(105, 905), lr.randint(3,440)), (lr.randint(33, 630), 80), (lr.randint(300,899), 80)], 1)
        time.sleep(.5)
	#self._display_surf.blit()
        pygame.display.flip()
	pygame.display.update()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

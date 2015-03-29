import pygame
from pygame import *
from random import Random
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        #self._random = Random.random()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        #self._image_surf = pygame.image.load("myimage.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pygame.draw.lines(self.diplay_surf, black, [(20, 4), (40, 30), (30, 80), (40, 80)], 1)
        self._display_surf.blit()
        pygame.display.flip()
 
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

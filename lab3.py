import pygame
import random

pink = (255, 0, 255)
black = (0, 0, 0)

class Life(object):
    def __init__(self, screen,iniciales):
        self.screen = screen
        for cont in iniciales:
            x = cont[0]
            y = cont[1]
            self.pixel(x,y,pink)
        

    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y,color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()
    def fate(self, x,y):
        cell = [x,y]
        search_x = x - 1
        search_y = y - 1
        search = [search_x,search_y]
        fate = 0
        conty= 0
        if(self.prev_turn.get_at((x, y))[:3] == pink):
            while (conty <= 2):
                contx = 0
                search_x = x - 1
                while (contx <= 2):
                    if(self.prev_turn.get_at((search_x, search_y))[:3] == pink):
                        search = [search_x,search_y]
                        if(search != [x,y]):
                            fate += 1
                    contx = contx + 1
                    search_x = search_x + 1
                conty = conty + 1
                search_y = search_y + 1
            return fate
        elif (self.prev_turn.get_at((x, y))[:3] == black):
            while (conty <= 2):
                contx = 0
                search_x = x - 1
                while (contx <= 2):
                    if(self.prev_turn.get_at((search_x, search_y))[:3] == pink):
                        fate += 1
                    contx = contx + 1
                    search_x = search_x + 1
                conty = conty + 1
                search_y = search_y + 1
            return fate
            
                            

    def render(self):
        for y in range(10,190):
            for x in range(10,190):
                fate = self.fate(x,y)
                if(self.prev_turn.get_at((x, y))[:3] == pink):
                    if(fate < 2):
                        self.pixel(x, y,black)
                    if (fate == 2 or fate == 3):
                        self.pixel(x, y,pink)
                    if (fate > 3):
                        self.pixel(x, y,black)
                elif (fate == 3):
                    self.pixel(x, y,pink)
            
    
iniciales = []
for var in range(5000):
    iniciales.append([random.randint(10,190),random.randint(10,190)])

pygame.init()
screen = pygame.display.set_mode((200, 200))

r = Life(screen,iniciales)

while True:
  pygame.time.delay(100)
  r.copy()
  r.clear()
  r.render()

  pygame.display.flip()

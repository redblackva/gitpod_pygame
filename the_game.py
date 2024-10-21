import pygame, sys
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHTRED = (255, 150, 150)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (200, 0, 100)
PEACH = (255, 200, 150)

class environment:
    def __init__(self, dimensions, colour, caption, font):
        self.dimensions = dimensions
        self.colour = colour
        self.caption = caption
        self.font = font
        self.window = pygame.display.set_mode((dimensions[0], dimensions[1]))
        self.window.fill(colour)
        pygame.display.set_caption(caption)
    
    def updateColour(self, newColour):
        self.colour = newColour
        self.window.fill(self.colour)

window = environment((500, 800), PEACH, "To Feed or not to Feed", pygame.font.Font('freesansbold.ttf', 32))

class button:
    def __init__ (self, size, position, colours, text, function, surface):
        self.size = size 
        self.position = position
        self.colours = colours 
        self.function = function
        self.surface = surface
        self.text = surface.font.render(text, True, colours[1], colours[2])
        self.textRect = self.text.get_rect()
        self.textRect.center = (surface.dimensions[0] * position[0], surface.dimensions[1] * position[1])
        self.buttonRect = pygame.Rect(surface.dimensions[0] * position[0] - size[0] / 2, surface.dimensions[1] * position[1] - size[1] / 2, size[0], size[1])
    
    def place(self):
        pygame.draw.rect(self.surface.window, self.colours[0], self.buttonRect)
        self.surface.window.blit(self.text, self.textRect)


def swapF(bool):
    if bool:
        return False
    else:
        return True
imageButton = button((200, 60), (0.5, 0.5), (PINK, LIGHTRED, PINK), "Girl Scouts", swapF, window)


class image:
    def __init__(self, name, scale, surface):
        self.name = name
        self.scale = scale
        self.surface = surface
        self.image = pygame.image.load(name).convert()
        self.image = pygame.transform.scale(self.image, (self.surface.dimensions[0] *self.scale[0], self.surface.dimensions[1] * self.scale[1]))
    
    def place(self, pos):
        self.surface.window.blit(self.image, ((pos[0] - self.scale[0] / 2) * self.surface.dimensions[0], (pos[1] - self.scale[1] / 2) * self.surface.dimensions[1]))

toucan1 = image("TOUCAN.jpeg", (0.4, 0.25), window)

BIRD = False

while True:
    mouse = pygame.mouse.get_pos()
    window.updateColour(PEACH)
    imageButton.place()

    if BIRD:
        toucan1.place((1/2, 1/6))
        toucan1.place((1/2, 5/6))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if window.dimensions[0] * imageButton.position[0] - imageButton.size[0] / 2 <= mouse[0] <= window.dimensions[0] * imageButton.position[0] + imageButton.size[0] / 2:
                if window.dimensions[1] * imageButton.position[1] - imageButton.size[1] / 2 <= mouse[1] <= window.dimensions[1] * imageButton.position[1] + imageButton.size[1] / 2:
                    BIRD = imageButton.function(BIRD)
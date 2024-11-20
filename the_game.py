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
    
    def mouseCheck(self, button):
        if self.dimensions[0] * button.position[0] - button.size[0] / 2 <= mouse[0] <= self.dimensions[0] * button.position[0] + button.size[0] / 2:
                if self.dimensions[1] * button.position[1] - button.size[1] / 2 <= mouse[1] <= self.dimensions[1] * button.position[1] + button.size[1] / 2:
                    return True

window = environment((500, 800), PEACH, "To Feed or not to Feed", pygame.font.Font('freesansbold.ttf', 32))

class button:
    def __init__ (self, size, position, colours, text, function, surface, exist):
        self.exist = exist
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

startB = button((250, 60), (0.5, 0.5), (PINK, LIGHTRED, PINK), "Image Bank", swapF, window, True)
nextB = button((100, 60), (0.8, 0.5), (PINK, LIGHTRED, PINK), "Next", swapF, window, False)
prevB = button((100, 60), (0.2, 0.5), (PINK, LIGHTRED, PINK), "Prev", swapF, window, False)
backB = button((100, 60), (0.16, 0.08), (PINK, LIGHTRED, PINK), "Back", swapF, window, False)

buttons = [nextB, prevB, startB, backB]

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
toucan2 = image("TOUCAN2.jpg", (0.4, 0.25), window)
parrot = image("PARROT.jpg", (0.4, 0.25), window)
sillyBird1 = image("sillyBird1.jpeg", (0.4, 0.25), window)
sillyBird2 = image("sillyBird2.jpeg", (0.4, 0.25), window)
sillyBird3 = image("sillyBird3.jpeg", (0.4, 0.25), window)
sillyBird4 = image("sillyBird4.jpeg", (0.4, 0.25), window)

Birds = [toucan1, toucan2, parrot, sillyBird1, sillyBird2, sillyBird3, sillyBird4]
BIRD = len(Birds)

while True:
    mouse = pygame.mouse.get_pos()
    window.updateColour(PEACH)

    for i in buttons:
        if i.exist:
            i.place()

    if BIRD < len(Birds):
        Birds[BIRD].place((1/2, 1/4))
        Birds[BIRD].place((1/2, 3/4))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if window.mouseCheck(startB) and startB.exist:
                startB.exist = False
                nextB.exist = True
                prevB.exist = True
                backB.exist = True
                BIRD = 0
            if window.mouseCheck(nextB) and nextB.exist:
                BIRD += 1
                if BIRD >= len(Birds):
                    BIRD = 0
            if window.mouseCheck(prevB) and prevB.exist:
                BIRD -= 1
                if BIRD < 0:
                    BIRD = len(Birds) - 1
            if window.mouseCheck(backB) and backB.exist:
                startB.exist = True
                nextB.exist = False
                prevB.exist = False
                backB.exist = False
                BIRD = len(Birds)
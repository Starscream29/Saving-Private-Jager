# import the pygame module, so you can use it
import pygame
import time
from gridGraph import gridGraph
from Functions import constrain
from Zombies import processGrunts, processBreachers


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("Logo.PNG")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Scott Chang looks for his son")

    # create a surface on screen that has the size of 240 x 180
    screenWidth = 1300
    screenHeight = 650
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))

    # define scott's initial position
    ScottX = 50
    ScottY = 50
    # how many pixels we move our scott
    step = 50
    # check if the scott is still on screen, if not change direction

    Scott = pygame.image.load("SC.PNG")
    screen.blit(Scott, (ScottX, ScottY))
    pygame.display.flip()

    clock = pygame.time.Clock()
    # define a variable to control the main loop
    game = True

    grunts = []
    breachers = []
    startTime = 0
    endTime = 0
    gruntClock = 0
    gruntSpawnClock = 0
    breacherClock = 0
    breacherSpawnClock = 0

    # main loop
    while game:
        startTime = time.time()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ScottX -= step
                    ScottX = constrain(ScottX, 0, screenWidth - step)
                if event.key == pygame.K_RIGHT:
                    ScottX += step
                    ScottX = constrain(ScottX, 0, screenWidth - step)
                if event.key == pygame.K_UP:
                    ScottY -= step
                    ScottY = constrain(ScottY, 0, screenHeight - step)
                if event.key == pygame.K_DOWN:
                    ScottY += step
                    ScottY = constrain(ScottY, 0, screenHeight - step)
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                game = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game = False

        # now blit the scott on screen
        screen.blit(background, (0, 0))
        Jager = pygame.image.load("Jager.PNG")
        screen.blit(Jager, (650, 500))

        gruntClock, gruntSpawnClock = processGrunts(grunts, gruntSpawnClock, gruntClock, pygame, graph, screen)
        breacherClock, breacherSpawnClock = processBreachers(breachers, breacherSpawnClock, breacherClock, pygame, graph, screen)

        screen.blit(Scott, (ScottX, ScottY))
        # and update the screen (dont forget that!)
        pygame.display.flip()

        # this will slow it down to 10 fps, so you can watch it,
        # otherwise it would run too fast
        endTime = time.time()
        gruntClock = gruntClock + (endTime - startTime)
        gruntSpawnClock = gruntSpawnClock + (endTime - startTime)
        breacherClock = breacherClock + (endTime - startTime)
        breacherSpawnClock = breacherSpawnClock + (endTime - startTime)
        clock.tick(25)


if __name__ == '__main__':
    graph = gridGraph

    main()

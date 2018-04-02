# import modules and functions
import pygame
import time
from gridGraph import gridGraph
from Functions import constrain
from Zombies import processGrunts, processBreachers


def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("Logo.PNG")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Scott Chang saves his son")

    # create game surface
    screenWidth = 1300
    screenHeight = 650
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))

    # set scott's initial position
    ScottX = 650
    ScottY = 250
    # how many pixels each move is, also the width of each square
    step = 50

    # display Scott and Jager's initial positions
    screen.blit(background, (0, 0))
    Scott = pygame.image.load("SC.PNG")
    screen.blit(Scott, (ScottX, ScottY))
    Jager = pygame.image.load("Jager.PNG")
    screen.blit(Jager, (650, 500))
    pygame.display.flip()

    # set up the game clock, speed this up to make the game much harder
    clock = pygame.time.Clock()
    # 2 phases, first the player gets to prep his barricades, before the actual games starts
    prep = True
    game = False

    # arrays containing the current locations of zombies
    grunts = []
    breachers = []
    # preps timers for moving and spawning
    startTime = 0
    endTime = 0
    gruntClock = 0
    gruntSpawnClock = 0
    breacherClock = 0
    breacherSpawnClock = 0

    prepPhase = 0

    while prep:
        startTime = time.time()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # read keystrokes for movement
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
                prep = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                prep = False
        screen.blit(background, (0, 0))
        screen.blit(Scott, (ScottX, ScottY))
        screen.blit(Jager, (650, 500))
        pygame.display.flip()
        endTime = time.time()
        prepPhase = prepPhase + (endTime - startTime)
        if prepPhase >= 0.5:
            prep = False
            game = True

        clock.tick(25)

    # prep has ended, game has started.
    while game:
        startTime = time.time()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Reading movement keys
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

        # display the Jager
        screen.blit(background, (0, 0))
        Jager = pygame.image.load("Jager.PNG")
        screen.blit(Jager, (650, 500))

        # spawn/move zombies
        gruntClock, gruntSpawnClock = processGrunts(grunts, gruntSpawnClock, gruntClock, pygame, graph, screen)
        breacherClock, breacherSpawnClock = processBreachers(breachers, breacherSpawnClock, breacherClock, pygame, graph, screen)

        # display Scott
        screen.blit(Scott, (ScottX, ScottY))
        # and update the screen
        pygame.display.flip()

        # update clocks
        endTime = time.time()
        gruntClock = gruntClock + (endTime - startTime)
        gruntSpawnClock = gruntSpawnClock + (endTime - startTime)
        breacherClock = breacherClock + (endTime - startTime)
        breacherSpawnClock = breacherSpawnClock + (endTime - startTime)
        clock.tick(25)


if __name__ == '__main__':
    graph = gridGraph

    main()

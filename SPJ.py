# import modules and functions
import pygame
import time
from gridGraph import gridGraph
from Functions import constrain
from Zombies import processGrunts, processBreachers
import sys


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
    wall = pygame.image.load("wall.PNG")
    pygame.display.flip()

    # set up the game clock, speed this up to make the game much harder
    clock = pygame.time.Clock()
    # 2 phases, first the player gets to prep his barricades, before the actual games starts
    prep = True
    game = False

    # arrays containing the current locations of zombies
    grunts = []
    breachers = []
    # breacher targets:
    target = []
    detonating = []
    # preps timers for moving and spawning
    startTime = 0
    endTime = 0
    gruntClock = 0
    gruntSpawnClock = 0
    breacherClock = 0
    breacherSpawnClock = 0
    detonatingClock = 0
    barricades = [[350, 600], [350, 550], [350, 500], [350, 450], [350, 400], [350, 350], [350, 300],
        [1000, 600], [1000, 550], [1000, 500], [1000, 450], [1000, 400], [1000, 350], [1000, 300]]
    prepPhase = 0
    print("Hit 1, 2, or 3 to choose a defence configuration")
    while prep:
        startTime = time.time()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # read keystrokes for different wall arangements
                if event.key == pygame.K_1:
                    barricades = [[350, 600], [350, 550], [350, 500], [350, 450], [350, 400], [350, 350], [350, 300],
                        [1000, 600], [1000, 550], [1000, 500], [1000, 450], [1000, 400], [1000, 350], [1000, 300]]
                if event.key == pygame.K_2:
                    barricades = [[150, 350], [200, 350], [250, 350], [300, 350], [350, 350], [400, 350],
                        [450, 350], [500, 350], [550, 350], [600, 350], [650, 350], [700, 350], [750, 350],
                        [800, 350], [850, 350], [900, 350], [950, 350], [1000, 350], [1050, 350], [1100, 350],
                        [1100, 400], [150, 400]]
                if event.key == pygame.K_3:
                    barricades = [[350, 600], [350, 550], [350, 500], [350, 450],
                        [1000, 600], [1000, 550], [1000, 500], [1000, 450],
                        [450, 200], [500, 200], [550, 200], [600, 200], [650, 200], [700, 200], [750, 200],
                        [800, 200], [850, 200]]
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
        for n in barricades:
            screen.blit(wall, n)
        pygame.display.flip()
        endTime = time.time()
        prepPhase = prepPhase + (endTime - startTime)
        if prepPhase >= 0.3:
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

        # display barricade
        for n in barricades:
            screen.blit(wall, n)

        # spawn/move zombies
        gruntClock, gruntSpawnClock = processGrunts(barricades, grunts, gruntSpawnClock, gruntClock, graph, screen)
        breacherClock, breacherSpawnClock, detonatingBreacher = processBreachers(detonating, target, barricades, breachers, breacherSpawnClock, breacherClock, graph, screen)
        endTime2 = time.time()
        # display detonating breacher
        if detonatingBreacher:
            if detonatingClock >= 0.3:
                fuze = pygame.image.load("fuze.PNG")
                detonatingPosition = [int(i) for i in detonatingBreacher[0].split()]
                screen.blit(fuze, detonatingPosition)
                detonatingClock = 0
                del detonatingBreacher[0]
                barricades.remove(detonatingPosition)
                print("A barricade has been destroyed")
            else:
                detonatingClock = detonatingClock + (endTime2 - startTime)

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
        detonatingClock = detonatingClock + (endTime - startTime)
        clock.tick(60)


if __name__ == '__main__':
    graph = gridGraph
    main()
    pygame.quit()
    sys.exit()

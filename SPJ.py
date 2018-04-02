# import the pygame module, so you can use it
import pygame
import time
from Functions import constrain
from Functions import Spawn
from collections import deque


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("Logo.PNG")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Scott Chang looks for his son")

    # create a surface on screen that has the size of 240 x 180
    screenWidth = 200
    screenHeight = 200
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
    running = True

    zombies = []
    startTime = 0
    endTime = 0
    gruntClock = 0
    zombies =[[0, 0]]

    # main loop
    while running:
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
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # now blit the scott on screen
        screen.blit(background, (0, 0))
        Jager = pygame.image.load("Jager.PNG")
        screen.blit(Jager, (150, 150))

        # spawnX, spawnY = Spawn()
        #
        # if (gruntClock) >= 0.1:
        #     zombies.append([spawnX, spawnY])
        #     gruntClock = 0
        #
        Grunt = pygame.image.load("Grunt.PNG")
        if gruntClock >= 0.03:
            for i in range(len(zombies)):
                currentLocation = [0, 0]
                currentLocation = str(zombies[i][0]) + ' ' + str(zombies[i][1])
                newLocation = [0, 0]
                pathing = shortest_path(graph, currentLocation, '150 150')
                newLocation[0], newLocation[1] = pathing[1].split()
                zombies[i][0] = int(newLocation[0])
                zombies[i][1] = int(newLocation[1])
                gruntClock = 0

        for j in range(len(zombies)):
            positionX = zombies[j][0]
            positionY = zombies[j][1]
            screen.blit(Grunt, (positionX, positionY))

        screen.blit(Scott, (ScottX, ScottY))
        # and update the screen (dont forget that!)
        pygame.display.flip()

        # this will slow it down to 10 fps, so you can watch it,
        # otherwise it would run too fast
        endTime = time.time()
        gruntClock = gruntClock + (endTime - startTime)
        clock.tick(50)


def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])


def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None  # or raise appropriate exception


if __name__ == '__main__':
    graph = {'150 0': ['100 0', '150 50'],
             '150 50': ['150 0', '100 50', '150 100'],
             '150 100': ['150 50', '100 100', '150 150'],
             '150 150': ['150 100', '100 150'],
             '100 0': ['150 0', '100 50', '50 0'],
             '100 50': ['100 0', '150 50', '100 100', '50 50'],
             '100 100': ['100 50', '150 100', '100 150', '50 100'],
             '100 150': ['150 150', '100 100', '50 150'],
             '50 0': ['100 0', '50 50', '0 0'],
             '50 50': ['50 0', '100 50', '50 100', '0 50'],
             '50 100': ['50 50', '100 100', '50 150', '0 100'],
             '50 150': ['50 100', '100 150', '0 150'],
             '0 0': ['50 0', '0 50'],
             '0 50': ['0 0', '50 50', '0 100'],
             '0 100': ['0 50', '50 100', '0 150'],
             '0 150': ['0 100', '50 150']}

    main()

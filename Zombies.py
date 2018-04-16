from Functions import Spawn
from Functions import shortest_path
from Functions import shortest_pathBreacher
import random
import pygame
import SPJsprites
import sys


def processGrunts(barricades, grunts, gruntSpawnClock, gruntClock, graph, screen, bulletList):
    '''the most common zombie, grunts spawn in large numbers and attempt to
    run at jager, dies in a single shot, if one reaches jager, the play loses,
    ignores Scott'''

    jager = SPJsprites.Jager(screen)
    spawnX, spawnY = Spawn()

    if (gruntSpawnClock) >= 0.1:
        grunts.append([spawnX, spawnY])
        # reset the spawn clock
        gruntSpawnClock = 0

    if gruntClock >= 0.4:
        for i in range(len(grunts)):
            currentLocation = [0, 0]
            currentLocation = str(grunts[i][0]) + ' ' + str(grunts[i][1])
            newLocation = [0, 0]
            pathing = shortest_path(graph, currentLocation, '650 500', barricades)
            newLocation[0], newLocation[1] = pathing[1].split()
            grunts[i][0] = int(newLocation[0])
            grunts[i][1] = int(newLocation[1])
            # reset the move clock
            gruntClock = 0

    for j in range(len(grunts)):
        Grunt = pygame.image.load("Grunt.PNG")
        if j < len(grunts):
            positionX = grunts[j][0]
            positionY = grunts[j][1]
            rectangle = pygame.draw.rect(screen, (50, 50, 50), (positionX, positionY, 50, 50))
            screen.blit(Grunt, (positionX, positionY))
            if jager.rect.colliderect(rectangle):
                print("Jager is dead. Mission failed. Better luck next time.")
                pygame.quit()
                sys.exit()
            for bullet in bulletList:
                if bullet.rect.colliderect(rectangle):
                    bulletList.remove(bullet)
                    del grunts[j]
                    # grunts[j][0] = 0
                    deathsound = pygame.mixer.Sound("Grunt Death.wav")
                    deathsound.play()

    return gruntClock, gruntSpawnClock


def processBreachers(detonating, target, barricades, breachers, breachersSpawnClock, breachersClock, graph, screen, bulletList):
    '''spawns much more rarely, but move very quickly. They don't attack Scott or Jager,
    instead, they prioritize going after barricades. If they are allowed to attach to a barricade,\
    the barricade is destroyed'''

    spawnX, spawnY = Spawn()
    if (breachersSpawnClock) >= 1:
        breachers.append([spawnX, spawnY])

        target.append(" ".join([str(x) for x in random.choice(barricades)]))
        # reset hte spawn clock
        breachersSpawnClock = 0
        print("Another breacher has spawned")

    Breacher = pygame.image.load("Breacher.PNG")
    if breachersClock >= 0.03:
        for i in range(len(breachers)):
            currentLocation = [0, 0]
            currentLocation = str(breachers[i][0]) + ' ' + str(breachers[i][1])
            checkBarricade = [int(i) for i in currentLocation.split()]
            if checkBarricade in barricades:
                del breachers[0]
                detonating.append(currentLocation)
                break
            if currentLocation is target[i]:
                del breachers[0]
                break
            newLocation = [0, 0]
            pathing = shortest_pathBreacher(graph, currentLocation, target[i], barricades)
            newLocation[0], newLocation[1] = pathing[1].split()

            breachers[i][0] = int(newLocation[0])
            breachers[i][1] = int(newLocation[1])
            # reset the move clock
            breachersClock = 0

    for j in range(len(breachers)):
        if j < len(breachers):
            positionX = breachers[j][0]
            positionY = breachers[j][1]
            rectangle = pygame.draw.rect(screen, (50, 50, 50), (positionX, positionY, 50, 50))
            screen.blit(Breacher, (positionX, positionY))
            for bullet in bulletList:
                if bullet.rect.colliderect(rectangle):
                    # print("Hit!")
                    bulletList.remove(bullet)
                    deathsound = pygame.mixer.Sound("Breacher Death.wav")
                    deathsound.play()
                    del breachers[j]
    return breachersClock, breachersSpawnClock, detonating

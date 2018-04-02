from Functions import Spawn
from Functions import shortest_path


def processGrunts(grunts, gruntSpawnClock, gruntClock, pygame, graph, screen):
    '''the most common zombie, grunts spawn in large numbers and attempt to
    run at jager, dies in a single shot, if one reaches jager, the play loses,
    ignores Scott'''

    spawnX, spawnY = Spawn()

    if (gruntSpawnClock) >= 0.09:
        grunts.append([spawnX, spawnY])
        # reset the spawn clock
        gruntSpawnClock = 0

    Grunt = pygame.image.load("Grunt.PNG")
    if gruntClock >= 0.03:
        for i in range(len(grunts)):
            currentLocation = [0, 0]
            currentLocation = str(grunts[i][0]) + ' ' + str(grunts[i][1])
            newLocation = [0, 0]
            pathing = shortest_path(graph, currentLocation, '650 500')
            newLocation[0], newLocation[1] = pathing[1].split()
            grunts[i][0] = int(newLocation[0])
            grunts[i][1] = int(newLocation[1])
            # reset the move clock
            gruntClock = 0

    for j in range(len(grunts)):
        positionX = grunts[j][0]
        positionY = grunts[j][1]
        screen.blit(Grunt, (positionX, positionY))
    return gruntClock, gruntSpawnClock


def processBreachers(breachers, breachersSpawnClock, breachersClock, pygame, graph, screen):
    '''spawns much more rarely, but move very quickly. They don't attack Scott or Jager,
    instead, they prioritize going after barricades. If they are allowed to attach to a barricade
    for a few seconds, the barricade is destroyed'''

    spawnX, spawnY = Spawn()

    if (breachersSpawnClock) >= 0.2:
        breachers.append([spawnX, spawnY])
        # reset hte spawn clock
        breachersSpawnClock = 0

    Breacher = pygame.image.load("Breacher.PNG")
    if breachersClock >= 0.01:
        for i in range(len(breachers)):
            currentLocation = [0, 0]
            currentLocation = str(breachers[i][0]) + ' ' + str(breachers[i][1])
            newLocation = [0, 0]
            pathing = shortest_path(graph, currentLocation, '650 500')
            newLocation[0], newLocation[1] = pathing[1].split()
            breachers[i][0] = int(newLocation[0])
            breachers[i][1] = int(newLocation[1])
            # reset the move clock
            breachersClock = 0

    for j in range(len(breachers)):
        positionX = breachers[j][0]
        positionY = breachers[j][1]
        screen.blit(Breacher, (positionX, positionY))
    return breachersClock, breachersSpawnClock

import pygame
import time
from gridGraph import gridGraph
from Zombies import processGrunts, processBreachers
import SPJsprites


def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("Images/Logo.PNG")
    pygame.display.set_icon(logo)

    # set the caption
    caption = "Scott Chang's Bizarre Adventure"
    pygame.display.set_caption(caption)

    # create game surface
    size = (1300, 650)
    screen = pygame.display.set_mode(size)

    # background
    BACKGROUND_COLOR = (50, 50, 50)
    screen.fill(BACKGROUND_COLOR)

    # display Jager's initial position
    Jager = pygame.image.load("Images/Jager.PNG")
    screen.blit(Jager, (650, 500))

    # load the wall image
    wall = pygame.image.load("Images/wall.PNG")

    # update contents of entire display
    pygame.display.flip()

    # set up the game clock, speed this up to make the game much harder
    clock = pygame.time.Clock()
    # 2 phases, first the player gets to prep his barricades, before the actual games starts

    prep = True
    game = False

    # create sprite list of bullets
    bulletList = pygame.sprite.Group()

    # create Scott and Jager
    scott = SPJsprites.Scott(screen)
    jager = SPJsprites.Jager(screen)

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
    print("Hit 1, 2, or 3 to choose a defence configuration.")
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

        screen.fill(BACKGROUND_COLOR)
        jager.draw(screen)
        for n in barricades:
            screen.blit(wall, n)
        pygame.display.flip()
        endTime = time.time()
        prepPhase = prepPhase + (endTime - startTime)
        if prepPhase >= 0.03:
            prep = False
            game = True

        clock.tick(30)

    # Music
    pygame.mixer.music.load("Sound/Music.mp3")
    pygame.mixer.music.play(0)

    score = 0
    spawntime = 0.2
    # prep has ended, game has started.
    while game:
        startTime = time.time()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                game = False
            scott.get_event(event, bulletList)

        # self.update()
        bulletList.update(pygame.display.get_surface().get_rect())
        scott.update()

        # background again
        screen.fill(BACKGROUND_COLOR)

        # display Scott and bullets
        scott.draw(screen)
        jager.draw(screen)
        bulletList.draw(screen)

        # display barricade
        for n in barricades:
            screen.blit(wall, n)

        # spawn/move zombies
        gruntClock, gruntSpawnClock, score, gameOver = processGrunts(barricades, grunts, gruntSpawnClock, gruntClock, graph, screen, bulletList, score, spawntime)

        # Check if Jager is dead, if so, end the game
        if gameOver is True:
            pygame.quit()
            return score
        breacherClock, breacherSpawnClock, detonatingBreacher, score = processBreachers(detonating, target, barricades, breachers, breacherSpawnClock, breacherClock, graph, screen, bulletList, score)

        endTime2 = time.time()
        # display detonating breacher
        if detonatingBreacher:
            if detonatingClock >= 0.3:
                fuze = pygame.image.load("Images/fuze.PNG")
                detonatingPosition = [int(i) for i in detonatingBreacher[0].split()]
                screen.blit(fuze, detonatingPosition)
                detonatingClock = 0
                del detonatingBreacher[0]
                if detonatingPosition in barricades:
                    barricades.remove(detonatingPosition)
            else:
                detonatingClock = detonatingClock + (endTime2 - startTime)

        # Update the score
        myfont = pygame.font.SysFont("monospace", 30)
        label = myfont.render("score: " + str(score), 1, (255, 255, 0))
        screen.blit(label, (10, 600))

        # gruntList.draw(screen)
        pygame.display.flip()

        # update clocks
        endTime = time.time()
        gruntClock = gruntClock + (endTime - startTime)
        gruntSpawnClock = gruntSpawnClock + (endTime - startTime)
        breacherClock = breacherClock + (endTime - startTime)
        breacherSpawnClock = breacherSpawnClock + (endTime - startTime)
        detonatingClock = detonatingClock + (endTime - startTime)
        if spawntime > 0.08:
            spawntime = spawntime - 0.0001
        else:
            spawntime = spawntime - 0.00003

        clock.tick(60)


if __name__ == '__main__':
    graph = gridGraph
    score = main()

    print("Game over, your score was: " + str(score))

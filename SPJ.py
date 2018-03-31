# import the pygame module, so you can use it
import pygame
from Functions import constrain


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
    ScottX = 650
    ScottY = 300
    # how many pixels we move our scott
    step = 50
    # check if the scott is still on screen, if not change direction

    Scott = pygame.image.load("SC.PNG")
    screen.blit(Scott, (ScottX, ScottY))
    pygame.display.flip()

    clock = pygame.time.Clock()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
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
        screen.blit(Jager, (650, 500))

        screen.blit(Scott, (ScottX, ScottY))
        # and update the screen (dont forget that!)
        pygame.display.flip()

        # this will slow it down to 10 fps, so you can watch it,
        # otherwise it would run too fast
        clock.tick(50)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

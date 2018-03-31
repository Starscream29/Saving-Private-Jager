# import the pygame module, so you can use it
import pygame


# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("Logo.PNG")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screenWidth = 1800
    screenHeight = 800
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))

    # define the position of the smily
    ScottX = 250
    ScottY = 250
    # how many pixels we move our smily each frame
    stepX = 50
    stepY = 50
    # check if the smily is still on screen, if not change direction

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
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # check for keypress and check if it was Esc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # check if the smily is still on screen, if not change direction
        if ScottX > screenWidth - 50 or ScottX < 0:
            stepX = -stepX
        if ScottY > screenHeight - 50 or ScottY < 0:
            stepY = -stepY
        # update the position of the smily
        ScottX += stepX  # move it to the right
        ScottY += stepY  # move it down

        # now blit the smily on screen
        screen.blit(background, (0,0))
        screen.blit(Scott, (ScottX, ScottY))
        # and update the screen (dont forget that!)
        pygame.display.flip()

        # this will slow it down to 10 fps, so you can watch it,
        # otherwise it would run too fast
        clock.tick(10)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

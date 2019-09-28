import pygame
import os


def main():
    """ main() fonction """

    # initialization of pygame
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(
        "Mac_Gyver_ressources/tile-crusader-logo.png"
        ))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("test_program")

    # Create a surface on screen
    screen = pygame.display.set_mode((600, 600))
    screen.fill((255, 200, 200))

    # Create a blit
    image = pygame.image.load(os.path.join(
        "Mac_Gyver_ressources/MacGyver.png"
        ))
    xpos = 300
    ypos = 300
    screen.blit(image, (xpos, ypos))
    pygame.display.flip()

    # Control of move
    step_x = 10
    step_y = 10

    # Control of the loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

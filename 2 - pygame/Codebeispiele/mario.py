import pygame

# initialize PyGame, and launch a window with the defined size and title
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("It's-a Me, Mario!")

# Our background color (RGB)
GREEN = (0, 255, 0)

# load a Mario icon
image = pygame.image.load('mario-60.png')

# Mario's initial position 
x = 300
y = 200

# We need the clock to manage the speed of our game loop
clock = pygame.time.Clock()
# The game loop
while True:
    clock.tick(60) # fps

    # check for keyboard events that happened since last loop run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 2
            elif event.key == pygame.K_UP:
                y -= 2
            elif event.key == pygame.K_LEFT:
                x -= 2
            elif event.key == pygame.K_RIGHT:
                x += 2

    # draw the background color and Mario
    screen.fill(GREEN)
    screen.blit(image, (x,y))
    # finally render everything
    pygame.display.update()
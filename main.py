import pygame
import os
import random

# Define constants in caps sense they wont change

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 700  # These variables define our "window", width, height
BORDER_WIDTH, BORDER_COLOR = 8, (255,255,255)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")  # Window caption

BLACK = (0, 0, 0)  # Defining background color
FPS = 60  # Defines our frame rate
VELOCITY = 5  # Defines how fast the ship will move

def BORDER():  # Border for my game
    pygame.draw.rect(WINDOW, BORDER_COLOR, (0, 0, WINDOW_WIDTH, BORDER_WIDTH))  # Top border
    pygame.draw.rect(WINDOW, BORDER_COLOR, (0, 0, BORDER_WIDTH, WINDOW_HEIGHT))  # Left border
    pygame.draw.rect(WINDOW, BORDER_COLOR, (0, WINDOW_HEIGHT - BORDER_WIDTH, WINDOW_WIDTH, BORDER_WIDTH))  # Bottom border
    pygame.draw.rect(WINDOW, BORDER_COLOR, (WINDOW_WIDTH - BORDER_WIDTH, 0, BORDER_WIDTH, WINDOW_HEIGHT))  # Right border


# Potential start screen section
def START_SCREEN():
    WINDOW.fill(BLACK)



stars = []

def create_stars(surface, num_stars):
    global stars

    # Remove stars that have gone off the screen
    stars = [(x, y + 1) for x, y in stars if y < WINDOW_HEIGHT]

    # Add new stars
    for _ in range(num_stars - len(stars)):
        x = random.randint(0, WINDOW_WIDTH)
        y = random.randint(-WINDOW_HEIGHT, 0)
        stars.append((x, y))

    # Draw stars
    for x, y in stars:
        pygame.draw.circle(surface, (255, 255, 255), (x, y), 1)



# Spaceship
SPACE_WIDTH, SPACE_HEIGHT = 70, 90
SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship.png'))

SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACE_WIDTH, SPACE_HEIGHT))

ship = pygame.Rect(420, 350, SPACE_WIDTH, SPACE_HEIGHT)


# Astroids
ASTROID_WIDTH, ASTROID_HEIGHT = 70, 90
ASTROID_IMAGE = pygame.image.load(
    os.path.join('assets', 'astroid.png'))

ASTROID_ROTATE_SPEED = 2

ASTROID = pygame.transform.scale(ASTROID_IMAGE, (ASTROID_WIDTH, ASTROID_HEIGHT))

astroid_x = random.randint(0, WINDOW_WIDTH - ASTROID_WIDTH)
astroid = pygame.Rect(astroid_x, 0,  ASTROID_WIDTH, ASTROID_HEIGHT)




def draw_window(ship):
    WINDOW.fill(BLACK)  # Draw background first
    create_stars(WINDOW, 200)  # Creates stars
    BORDER()

    WINDOW.blit(SPACESHIP, (ship.x, ship.y))  # Draws spaceship start position
    WINDOW.blit(ASTROID, (astroid.x, 0))  # Draw the asteroid

    pygame.display.update()  # Updating our window


def spaceship_movement(keys_pressed, ship):
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        if ship.x - VELOCITY > BORDER_WIDTH:  # Check left border
            ship.x -= VELOCITY
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        if ship.x + VELOCITY < WINDOW_WIDTH - BORDER_WIDTH - SPACE_WIDTH:  # Check right border
            ship.x += VELOCITY
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
        if ship.y - VELOCITY > BORDER_WIDTH:  # Check top border
            ship.y -= VELOCITY
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
        if ship.y + VELOCITY < WINDOW_HEIGHT - BORDER_WIDTH - SPACE_HEIGHT:  # Check bottom border
            ship.y += VELOCITY


def main():
    
    clock = pygame.time.Clock()
    run = True


    while run:
        clock.tick(FPS)  # frame refresh rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()  # What keys are currently being pressed
        spaceship_movement(keys_pressed, ship)  # Moves spaceship

        draw_window(ship)  # Displaying the window


    pygame.quit()  # If user quits the game

if __name__ == "__main__":
    main()  # Runs the file

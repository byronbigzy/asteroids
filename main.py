import pygame  # Import pygame for game development
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  # Import screen dimensions from constants.py
from player import Player  # Import the Player class

def main():
    # Print initial debug messages
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()  # Initialize all pygame modules

    # Create the game window with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Set the initial position of the player at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Create an instance of the Player class
    player = Player(x, y)

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen by filling it with black

        # Handle events (e.g., quitting the game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the close button is clicked
                running = False  # Exit the game loop

        # Draw the player on the screen
        player.draw(screen)

        # Update the display to show the new frame
        pygame.display.flip()

        # Limit the game to 60 frames per second (FPS)
        dt = clock.tick(60) / 1000  # `dt` represents time elapsed per frame (in seconds)

        player.update(dt)

    # Quit pygame when the game loop ends
    pygame.quit()

# Run the game if this script is executed directly
if __name__ == '__main__':
    main()

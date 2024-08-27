import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Moving Ball Example')

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up ball properties
ball_color = red
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5
ball_speed_y = 5

# Main game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce the ball off the edges of the window
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    # Clear the screen
    screen.fill(white)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
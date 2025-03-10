import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chain of Boxes")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Box properties
box_width, box_height = 50, 50
gap = 20
border_width = 2  # Width of the border


# Function to draw a box with only the border
def draw_box(x, y):
    pygame.draw.rect(window, BLACK, (x, y, box_width, box_height), border_width)


# Initial number of boxes
num_boxes = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                num_boxes += 1

    # Fill the background
    window.fill(WHITE)

    # Draw chain of boxes
    x, y = 100, 100
    for i in range(num_boxes):
        draw_box(x, y)
        if i < num_boxes - 1:  # Draw line to the next box
            pygame.draw.line(
                window,
                BLACK,
                (x + box_width, y + box_height // 2),
                (x + box_width + gap, y + box_height // 2),
                2,
            )
        x += box_width + gap

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

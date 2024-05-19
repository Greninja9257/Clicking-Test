import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Click the Red Button")

# Define colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Define button dimensions
button_radius = 100
button_x = window_width // 2 - button_radius
button_y = window_height // 2 - button_radius
button_y_offset = 10  # Amount to move the button down and up

# Initialize variables
start_time = None
last_click_time = None
click_count = 0
delay_sum = 0
animation_time = 0
animation_duration = 0.2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_rect = pygame.Rect(button_x, button_y, button_radius * 2, button_radius * 2)
            if button_rect.collidepoint(mouse_x, mouse_y):
                if start_time is None:
                    start_time = time.time()
                if last_click_time is not None:
                    delay = time.time() - last_click_time
                    delay_sum += delay
                last_click_time = time.time()
                click_count += 1
                animation_time = time.time()

    # Clear the window
    window.fill(BLACK)

    # Draw the button
    if time.time() - animation_time < animation_duration:
        button_y_animation = button_y + button_y_offset * (1 - (time.time() - animation_time) / animation_duration)
        pygame.draw.circle(window, DARK_RED, (button_x + button_radius, button_y_animation + button_radius), button_radius)
        pygame.draw.circle(window, RED, (button_x + button_radius, button_y_animation + button_radius), button_radius - 10)
    else:
        pygame.draw.circle(window, DARK_RED, (button_x + button_radius, button_y + button_radius), button_radius)
        pygame.draw.circle(window, RED, (button_x + button_radius, button_y + button_radius), button_radius - 10)

    # Calculate and display statistics
    if start_time is not None:
        elapsed_time = time.time() - start_time
        clicks_per_second = click_count / elapsed_time
        average_delay = delay_sum / click_count if click_count > 0 else 0
        font = pygame.font.Font(None, 36)
        text = font.render(f"Clicks: {click_count}, CPS: {clicks_per_second:.2f}, Average Delay: {average_delay:.2f}s, Time: {elapsed_time:.2f}s", True, WHITE)
        window.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

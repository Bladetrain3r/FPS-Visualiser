import pygame
import random
import time

def display_frame(screen, color):
    screen.fill(color)
    pygame.display.flip()

def main(fps, fade_frames):
    # Initialize Pygame
    pygame.init()
    
    # Set up display
    screen = pygame.display.set_mode((800, 600))
    
    # Clock for controlling FPS
    clock = pygame.time.Clock()

    # Time to display the frame in seconds
    display_time = 10

    # Determine when to start fading to white
    fade_start_time = random.uniform(0, display_time - (2 * fade_frames / fps))
    
    start_time = time.time()
    color_intensity = 0  # Start with black
    fading_in = True

    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Check elapsed time
        elapsed_time = time.time() - start_time

        # Start fading at the random time point
        if elapsed_time >= fade_start_time and elapsed_time <= fade_start_time + (2 * fade_frames / fps):
            if fading_in:
                color_intensity += 255 // fade_frames
                if color_intensity >= 255:
                    color_intensity = 255
                    fading_in = False
            else:
                color_intensity -= 255 // fade_frames

        # Force back to black after the fade sequence
        if elapsed_time > fade_start_time + (2 * fade_frames / fps):
            color_intensity = 0

        display_frame(screen, (color_intensity, color_intensity, color_intensity))

        # Stop after the designated display time
        if elapsed_time > display_time:
            break

        # Control the frame rate
        clock.tick(fps)

if __name__ == "__main__":
    fps = int(input("Enter the frame rate (FPS): "))
    fade_frames = int(input("Enter the number of frames for the fade: "))
    main(fps, fade_frames)

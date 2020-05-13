import pygame
import random
import sys


def check_if_clicked_coordinates_in_target(
    mouse_coordinates, circle_center, circle_radius
):
    x_start_range = circle_center[0] - circle_radius
    x_end_range = circle_center[0] + circle_radius

    y_start_range = circle_center[1] - circle_radius
    y_end_range = circle_center[1] + circle_radius

    if (x_start_range <= mouse_coordinates[0] <= x_end_range) and (
        y_start_range <= mouse_coordinates[1] <= y_end_range
    ):
        return True

    return False


if __name__ == "__main__":
    pygame.init()
    size = width, height = 500, 500
    radius = 30
    black = 0, 0, 0
    red = 255, 0, 0
    white = 255, 255, 255
    random_center = 0, 0

    screen = pygame.display.set_mode(size)

    score = 0
    attempts = 0
    for _ in range(25):
        pygame.display.set_caption(f"Score: {score}")

        screen.fill(black)

        random_center = (
            random.randint(radius, width - radius),
            random.randint(radius, height - radius),
        )
        for circle_count in range(6, 0, -1):
            if circle_count % 2 == 0:
                circle_color = red
            else:
                circle_color = white
            pygame.draw.circle(
                screen, circle_color, random_center, circle_count * 5
            )
        pygame.display.update()

        clock = pygame.time.Clock()
        waiting = True
        max_wait_time = 3000  # 5 seconds
        start_time = pygame.time.get_ticks()

        while waiting:
            current_time = pygame.time.get_ticks()
            if current_time - start_time >= max_wait_time:
                waiting = False
                break

            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN) and (
                    event.button == 1
                ):
                    attempts += 1
                    mouse_coordinates = pygame.mouse.get_pos()

                    if check_if_clicked_coordinates_in_target(
                        mouse_coordinates, random_center, radius
                    ):
                        score += 1
                        waiting = False
                        break
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    sys.exit()

    pygame.quit()
    print(f"Score: {score}")
    print(f"Accuracy: {score / attempts}")

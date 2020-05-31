import pygame
import random
from math import sqrt


class Circle:
    def __init__(self, screen_width, screen_height, window, circle_radius=30):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = window
        self.radius = circle_radius
        self.red = 255, 0, 0
        self.white = 255, 255, 255
        self.get_new_position_and_draw()

    def draw(self):
        for circle_count in range(6, 0, -1):
            if circle_count % 2 == 0:
                circle_color = self.red
            else:
                circle_color = self.white
            pygame.draw.circle(
                self.screen, circle_color, self.center, circle_count * 5
            )

    def get_new_position(self):
        return (
            random.randint(self.radius, self.screen_width - self.radius),
            random.randint(self.radius, self.screen_height - self.radius),
        )

    def get_new_position_and_draw(self):
        self.center = self.get_new_position()
        self.draw()

    def is_clicked(self, coordinates_clicked):

        x_difference = (coordinates_clicked[0] - self.center[0]) ** 2
        y_difference = (coordinates_clicked[1] - self.center[1]) ** 2

        return sqrt(x_difference + y_difference) <= self.radius


def get_statistics_text(score, attempts, screen_width, screen_height):
    font = pygame.font.Font('freesansbold.ttf', 32)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    texts_and_boxes = []

    score_text = font.render(f'Score: {score}', True, green, blue)
    score_text_rectangle = score_text.get_rect()
    score_text_rectangle.center = (screen_width // 2, screen_height // 2)
    texts_and_boxes.append((score_text, score_text_rectangle))

    if attempts > 0:
        accuracy_text = font.render(f'Accuracy: {round(100*score/attempts, 2)}%', True, green, blue)
    else:
        accuracy_text = font.render('Accuracy: 0%', True, green, blue)
    accuracy_text_rectangle = accuracy_text.get_rect()
    accuracy_text_rectangle.center = (screen_width // 2, screen_height // 2 + score_text_rectangle.height)
    texts_and_boxes.append((accuracy_text, accuracy_text_rectangle))

    play_again_text = font.render('Play Again?', True, green, blue)
    play_again_text_rectangle = play_again_text.get_rect()
    accuracy_text_rectangle.center = (screen_width // 2, screen_height // 2 + accuracy_text_rectangle.height)
    texts_and_boxes.append((play_again_text, play_again_text_rectangle))

    return texts_and_boxes


if __name__ == "__main__":
    pygame.init()
    size = width, height = 500, 500
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    start_game = True
    end_game = False
    score = 0
    attempts = 0

    while not end_game:
        if start_game:
            score = 0
            attempts = 0

            for _ in range(5):
                pygame.display.set_caption(f"Score: {score}")

                screen.fill(black)

                circle = Circle(screen_width=width, screen_height=height, window=screen)

                pygame.display.update()

                clock = pygame.time.Clock()
                waiting = True
                max_wait_time = 2000  # 2 seconds -- change this if you want to increase/decrease difficulty
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

                            if circle.is_clicked(mouse_coordinates):
                                score += 1
                                waiting = False
                                break
                        if event.type == pygame.QUIT:
                            waiting = False
                            end_game = True
                            break

                if end_game:
                    break

            start_game = False

        text_and_boxes = get_statistics_text(score=score, attempts=attempts, screen_width=width, screen_height=height)
        screen.fill(black)
        for text, text_box in text_and_boxes:
            screen.blit(text, text_box)
        pygame.display.update()

        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN) and (
                    event.button == 1
            ):
                mouse_coordinates = pygame.mouse.get_pos()

                if text_and_boxes[-1][1].collidepoint(mouse_coordinates):
                    start_game = True
                    break
            if event.type == pygame.QUIT:
                end_game = True
    pygame.quit()

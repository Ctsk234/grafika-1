import pygame
import sys


class ShapeDrawer:
    def __init__(self, screen):
        self.screen = screen

    def draw_chevron(self, points, color):
        pygame.draw.polygon(self.screen, color, points)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Shape Drawing")
    screen.fill(pygame.Color('white'))
    drawer = ShapeDrawer(screen)

    # Draw Chevron
    # format [((x, y) (x, y) (x, y) (x, y)], (rrr, ggg, bbb))
    drawer.draw_chevron([(350, 250), (450, 250),(450, 350),(400, 300),(350, 350), ], (0, 255, 0))


    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

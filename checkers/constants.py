import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
BLACK_CHECKER = pygame.transform.scale(pygame.image.load('resource/image/black_checker.png'), (SQUARE_SIZE, SQUARE_SIZE))
WHITE_CHECKER = pygame.transform.scale(pygame.image.load('resource/image/white_checker.png'), (SQUARE_SIZE, SQUARE_SIZE))
CROWN = pygame.transform.scale(pygame.image.load('resource/image/crown.png'), (SQUARE_SIZE, SQUARE_SIZE))

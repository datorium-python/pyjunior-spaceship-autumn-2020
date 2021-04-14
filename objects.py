import pygame
import random


class Spaceship:
    # функция в классе называется метод
    # class attribute - общий для всех объектов
    image = pygame.image.load("spaceship.png")
    speed = 0.3

    def __init__(self, x_position, y_position):
        # self.что-то instance attribute - для каждого свой 
        self.x_position = x_position
        self.y_position = y_position
        # x_position_change и y_position_change указывают направление
        self.x_position_change = 0
        self.y_position_change = 0        

    def change_position(self, window):
        if self.x_position <= 0:
            self.x_position = 0

        if self.y_position <= 0:
            self.y_position = 0

        if self.x_position >= window.get_width() - Spaceship.image.get_width():
            self.x_position = window.get_width() - Spaceship.image.get_width()

        if self.y_position >= window.get_height() - Spaceship.image.get_height():
            self.y_position = window.get_height() - Spaceship.image.get_height()

        self.x_position += self.x_position_change
        self.y_position += self.y_position_change

    def draw_spaceship(self, window):
        coordinates = (self.x_position, self.y_position)
        window.blit(Spaceship.image, coordinates)

    
class Missile: 

    # class attribute - общий для всех объектов
    image = pygame.image.load("missile.png")
    speed = -0.7 

    # __init__ создает объект
    # initialize -> создать
    def __init__(self, spaceship):
        # если видием self.аттрибут -> у каждого свое значение у всех отличаются
        self.x_position = spaceship.x_position + (spaceship.image.get_width() / 2)
        self.y_position = spaceship.y_position - Missile.image.get_height()
        
    def change_position(self):
        self.y_position += Missile.speed

    def draw_missile(self, window):
        coordinates = (self.x_position, self.y_position)
        window.blit(Missile.image, coordinates)


class Asteroid: 

    # class attribute - общий для всех объектов
    image = pygame.image.load("asteroid.png")
    speed = 0.5 

    # __init__ создает объект
    # initialize -> создать
    def __init__(self, window):
        # если видием self.аттрибут -> у каждого свое значение у всех отличаются
        self.x_position = random.randint(0, window.get_width() - Asteroid.image.get_width())
        self.y_position = random.randint(-100, 0)
        
    def change_position(self):
        self.y_position += Asteroid.speed

    def draw_asteroid(self, window):
        coordinates = (self.x_position, self.y_position)
        window.blit(Asteroid.image, coordinates)

    def has_colided(self, entity):
        # get rectangle – получить прямоугольник
        asteroid_rect = Asteroid.image.get_rect()
        asteroid_rect.topleft = (self.x_position, self.y_position)

        entity_rect = entity.image.get_rect()
        entity_rect.topleft = (entity.x_position, entity.y_position)

        # return True или False
        return asteroid_rect.colliderect(entity_rect)

        
        
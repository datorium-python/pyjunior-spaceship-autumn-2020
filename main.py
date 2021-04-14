import pygame
from objects import Spaceship, Missile, Asteroid

pygame.init()

BLACK = (0, 0, 0)

SIZE = (480, 715)
ICON = pygame.image.load("asteroid.png")
BACKGROUND = pygame.image.load("stars.jpg")

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Destroy asteroids!")
pygame.display.set_icon(ICON)


def render(spaceship, missiles, asteroids):
    window.fill(BLACK)
    window.blit(BACKGROUND, (0, 0))

    spaceship.draw_spaceship(window)

    for missile in missiles:
        # если список пустой то код просто не выполняется ->
        # программа даже не пытается нарисовать
        missile.draw_missile(window)

    for asteroid in asteroids:
        asteroid.draw_asteroid(window)

    pygame.display.update()

CREATE_ASTEROID_EVENT = pygame.USEREVENT
pygame.time.set_timer(CREATE_ASTEROID_EVENT, 150)

spaceship = Spaceship(x_position=1, y_position=1)
missiles = []
asteroids = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                spaceship.y_position_change = -spaceship.speed
                spaceship.x_position_change = 0
            if event.key == pygame.K_a:
                spaceship.y_position_change = 0
                spaceship.x_position_change = -spaceship.speed
            if event.key == pygame.K_s:
                spaceship.y_position_change = spaceship.speed
                spaceship.x_position_change = 0
            if event.key == pygame.K_d:
                spaceship.y_position_change = 0
                spaceship.x_position_change = spaceship.speed

            if event.key == pygame.K_SPACE:
                missile = Missile(spaceship)
                missiles.append(missile)

        if event.type == CREATE_ASTEROID_EVENT:
            asteroid = Asteroid(window)
            asteroids.append(asteroid)


    spaceship.change_position(window)

    for missile in missiles:
        missile.change_position()

        if missile.y_position <= -missile.image.get_height():
            missiles.remove(missile)

    for asteroid in asteroids:
        asteroid.change_position()

        if asteroid.y_position >= window.get_height():
            asteroids.remove(asteroid)

        for missile in missiles:
            if asteroid.has_colided(missile):
                asteroids.remove(asteroid)
                missiles.remove(missile)
                break



    render(spaceship, missiles, asteroids)


# поменять скорости ЕСТЬ!!!!!!!!!!!!!!!!!!!!!!
# показать взрыв!!!!!!!!! 
# столкнуться с кораблем (здоровье)
# показасть счет и здоворвье
# показать game over
# добавить музыку
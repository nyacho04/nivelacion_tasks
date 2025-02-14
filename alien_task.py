#!/usr/bin/python3
class Alien:
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_coordinate1, new_coordinate2):
        self.x_coordinate = new_coordinate1
        self.y_coordinate = new_coordinate2

    def collision_detection(self, placeholder):
        self.placeholder = 0
        pass

def new_aliens_collection(valores):
    aliens = []
    for valor in valores:
        aliens.append(Alien(valor[0], valor[1]))
    return aliens
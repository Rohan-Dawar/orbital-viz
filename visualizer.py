import pygame as pg
import math

# Screen Surface & Constants
pg.init()
WIDTH = 1024
HEIGHT = 850

WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (200,0,100)
RED = (240,0,0)
ORANGE = (255, 153, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
LGREEN = (30,130,100)
screen = pg.display.set_mode((WIDTH,HEIGHT))

# Sun
class Star:
	def __init__(self, coords, size):
		self.coords = coords #(x,y) tuple of self coordinates
		self.size = size #size (radius) of this planet

	def draw(self):
		pg.draw.circle(screen, ORANGE, self.coords, self.size)

# Planet
class Planet:
	instances = []
	def __init__(self, Ocoords, Oradius, velocity, size, col, distLine):
		self.__class__.instances.append(self)
		self.Ocoords = Ocoords #(x,y) tuple of the coordinates this planet orbits
		self.Oradius = Oradius #radius around which the planet orbits
		self.velocity = velocity #speed at which it orbits
		self.size = size #size (radius) of this planet
		self.col = col #color of planet
		self.distLine = distLine #bool, show distance lines to other planets
		self.x, self.y = (Ocoords[0]-Oradius, Ocoords[1]-Oradius)
		self.coords = (self.x, self.y)
		self.angle = 0

	def motion(self):
		self.angle += 0.001*self.velocity
		self.x = int(math.cos(self.angle) * self.Oradius) + self.Ocoords[0]
		self.y = int(math.sin(self.angle) * self.Oradius) + self.Ocoords[1]
		self.coords = (self.x, self.y)

	def draw(self):
		pg.draw.circle(screen, self.col, self.coords, self.size, 0)

	def draw_orbit(self):
		pg.draw.circle(screen, WHITE, self.Ocoords, self.Oradius, 1)
		if self.distLine:
			otherPlanets = Planet.instances
			if self in otherPlanets:
				otherPlanets.remove(self)
			distlist = [math.sqrt(math.pow(instance.x - self.x, 2) + math.pow(instance.y - self.y, 2)) for instance in otherPlanets]
			ex, ey = Planet.instances[distlist.index(min(distlist))].coords
			pg.draw.line(screen, WHITE, (self.x, self.y), (ex, ey), 1)

	def rend(self):
		self.motion()
		self.draw_orbit()
		self.draw()

SUN = Star((round(WIDTH/2), round(HEIGHT/2)), 20)

EARTH = Planet(SUN.coords, 100, 3, 12, BLUE, True)
MARS = Planet(SUN.coords, 200, 4, 10, RED, False)
SATT = Planet(SUN.coords, 300, 5, 8, PINK, False)
SATT2 = Planet(SUN.coords, 400, 6, 10, LGREEN, False)

# Game Loop
running = True
while running:
	screen.fill(BLACK)
	SUN.draw()
	EARTH.rend()
	MARS.rend()
	SATT.rend()
	SATT2.rend()
	pg.display.update()
	# Quit Game:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				running = False

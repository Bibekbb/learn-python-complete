import pygame
from pygame.locals import *

pygame.init()

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')
 

 #Define Game variable
tile_size = 200

 #Load images
sun_img = pygame.image.load('img/sun.png')
bg_img = pygame.image.load('img/sky.png')

def draw_grid():
	for line in range(0, 6):
		pygame.draw.line(screen,(255,255,255),(0,line*tile_size), (screen_width, line*tile_size))
		pygame.draw.line(screen(255,255,255),(0,line*tile_size,0),(line*tile_size,screen_height))

class world():
	def __init__(self,data):
		self.tile_list = []



	#Load Images
	dirt_img = pygame.image.load('img/dirt.png')
	
	row_count = 0
	for row in data:
		col_count = 0
		for tile in row :
			if tile == 1:
				img = pygame.transform.scale(dirt_img,(tile_size, tile_size))
				img_ract = img.get_rect()
				img_ract.x = col_count*tile_size
				img_ract.y = col_count*tile_size
				tile = (img,img_ract)
				self.tile_list.append(tile_list)
			col_count += 1
		row_count += 1


world_data = [
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
]

run = True
while run:

	screen.blit(bg_img, (0,0))
	screen.blit(sun_img,(100,100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()
	
pygame.quit()


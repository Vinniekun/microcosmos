import json
import pygame
from ImageControl import *

class ObjectsLoaded:

	def __init__(self):
		pass

	def loadEnemies(self):

		with open('../enemies/all_enemies.json') as json_data:
			self.enemies = json.load(json_data)
			self.enemiesImage = dict()

		for key in self.enemies:
			for i in range(0, len(self.enemies[key]["extrastates"]) + 1):
				for j in range(0, self.enemies[key]["nimgs"][i]):

					location = "../graphics/Monsters/" + key + "/" + \
						key + str(j + 1) + ".png"
					if len(self.enemies[key]["extrastates"]) > 0:
						location2 = "../graphics/Monsters/" + key + "/" + \
							self.enemies[key]["extrastates"][i - 1] + str(j + 1) + ".png"
					else:
						location2 = ""

					if i == 0:
						if key not in self.enemiesImage:
							self.enemiesImage[key] = [[]]

						if 'resize' in self.enemies[key].keys():
							resize = self.enemies[key]['resize']
							self.enemiesImage[key][0].append(ImageControl.zoomImage(pygame.image.load(location).convert_alpha(), resize))
						else:
							self.enemiesImage[key][0].append(pygame.image.load(location).convert_alpha())

					else:
						if len(self.enemiesImage[key]) <= i:
							self.enemiesImage[key].append([])
						if 'resize' in self.enemies[key].keys():
							self.enemiesImage[key][i].append(ImageControl.zoomImage(pygame.image.load(location2).convert_alpha(), resize))
						else:
							self.enemiesImage[key][i].append(pygame.image.load(location2).convert_alpha())
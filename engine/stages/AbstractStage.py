from pygame import *
from pygame.locals import *
from Camera import *
from ImageControl import *
from TerrainSurface import *
from Enemy import *
from Entity import *
import sys


class AbstractStage:

	def __init__(self, player, window, nextStageKey, dimensions):
		self.window = window
		self.objects = pygame.sprite.Group()
		self.camera = Camera(self.window.camera, dimensions)
		self.player = player
		self.changeResolution = False
		self.entities = pygame.sprite.Group()
		self.terrains = pygame.sprite.Group()
		self.nextStageKey = nextStageKey
		self.lastTime = pygame.time.get_ticks()
		self.shipPhase = True
		self.blocos = pygame.sprite.Group()

	def object_actions(self, fps):
		for o in self.objects:
			o.action(fps)
			if o.die:
				o.remove(self.objects)

	def collision(self):

		for o in self.objects:
			collision_pos = pygame.sprite.collide_mask(o, self.player)
			if collision_pos is not None:
				o.collision(self.player)

		for e in self.terrains:
			collision_pos = pygame.sprite.collide_mask(e, self.player)
			if collision_pos is not None:
				self.player.isDead = True

	def create_enemies(self, name, position, inverted=False, resize=1):
		enemy = Enemy(name, self.allObjects.enemies[name], self.allObjects.enemiesImage[name], position, self.sound, inverted, resize)
		self.objects.add(enemy)

	def create_terrain(self, stage, nimgs):

		aux = TerrainSurface(stage, "1")
		width = aux.image.get_width()

		self.terrains.add(aux)
		for i in range(2, nimgs):
			aux = TerrainSurface(stage, str(i))
			aux.rect.x = (i - 1) * width
			self.terrains.add(aux)


	def create_background(self, img):
		self.background = pygame.image.load("../graphics/Textures/" + img + ".jpg").convert_alpha()
		self.background = ImageControl.zoomImage(self.background, 1.5)
		self.realbackground = ImageControl.fixScale(self.background)


	def checkIfAppears(self, obj, x=True, y=True):
		xcheck = True
		ycheck = True
		if x:
			if not (obj.rect.x + obj.rect.w >= self.player.rect.x - self.window.screenResolution[0] and obj.rect.x <= self.player.rect.x + self.window.screenResolution[0]):
				xcheck = False
		if y:
			if not (obj.rect.y + obj.rect.h >= self.player.rect.y - self.window.screenResolution[1] and obj.rect.y - obj.rect.h <= self.player.rect.y + self.window.screenResolution[1]):
				ycheck = False
		return xcheck and ycheck


	def scene_imgs(self):
		ImageControl.setImageAt(self.window, self.realbackground, (0, 0))

		try:
			for b in self.blocos:
				if self.checkIfAppears(b):
					self.window.windowScreen.blit(b.image, self.camera.apply(b))
		except AttributeError:
			pass

		for o in self.objects:
			xparam = True
			yparam = True
			if o.name == "pelo":
				yparam = False

			if self.checkIfAppears(o, xparam, yparam):
				if o.rotates:
					image = pygame.transform.rotate(o.image, o.angle)
					self.window.windowScreen.blit(image, self.camera.apply(o))
				else:
					self.window.windowScreen.blit(o.image, self.camera.apply(o))

		for e in self.entities:
			self.window.windowScreen.blit(e.image, self.camera.apply(e))

		for t in self.terrains:
			if self.checkIfAppears(t):
				self.window.windowScreen.blit(t.image, self.camera.apply(t))

		try:
			for i in range(self.player.life):
				self.window.windowScreen.blit(self.player.lifeImage, (80 + 85 * i, 32))
		except:
			pass

	def resizeImages(self):
		for o in self.objects:
			for i in range(len(o.images)):
				for j in range(len(o.images[i])):
					o.actualimages[i][j] = ImageControl.fixScale(o.images[i][j])
			o.atualizeActualImage()

		for e in self.entities:
			for i in range(len(e.images)):
				for j in range(len(o.images[i])):
					e.actualimages[i][j] = ImageControl.fixScale(e.images[i][j])
			e.atualizeActualImage()

		for t in self.terrains:
			t.image = ImageControl.fixScale(t.realimage)

		self.realbackground = ImageControl.fixScale(self.background)


	def fixCameraRect(self):
		w, h = ImageControl.fixValues(self.camera.dimensions[0], self.camera.dimensions[1])
		self.camera.state = Rect(0, 0, w, h)

	def fixResolution(self):
		self.player.updateWindow()
		self.resizeImages()
		self.fixCameraRect()
		self.window.resolutionChange = False
		self.changeResolution = True

	def controlFPS(self):
		time = pygame.time.get_ticks()
		try:
			fps = 1000 / (time - self.lastTime)
		except:
			fps = 50
		self.lastTime = time
		return fps

	def update(self):

		self.window.windowScreen.fill((255, 255, 255))
		fps = self.controlFPS()
		#print("x:" + str(self.player.rect[0]) + "y:" + str(self.player.rect[1]))
		if self.shipPhase:
			self.player.movement(self.checkPressed())
		else:
			self.player.movement_char(self.control.checkPressed(), fps)
			self.player.collision(self.blocos)

		self.player.update(fps)

		if self.window.resolutionChange:
			self.fixResolution()

		self.camera.update(self.player)
		self.scene_imgs()
		self.object_actions(fps)

		pygame.display.flip()
		self.window.windowScreen.fill((255, 255, 255))
		self.collision()
		self.checkIfPlayerDie()

	def checkIfPlayerDie(self):
		if self.player.isDead:
			self.nextStageKey = self.player.death()
			if self.nextStageKey == "Menu":
				self.sound.playSound("fail")
			else:
				self.nextStageKey = self.name
				self.sound.playSound("quack")
				self.player.newLevel(self.player.checkpoint)

	def checkPressed(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				sys.exit()
			elif event.type == VIDEORESIZE:
				self.window.changeResolution(event)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					return "space"
				elif event.key == pygame.K_RIGHT:
					return "right"
				elif event.key == pygame.K_LEFT:
					return "left"
				elif event.key == pygame.K_UP:
					return "up"
				elif event.key == pygame.K_DOWN:
					return "down"
				elif event.key == pygame.K_z:
					return "z"

	def update_intros(self):
		#self.window.windowScreen.fill((255, 255, 255))
		fps = self.controlFPS()
		if self.window.resolutionChange:
			self.fixResolution()
		pygame.display.flip()
		self.window.windowScreen.fill((0, 0, 0))
		self.collision()
		return fps

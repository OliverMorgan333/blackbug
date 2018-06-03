import time
import random
import numpy as np
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle #for testing
from kivy.core.window import Window
from kivy.uix.label import Label

class settings:
	#adjust screen_size
    def __init__(self):
        self.screen_size = 1.5
        self.display_width_dim = 1334
        self.display_height_dim = 750
        self.display_width = int(self.display_width_dim*self.screen_size)
        self.display_height = int(self.display_height_dim*self.screen_size)

s = settings()
class Sprite(Image):
	def __init__(self, **kwargs):
		super(Sprite, self).__init__(allow_stretch=True, **kwargs)
		self.size = self.texture_size

class ani:
	#Class that can create widget and display animations.
	#Uses an instance from the fighter class to be able to use widgets.
	def __init__(self, s, image, folder, repeating, N):
		self.N = N
		self.s = s
		self.image = image
		self.repeating = repeating
		self.folder = folder
		self.x_from_edge = 120
		self.y_from_edge = 30
		self.l_i = 0

		self.initted = False
		self.N

	def __call__(self):
		#Initiates the first image in the animation, then rolls trough them
		#untill the last where it starts over
		if not self.initted:
			self.init2()
			
		self.image.source = \
				'atlas://img/fighter/'+self.folder+'/myatlas/img_%i' % self.l_i
		if self.l_i < self.N:
			self.l_i += 1
			return True
		else:
			self.l_i = 0
			if self.repeating:
				self.l_i = 1
				return True

	def init2(self):
		self.image.pos = self.x_from_edge, self.y_from_edge
		self.image.size = self.image.texture_size
		self.s.add_widget(self.image)
		self.initted = True


		
class fighter_images(Widget):
	#string = 'subclass of image_positioning-settings'
	def __init__(self, **kwargs):
		super(fighter_images, self).__init__(**kwargs)
		self.l_idle_img = Sprite(
			source ='atlas://img/fighter/idle/myatlas/img_0')

		self.myani_idle = ani(self, self.l_idle_img, 'idle', True, 8)

class Game(fighter_images):
	def __init__(self, **kwargs):
		fighter_images.__init__(self)

		# Here I add a buttons as a background to show the error (works fine).
		turn = Button(text ='turn', font_size = 14, pos = [300, 0],
					  size = [300, 50])
		self.add_widget(turn)
		#____________________________________________________________________
		Clock.schedule_interval(self.update, 1/15.)
		
	def update(self, *ignore):
		self.myani_idle()

class gameApp(App):
	def build(self):
		game = Game()
		Window.size = [s.display_width, s.display_height]
		return game

if __name__ == '__main__':
	gameApp().run()






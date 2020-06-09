import pygame
import numpy as np
import itertools


class Mandelbrot:
	def __init__(self, dim, iterations, center, extent, zoom, z=complex(0, 0)):
		self.iterations = iterations
		self.center = center
		self.ratio = float(dim[0] / dim[1])
		self.extent = [extent[0] * self.ratio, extent[1]]
		self.zoom = zoom
		self.x_min, self.x_max = (self.center[0] - (self.extent[0]//2)/zoom)*self.ratio,\
		                         (self.center[0] + (self.extent[0]//2)/zoom)*self.ratio
		self.y_min, self.y_max = (self.center[1] - (self.extent[1]//2)/zoom)*self.ratio,\
		                         (self.center[1] + (self.extent[1]//2)/zoom)*self.ratio
		self.scale_x, self.scale_y = float((self.extent[0])/dim[0]/zoom)*self.ratio,\
		                             float((self.extent[1])/dim[1]/zoom)*self.ratio
		self.dim = dim
		self.z = z
		#self.coordinates = list(itertools.product(np.linspace(self.x_min, self.x_max, num=round(self.dim[0])),
		#                                          np.linspace(self.y_min, self.y_max, num=round(self.dim[1]))))

	def get_vector(self, pos):
		return [(self.x_min + pos[0] * self.scale_x)/self.ratio, ( self.y_min + pos[1] * self.scale_y)/self.ratio]

	def draw(self, screen):
		pixel_array = pygame.PixelArray(screen)
		for x in range(self.dim[0]):
			for y in range(self.dim[1]):
				z = complex(self.x_min + x * self.scale_x, self.y_min + y * self.scale_y)
				value = self.main_function(x, y, z)
				if value == self.iterations:
					pix_color = pygame.Color(0, 0, 0, 255)
				else:
					col = round(value/self.iterations * 255)
					pix_color = pygame.Color(col, col, col, 255)
				pixel_array[x, y] = pix_color
		del pixel_array

	def main_function(self, x, y, z):
		self.z = complex(self.x_min + x * self.scale_x, self.y_min + y * self.scale_y)
		count = 0
		while count <= self.iterations:
			if z.real*z.real + z.imag*z.imag > 4.0:
				return count
			z = complex(z*z + self.z)
			count += 1
		return self.iterations


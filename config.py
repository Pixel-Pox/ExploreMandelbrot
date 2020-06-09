from mandelbrot import Mandelbrot
import pygame as pg

#Global variables
dim = (1200, 800)
ratio = float(dim[0]/dim[1])
iterations = 16
center = [0, 0]
extent = [4, 4]
zoom = 1
screen = pg.display.set_mode(dim)
mandelbrot = Mandelbrot(dim, iterations, center, extent, zoom)
changed = False
bp_center = [0,0]
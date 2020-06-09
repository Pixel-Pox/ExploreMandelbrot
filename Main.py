import pygame as pg
import config as cn
import functions as fn

#Main loop
def run_program():
	pg.init()
	cn.mandelbrot.draw(cn.screen)
	pg.display.set_caption("Mandelbrot set")
	while True:
		fn.check_events()
		pg.display.update()

run_program()

import pygame as pg
import sys
import config as cn
from mandelbrot import Mandelbrot
import numpy as np
import time


def check_events():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				cn.center[0] += 1/cn.zoom
				print('Center moved to the right. Current center: ' + str(cn.center))
			elif event.key == pg.K_LEFT:
				cn.center[0] -= 1/cn.zoom
				print('Center moved to the left. Current center: ' + str(cn.center))
			elif event.key == pg.K_UP:
				cn.center[1] -= 1/cn.zoom
				print('Center moved up. Current center: ' + str(cn.center))
			elif event.key == pg.K_DOWN:
				cn.center[1] += 1/cn.zoom
				print('Center moved down. Current center: ' + str(cn.center))
			elif event.key == pg.K_SPACE:
				start_time = time.time()
				print('Preparing Mandelbrot array...')
				Mandelbrot(cn.dim, cn.iterations, cn.center, cn.extent, cn.zoom).draw(cn.screen)
				cn.changed = False
				end_time = time.time() - start_time
				print('Array ready. Time: ' + str(end_time))
			elif event.key == pg.K_KP_PLUS:
				cn.iterations *= 2
				print('Current iterations increased to: ' + str(cn.iterations))
			elif event.key == pg.K_KP_MINUS:
				cn.iterations /= 2
				print('Current iterations decreased to: ' + str(cn.iterations))
			elif event.key == pg.K_q:
				cn.zoom *= 2
				print('Zoom increased. Current zoom: ' + str(cn.zoom))
			elif event.key == pg.K_e:
				cn.zoom /= 2
				print('Zoom decreased. Current zoom: ' + str(cn.zoom))
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				print('Aligning to new center...')
				move_vector = np.divide(cn.mandelbrot.get_vector(np.array(pg.mouse.get_pos())), cn.zoom)
				print(pg.mouse.get_pos())
				if not cn.changed:
					cn.bp_center = cn.center
					cn.center = np.add(move_vector, cn.center)
					cn.changed = True
				else:
					cn.center = cn.bp_center
					cn.center = np.add(move_vector, cn.center)
					cn.changed = True
				print("New center is: " + str(cn.center) + '. Moved by vector of: ' + str(move_vector))

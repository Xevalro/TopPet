import pygame as pg
from pygame import *
import win32api
import win32con
import win32gui
from threading import *
import threading
from time import *
import time

pg.init()

# Window Settings

screen = pg.display.set_mode((300, 300), NOFRAME)
bgColor = (255, 0, 128)  # Transparency color
hwnd = pg.display.get_wm_info()["window"] # Create layered window
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*bgColor), 0, win32con.LWA_COLORKEY) # Set window transparency color
pg.display.set_caption("Top Pet V.3")

# Variables

done = False

while not done:

    screen.fill(bgColor)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

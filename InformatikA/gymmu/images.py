from ipycanvas import Canvas, MultiCanvas
from PIL import Image
from math import sqrt
import requests

import numpy as np
from io import BytesIO


def load_image_data(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return (np.array(img.getdata()).reshape(-1).tolist(), img.width)


def make_image():
    c = Canvas(width=200, height=200)
    c.sync_image_data = True
    return c

def draw_grid(canvas, SCALE_FACTOR=20):
    mc = MultiCanvas(2, width=canvas.width, height=canvas.height, sync_image_data=True)
    mc[0].put_image_data(canvas.get_image_data(), 0, 0)
    grid = mc[1]
    ran = range(0,mc.width,SCALE_FACTOR)
    for x in ran:
        for y in ran:
            grid.stroke_rect(x, y, SCALE_FACTOR)
    return mc

def _get_gray(data):
    if data[3] == 0:
        return 1
    else:
        return (sum(data[0:3]) / 3) / 255

def get_image_data(canvas):
    data = canvas.get_image_data()
    return _get_greyscale(data)

def _get_greyscale(data):
    data = np.reshape(data, -1)
    data = np.array([_get_gray(data[i:i+4]) for i in range(0, len(data), 4)])
    return data

def write_image_from_data(data):
    l = len(data)
    side = int(sqrt(l))
    scale = 150 / side

    data = np.array(data) * 255

    newdata = np.zeros((150,150))
    data = np.reshape(data, (side, side))

    for x in range(150):
        for y in range(150):
            newdata[x][y] = data[int(x // scale)][int(y // scale)]

    c = Canvas(width=150, height=150, sync_image_data=True)
    alpha = np.zeros((150, 150)) + 255
    rgb_data = np.stack([newdata, newdata, newdata, alpha], axis=2)
    c.put_image_data(rgb_data, 0, 0)
    return c


def write_image_from_data_colored(data):
    l = len(data) / 3
    side = int(sqrt(l))
    scale = 150 / side

    data = np.array(data) * 255

    newdata = np.zeros((150,150, 3))
    data = np.reshape(data, (side, side, 3))

    for x in range(150):
        for y in range(150):
            for i in range(3):
                newdata[x][y][i] = data[int(x // scale)][int(y // scale)][i]

    c = Canvas(width=150, height=150, sync_image_data=True)
    alpha = np.zeros((150, 150)) + 255
    rgb_data = np.stack([newdata[:,:,0], newdata[:,:,1], newdata[:,:,2], alpha], axis=2)
    c.put_image_data(rgb_data, 0, 0)
    return c


def write_image_from_data_rgb(data):
    l = len(data) / 3
    side = int(sqrt(l))
    scale = 150 / side

    data = np.array(data)

    newdata = np.zeros((150,150, 3))
    data = np.reshape(data, (side, side, 3))

    for x in range(150):
        for y in range(150):
            for i in range(3):
                newdata[x][y][i] = data[int(x // scale)][int(y // scale)][i]

    c = Canvas(width=150, height=150, sync_image_data=True)
    alpha = np.zeros((150, 150)) + 255
    rgb_data = np.stack([newdata[:,:,0], newdata[:,:,1], newdata[:,:,2], alpha], axis=2)
    c.put_image_data(rgb_data, 0, 0)
    return c


def write_image_rgb(data, width):
    l = len(data) / 3
    height = int(l / width)

    data = np.array(data)

    data = np.reshape(data, (height, width, 3))

    c = Canvas(width=width, height=height, sync_image_data=True)
    # alpha = np.zeros((width, height)) + 255
    # rgb_data = np.stack([data[:,:,0], data[:,:,1], data[:,:,2], alpha], axis=2)
    c.put_image_data(data, 0, 0)
    return c


def write_image_grey(data, width):
    l = len(data)
    height = int(l / width)

    data = np.array(data)

    data = np.reshape(data, (height, width, 1))

    c = Canvas(width=width, height=height, sync_image_data=True)
    grey_data = np.stack([data[:,:,0], data[:,:,0], data[:,:,0]], axis=2)
    c.put_image_data(grey_data, 0, 0)
    return c


def get_example_data():
    i = Image.open('res/simple_image.png')
    return _get_greyscale(np.asarray(i))


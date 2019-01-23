import argparse
import logging
import math

import numpy as np
from PIL import Image

from .helpInfo import info

logger = logging.getLogger(__name__)
logger.level = logging.ERROR

long_ascii_map = r"$@B%8&WM" + \
        "#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
long_ascii_map = long_ascii_map[::-1]
short_ascii_map = r" .:-=+*#%@"


def _mapping_ascii(color):
    step = float(255) / float(len(long_ascii_map))
    rank = float(color) / step
    rank = math.ceil(rank)-1 if color != 0 else 0
    return long_ascii_map[rank]


def _open_image(filepath):
    return Image.open(filepath).convert("L")


def _avgImage(image):
    image = np.array(image)
    return round(np.average(image.reshape(-1)))


def _scan(image, size):
    W, H = image.size
    w_gap, h_gap = size

    ret_arr = []
    for y in range(0, H, h_gap):
        for x in range(0, W, w_gap):

            start_x = x
            start_y = y
            end_x = x+w_gap if x+w_gap <= W else W
            end_y = y+h_gap if y+h_gap <= H else H

            ci = image.crop((start_x, start_y, end_x, end_y))
            avg = _avgImage(ci)

            ascii_chr = _mapping_ascii(avg)
            ret_arr.append(ascii_chr)

        yield ret_arr
        ret_arr.clear()


def _toFile(filepath, line):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("".join([i for i in line])+"\n")


def toASCII(imagePath=None, outFilePath=None, scale=(5, 5)):
    image = _open_image(imagePath)
    for l in _scan(image, scale):
        _toFile(outFilePath, l)


__all__ = ["toASCII", ]

# fanart_generator.py - tool for generating fanart image from set of icons
#
# Copyright 2015 kharts (https://github.com/kharts)
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

"""
fanart_generator.py - tool for generating fanart image from set of icons

Usage:
python fanart_generator [icons_folder [output_file]]

Example:
python fanart_generator "img" "fanart.jpg"
"""

__author__ = 'kharts'

import sys
import os
from PIL import Image

width = 1920
height = 1080
icon_size = 100
offset = 2

def create_fanart(icons_folder="img", output_file="fanart.jpg"):
    """
    Creates fanart image from set of icons
    :param image_folder: str - path to folder with icons
    :param output_file: str - path to output file
    :return: None
    """

    icons = []
    for (dirpath, dirnames, filenames) in os.walk(icons_folder):
        for filename in filenames:
            icon_file_name = os.path.join(dirpath, filename)
            icon = Image.open(icon_file_name, "r")
            icons.append(icon)
    y = 0
    start_i = 0
    max_i = len(icons) - 1
    target = Image.new("RGBA",(width, height),(255,255,255,255))
    while y < width:
        i = start_i
        x = 0
        while x < width:
            icon = icons[i]
            target.paste(icon, (x, y))
            i = shift(i, 1, max_i)
            x = x + icon_size
        y = y + icon_size
        start_i = shift(start_i, offset, max_i)
    target.save(output_file)


def shift(i, delta, max_i):
    if (i + delta) < max_i:
        new_i = i + delta
    else:
        new_i = i + delta - max_i
    return new_i


if __name__ == "__main__":
    icons_folder = "img"
    output_file = "fanart.jpg"
    if len(sys.argv) > 1:
        icons_folder = sys.argv[1]
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
    create_fanart(icons_folder, output_file)



# -*- coding: utf-8 -*-
import os
import math
import dobblo
from random import shuffle
from PIL import Image, ImageDraw

def build_set(num_of_elements):
    path = os.path.dirname(os.path.abspath(__file__))
    total_simbols = num_of_elements ** 2 - (num_of_elements - 1)
    simbols = range(total_simbols)
    dobblo_set = dobblo.init_game(num_of_elements, simbols)
    card_num = 1
    for card in dobblo_set:
        shuffle(card)
        build_card(card_num, num_of_elements, card, '%s/images/' % path)
        card_num = card_num + 1

def build_card(card_num, num_of_elements, card_elem, path):
    size = 600
    card = Image.new('RGBA', (size, size), (255, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    center = size / 2
    r = 220
    delta = 2 * math.pi / (num_of_elements - 1)
    i = 1
    while i < num_of_elements:
        angle = i * delta
        fix = center - hypotenuse(64, 64) 
        x = int(r * math.cos(angle) + fix)
        y = int(r * math.sin(angle) + fix)
        rotation_deg = math.degrees(angle * -1 - math.pi / 2)
        sim = prepare(Image.open(path + '%s.png' % card_elem[i])).rotate(rotation_deg)
        card.paste(sim, (x, y), sim)
        i = i + 1
    sim = Image.open(path + '%s.png' % card_elem[0])
    card.paste(sim, (round(center - 64), round(center - 64)))
    draw.ellipse((1, 1, size - 1, size - 1), outline=(255,255,255,255))
    card.save('./result/kardo-%s.png' % card_num, 'PNG')

def prepare(image):
    (w, h) = image.size
    hyp = hypotenuse(w, h)
    x = round((hyp - w) / 2)
    y = x
    new_img = Image.new('RGBA', (hyp, hyp), (255, 0, 0, 0))
    new_img.paste(image, (x, y))
    return new_img

def hypotenuse(co, ct):
    hyp = round(math.sqrt(co**2 + ct**2))
    return hyp

def main():
    build_set(8)

if __name__ == '__main__':
    main()

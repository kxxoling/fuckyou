#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys


def flip(char):
    chars =   [' ', '-', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    flipped = [' ', '-', '_', 'ɐ', 'q', 'ɔ', 'p', 'ǝ', 'ɟ', 'ɓ', 'ɥ', 'ı', 'ɾ', 'ʞ', 'l', 'ɯ', 'u', 'o', 'd', 'b', 'ɹ', 's', 'ʇ', 'n', 'ʌ', 'ʍ', 'x', 'ʎ', 'z', '⇂', 'ᄅ', 'Ɛ', 'ㄣ', 'ގ', '9', 'ㄥ', '8', '6', '0']
    flipped_dict = dict(zip(chars, flipped))
    return flipped_dict[char]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.argv[0] = ''
        origin_string = list(' '.join(sys.argv))
        flipped_string = ''.join(map(flip, origin_string)[::-1])
        print '(╯°□°）╯︵' + flipped_string
    else:
        print '(；￣Д￣) . o O( It’s not very effective... )'
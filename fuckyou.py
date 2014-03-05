#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys


def flip(char):
    chars = u' -_abcdefghijklmnopqrstuvwxyz1234567890'
    flipped = u' -_ɐqɔpǝɟɓɥıɾʞlɯuodbɹsʇnʌʍxʎz⇂ᄅƐㄣގ9ㄥ860'
    flipped_dict = dict(zip(chars, flipped))
    return flipped_dict[char]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.argv[0] = ''
        origin_string = list(' '.join(sys.argv))
        try:
            flipped_string = ''.join(map(flip, origin_string)[::-1])
            print '(╯°□°）╯︵' + flipped_string
        except KeyError:
            print 'Only lower letters accepted!'
    else:
        print '(；￣Д￣) . o O( It’s not very effective... )'
import argparse
import math

def parse_args ():
    parse = argparse. ArgumentParser(description='Calculate cone volume')
    parse.add_argument('-r', '--radius', default= 5, type=int, metavar='', required=True, help='radius of cone')
    parse.add_argument('-H', '--height', default= 8, type=int, metavar='', required=True, help='height of cone')
    args = parse.parse_args ()
    return args

def calculate_vol(radius, height):
    volume = math. pi * pow (radius, 2) * height / 3
    return volume

#!/usr/bin/env python3
import argparse
from secrets import randbelow as rnd


parser = argparse.ArgumentParser(description='Creates a String to be used as a password, default is 32 characters in '
                                             'length and including integers, lower case, upper case and special '
                                             'characters. Syntax: "pwgen -luns --size 64" ')

parser.add_argument('-l', '--lowercase', help='String excludes lowercase letters', action="store_true")
parser.add_argument('-u', '--uppercase', help='String excludes uppercase letters', action="store_true")
parser.add_argument('-n', '--numbers', help='String excludes numbers', action="store_true")
parser.add_argument('-s', '--special', help='String excludes special characters', action="store_true")
parser.add_argument('--size', help='sets the length of the String', type=int, default=32)

args = parser.parse_args()
blacklist = [96]


def pwgen(i):
    pw = ""
    while len(pw) < i:
        tmp_rnd = rnd(126 - 33) + 33
        if tmp_rnd not in blacklist:
            pw = pw + chr(tmp_rnd)

    return pw


if args.lowercase:
    blacklist = blacklist + [*range(97, 122+1)]


if args.uppercase:
    blacklist = blacklist + [*range(65, 90+1)]


if args.numbers:
    blacklist = blacklist + [*range(48, 57+1)]


if args.special:
    blacklist = blacklist + [*range(33, 47+1)] + [*range(58, 64+1)] + [*range(91, 96+1)] + [*range(123, 126+1)]


if args.special and args.lowercase and args.uppercase and args.numbers:
    exit()

print(pwgen(args.size))

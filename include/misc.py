#!/usr/bin/env python3

import shutil
import sys

COLOR = { "R" : "\033[1;31m", "G" : "\033[1;32m", "B" : "\033[1;36m", "Y" : "\033[1;33m", "END" : "\033[0m" }

VERSION = open("VERSION", "r").read().strip()

def tprint(code, str):
	print(COLOR[code] + "[+] " + COLOR["END"] + str)

 
def print_row():

	for n in range(0, shutil.get_terminal_size((80,20)).columns):
		sys.stdout.write("-")
	sys.stdout.write("\n")

def banner():

        print("\t -- binmagic %s --\n" % VERSION)
        print("\t\t@_x90__\n")

def usage():

        banner()

        print("Usage: %s [options]\n" % sys.argv[0])

        print("Options:")
        print("\t-i [input]\tAnalyse structures inside")
        print("\t-a\t\tAuto extract everything identified. (Recommended)\n")
        exit(1)


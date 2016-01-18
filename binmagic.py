#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.realpath(".") + "/include")

import binutils
import binstructures

VERSION = open("VERSION", "r").read().strip()

def banner():

	print("\t -- binmagic %s --\n" % VERSION)
	print("\t\t@_x90__\n")

def usage():

	banner()

	print("Usage: %s [options]\n" % sys.argv[0)

	print("Options:")
	print("\t-i [input image/binary]")
	print("\t-a\tAnalyse the image for recognised files.")
	print("\t-e\tAnalyse and auto extract everything. (Recommended)\n")
	exit(1)

if __name__ == "__main__":


	if "-i" not in sys.argv:
		usage()	

	bh = binutils.binhandler(sys.argv[1])
	bs = binstructures.binStruct()

	print(bs.get_header("SQUASHFS"))
	
	bh.extractObject(0, 0x10, "output.binary")



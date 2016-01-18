#!/usr/bin/env python

import sys
import os
import struct

sys.path.append(os.path.realpath(".") + "/include")

import binutils
import binstructures

VERSION = open("VERSION", "r").read().strip()

def banner():

	print("\t -- binmagic %s --\n" % VERSION)
	print("\t\t@_x90__\n")

def usage():

	banner()

	print("Usage: %s [options]\n" % sys.argv[0])

	print("Options:")
	print("\t-i [input image/binary]")
	print("\t-a\tAnalyse the image for recognised files.")
	print("\t-e\tAnalyse and auto extract everything. (Recommended)\n")
	exit(1)

def scan_for_struct(image_file):

	bh = binutils.binhandler(image_file).getHandle()
	bs = binstructures.binStruct()

	for key,value in bs.struct_defs.iteritems():

		for inner_key,inner_value in value.iteritems():

			while(True):
				read = struct.unpack("<4s", bh.read(4))
				#print read
				if read in value["HEADER"]:
					
					print "found"
					exit(1)
			
if __name__ == "__main__":


	if "-i" not in sys.argv:
		usage()	
	
	image_file = sys.argv[sys.argv.index("-i")+1]

	scan_for_struct(image_file)

	#print(bs.get_header("SQUASHFS"))
	
	#bh.extractObject(0, 0x10, "output.binary")



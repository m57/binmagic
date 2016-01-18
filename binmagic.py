#!/usr/bin/env python

import sys
import os
import struct

sys.path.append(os.path.realpath(".") + "/include")

import binutils
import binstructures

VERSION = open("VERSION", "r").read().strip()

structures_identified = {}

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


def report_found(key, header, read_offset):

	if key == "SQUASHFS"

def parse_header(

def scan_for_headers(image_file):

	bh = binutils.binhandler(image_file)
	bhandle = bh.getHandle()
	bs = binstructures.binStruct()
	found = 0

	for key,value in bs.struct_defs.iteritems():
		#print "Doing %s" % key
		found = 0
		while not (found):

			read = bhandle.read(4)

			if read in value["HEADER"]:
				report_found(key, read, bhandle.tell()-0x4)
				found = 1

		bh.handleSeek(0)
			
if __name__ == "__main__":


	if "-i" not in sys.argv:
		usage()	
	
	image_file = sys.argv[sys.argv.index("-i")+1]

	scan_for_headers(image_file)

	#print(bs.get_header("SQUASHFS"))
	
	#bh.extractObject(0, 0x10, "output.binary")



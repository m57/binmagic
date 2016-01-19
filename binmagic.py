#!/usr/bin/env python3

import sys
import os
import struct
import time

sys.path.append(os.path.realpath(".") + "/include")

import binutils
import binstructures
import misc

structures_identified = {}

def report_found(key, read_offset, bhandle, bh, bs):

	if key == "SQUASHFS":

		BE 	= 0 # big-endian
		LE 	= 0 # little-endian

		bhandle.seek(read_offset)

		sqsh = struct.unpack("<4s", bhandle.read(4))[0]

		if sqsh == bs.struct_defs["SQUASHFS"]["HEADER"][0]:
			BE = 1
		elif sqsh == bs.struct_defs["SQUASHFS"]["HEADER"][1]:
			LE = 1
		else:
			misc.tprint("R", "Error identifying SQUASHFS Endianness. May cause errors")
	
		
		title 		= bs.struct_defs[key]["TITLE"]
		size 		= struct.unpack("<LL", bh.readBytes(read_offset + bs.struct_defs[key]["SIZE"][0], bs.struct_defs[key]["SIZE"][1]))[0]
		blocksize	= struct.unpack("<L", bh.readBytes(read_offset + bs.struct_defs[key]["BLOCKSIZE"][0], bs.struct_defs[key]["BLOCKSIZE"][1]))[0]	
		inodes		= struct.unpack("<L", bh.readBytes(read_offset + bs.struct_defs[key]["INODES"][0], bs.struct_defs[key]["INODES"][1]))[0]	
		version_maj	= struct.unpack("<H", bh.readBytes(read_offset + bs.struct_defs[key]["VERSION_MAJ"][0], bs.struct_defs[key]["VERSION_MAJ"][1]))[0]
		version_min	= struct.unpack("<H", bh.readBytes(read_offset + bs.struct_defs[key]["VERSION_MIN"][0], bs.struct_defs[key]["VERSION_MIN"][1]))[0]
		method		= bs.struct_defs[key]["METHOD_MAPS"][struct.unpack("<H", bh.readBytes(read_offset + bs.struct_defs[key]["METHOD"][0], bs.struct_defs[key]["METHOD"][1]))[0]]
		endianness 	= "Little-endian" if LE else "Big-endian" if BE else "Unknown endianness"

		structures_identified[read_offset] = [ title, size ]
		
		print("%s%s%s:\t%s v%s.%s (%s) compression (%s) inodes(%d) blocksize(%d) size (%s)" % ( misc.COLOR["G"], hex(read_offset), misc.COLOR["END"], title, version_maj, version_min, endianness, method, inodes, blocksize, size))
		bhandle.seek(read_offset + size)

def extract_and_write(bh, image_file):

	misc.tprint("B", "Extracting file structures identified...")

	for key in structures_identified:

		bh.extractObject(key, structures_identified[key][1], "%s.squashfs" % image_file)
	print("")	

def scan_for_headers(image_file, bh, bs, bhandle):

	misc.print_row()

	file_size = bh.file_size

	for key in bs.struct_defs.keys():
		bhandle.seek(0)
		
		while ( (bhandle.tell() < file_size) ):
			bytes_read = bhandle.read(4)
			if bytes_read in bs.struct_defs[key]["HEADER"]:
				report_found(key, bhandle.tell()-0x4, bhandle, bh, bs)
								
	misc.print_row()		
	print("")

if __name__ == "__main__":


	start_time = time.time()

	# Command line args ####################

	if "-i" not in sys.argv:
		misc.usage()	

	image_file = sys.argv[sys.argv.index("-i")+1]

	if not os.path.exists(image_file):
		misc.tprint("R", "Error accessing file '%s'" % image_file)
		exit(1)

	auto_ex = 1 if "-e" in sys.argv else 0

	#########################################

	misc.banner() 
	
	misc.tprint("B", "Starting analysis on file '%s'\n" % image_file)

	bh 	= binutils.binhandler(image_file)
	bhandle = bh.getHandle()
	bs 	= binstructures.binStruct()

	scan_for_headers(image_file, bh, bs, bhandle)

	if auto_ex:
		extract_and_write(bh, image_file)

	misc.tprint("B", "Analysis finished ( %s seconds )" % (round(time.time() - start_time, 2)))




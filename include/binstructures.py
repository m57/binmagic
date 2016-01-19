#!/usr/bin/env python3
#
#
#
# STRUCTURE NOTATION:
#
# struct_defs {} -> NAME -> {} -> "HEADERS" etc
#
# SQUASHFS (LITTLE ENDIAN not shown below):
#
#	0x0 	: sqsh
#	0x4 	: inodes "<L"
#	0x8	: CTime "<L"
#	0x0c	: blocksize "<L"
#	0x10	: numfrags "<L"
#	0x14	: Method (LZMA,ZLIB etc
#	0x1c	: version "<L"
#	0x28 	: size "<LL" 
#
#

class binStruct(object):

	def __init__(self):

		self.struct_defs = { 

			"SQUASHFS2"	: { 
						"TITLE" : "SquashFS",
						"HEADER" : [ b'sqsh', b'hsqs' ],
						"INODES" : [ 0x4, 0x4 ],
						"BLOCKSIZE" : [ 0x0c, 0x4 ],
						"VERSION_MAJ" : [ 0x1c, 0x2 ], 
						"VERSION_MIN" : [ 0x1e, 0x2 ], 
						"SIZE" : [ 0x28, 0x8 ],
						"METHOD" : [ 0x14, 0x2 ],
						"METHOD_MAPS" : ["UNKNOWN", "ZLIB", "LZMA", "LZO", "XZ"]
			},
			"SQUASHFS"	: { 
						"TITLE" : "SquashFS",
						"HEADER" : [ b'sqsh', b'hsqs' ],
						"INODES" : [ 0x4, 0x4 ],
						"BLOCKSIZE" : [ 0x0c, 0x4 ],
						"VERSION_MAJ" : [ 0x1c, 0x2 ], 
						"VERSION_MIN" : [ 0x1e, 0x2 ], 
						"SIZE" : [ 0x28, 0x8 ],
						"METHOD" : [ 0x14, 0x2 ],
						"METHOD_MAPS" : ["UNKNOWN", "ZLIB", "LZMA", "LZO", "XZ"]
			}

		}

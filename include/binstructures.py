#!/usr/bin/env python


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
#	0x1c	: version "<L"
#	0x40 	: size "<LL" 
#	0x70	: start of squashFS
#
#

class binStruct(object):

	def __init__(self):
		self.struct_defs = { 

			"SQUASHFS"	: { 
						"HEADER" : ['sqsh', 'hsqs'],
						"INODES" : 0x4,
						"BLOCKSIZE" : 0x0c,
						"VERSION" : 0x1c, 
						"SIZE" : 0x40,
						"METHOD" : ["UNKNOWN", "ZLIB", "LZMA", "LZO", "XZ"]
			}
			
		}

#	def parse_squashfs(self):

	def get_header(self, index):
		return self.struct_defs[index][0][0]

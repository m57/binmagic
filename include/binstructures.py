#!/usr/bin/env python

class binStruct(object):

	def __init__(self):
		self.struct_defs = { 

			"SQUASHFS"	: [ '\x73\x68\x73\x71' ], 
			"JFFS2"		: [ '' ] 

		}

	def get_header(self, index):
		return self.struct_defs[index][0]

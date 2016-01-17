#!/usr/bin/env python
#
#
#

import sys
import binStructures

class binhandler(object):

    def __init__(self, filename):

        self.file = open(filename, "rb")

    def readByteAtOffset(self, offset):

        self.file.seek(offset) # This is in hex
        byte = self.file.read(1)
        self.file.seek(0)
        return byte

    def readBytes(self, offset, len):

        self.file.seek(offset)
        byteArray = self.file.read(len)
        self.file.seek(0)
        return byteArray


if __name__ == "__main__":

    #bh = binhandler(sys.argv[1])
    #y = bh.readByteAtOffset(0x10)
    #x = bh.readBytes(0, 0x5)
    #bytecmp = lambda x,y : True if x == y else False
    #print(bytecmp(y.hex(), 0x34))

    print(binStructures.structs["SQUASHFS"][0]) 

#!/usr/bin/env python

import misc

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

    def extractObject(self, start, length, output):
    
        self.file.seek(start)

        try:
       	    f = open(output, "wb")
        except:
            misc.tprint("R", "Error opening file '%s'" % output)
        
        f.write(self.file.read(length))
        misc.tprint("G", "File '%s' successfully written. (%d bytes)" % (output, length))
        f.close()

        self.file.seek(0)
    

    def getHandle(self):
        return self.file

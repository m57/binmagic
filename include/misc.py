#!/usr/bin/env python

COLOR = { "R" : "\033[1;31m", "G" : "\033[1;32m", "B" : "\033[1;33m", "END" : "\033[0m" }

def tprint(code, str):
	print(COLOR[code] + "[+] " + COLOR["END"] + str)

 

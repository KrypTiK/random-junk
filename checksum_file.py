#!/usr/bin/env python

from sys import argv,exit
from hashlib import md5,sha1,sha256

def all(file):
   exit(
        "MD5: "+md5(open(file, 'rb').read()).hexdigest()
	    +"\n"+
	    "SHA1: "+sha1(open(file, 'rb').read()).hexdigest()
	    +"\n"+
    	"SHA256: "+sha256(open(file, 'rb').read()).hexdigest()
	)

if __name__=="__main__":
	
	if len(argv) != 3:
		print "Usage: python %s <file> <hash type>\n"%argv[0]
		exit("Supported hash types\nall\nmd5\nsha1\nsha256")

	if 'all' in argv[2]:
		all(argv[1])
		
	hash = {'md5':md5,'sha1':sha1,'sha256':sha256}
		
	try:	
		exit(hash[argv[2]](open(argv[1], 'rb').read()).hexdigest())
	except KeyError:
		exit("Unsupported hash type\nPlease use md5, sha1, sha256, or all.")

#!/usr/bin/env python

from sys import exit,argv
from logging import getLogger, ERROR
getLogger("scapy.runtime").setLevel(ERROR)
from scapy.all import rdpcap

if len(argv) == 2:
	read = rdpcap(argv[1]+".pcap")
else:
	exit("usage: python %s <file_to_read(no ext)>"%argv[0])

print str(read.show()).replace("None","")

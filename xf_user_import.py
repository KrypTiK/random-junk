#!/usr/bin/env python
#XenForo user import 


import mechanize
from sys import stdout,exit

user = '' #admin user
password = '' #admin pass

f = open('import.txt','r') #file with username:email:password 

for x in f.readlines():

	str = x.strip()
	info = str.split(':')
	
	stdout.write("\r Creating user: %s" % info[0])
	stdout.flush()

	br = mechanize.Browser()
	br.open('http://localhost/xenforo/admin.php?users/add')

	br.select_form(nr=0)
	br.form['login'] = user
	br.form['password'] = password

	br.submit()

	br.select_form(nr=1)
	
	br.form['username'] = info[0]
	br.form['email'] = info[1]
	br.form['password'] = info[2]
	
	br.submit()
	
f.close()
exit('Import complete')

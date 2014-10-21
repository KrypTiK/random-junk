#!/usr/bin/env python
#Created by KrypTiK
#Only edit where specified
#Will work on this more


import mechanize
from sys import argv,exit
from bs4 import BeautifulSoup
from string import digits,ascii_uppercase
from random import choice

forum_url = 'http://localhost/vbulletin/' #Trailing slash / Edit this

def spam():
    user = ''.join(choice(ascii_uppercase+digits) for i in range(6))
    userinfo = {
        'username':user,
        'password':''.join(choice(ascii_uppercase+digits) for i in range(8)),
        'email': user+'@'+''.join(choice(ascii_uppercase+digits) for i in range(6))+'.com'
    }
    postinfo = {
        'title':'Spammer title', #Edit this
        'message':'Spammer body' #Edit this
    }
    if userinfo['username'] == userinfo['password']:
        exit("Username and password must not be the same")
    if len(postinfo['message']) < 10:
        exit("Post message must be more than 10 characters")
    br = mechanize.Browser()
    br.open(forum_url+'register.php')
    br.select_form(nr=2)
    br.form['username'] = userinfo['username']
    br.form['password'] = userinfo['password']
    br.form['passwordconfirm'] = userinfo['password']
    br.form['email'] = userinfo['email']
    br.form['emailconfirm'] = userinfo['email']
    br.find_control('agree').items[0].selected=True
    br.submit(label='Complete Registration')
    bs = BeautifulSoup(br.response(), 'lxml')
    for div in bs.find_all('div',{'class':'blockrow restore'}):
        if len(div) > 0:
            print 'Registration successful!\nUsername: '+userinfo['username']+'\nPassword: '+userinfo['password']
        else:
            exit('Registration failed!')
    br.open(forum_url+"forum.php")
    bs = BeautifulSoup(br.response(),'lxml')
    for forumtitle in bs.find('h2',{'class':'forumtitle'}):
        link = forumtitle['href']
    br.open(forum_url+link)
    bs = BeautifulSoup(br.response(), 'lxml')
    for a in bs.find_all('a',{'id':'newthreadlink_top'}):
        link = a['href']
    br.open(forum_url+link)
    bs = BeautifulSoup(br.response(), 'lxml')
    br.select_form(name='vbform')
    br.form['subject'] = postinfo['title']
    br.form['message'] = postinfo['message']
    br.submit()
    print "Thread '"+postinfo['title']+"' created"
    

if __name__=="__main__":
    i = 0
    if len(argv) != 2:
        count = 10
    else:
        count = int(argv[1])
    while i < count:
        spam()
        i += 1

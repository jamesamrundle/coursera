#! /usr/bin/python3

import re, pyperclip
#TODO: create regex for phone numbers

##create regex for email.com
##get text off document
##extract emails/numbers
##copy extraced emails to clipboard

message = (''' 816-679-3011 IM HUNGRY ORDER PIZZA (816)679-3012 hamburger sandwich
           8266793013 679-3014 ooooor 6793015 (816)-679-3016 816-679-3016 ext. 1654
           (816)679-3017 ext. 1654 8266793018 ext. 1234
           ''')
emailmessage = ('''Cornett, Catie
	
Health Services
	
Temporary Employee
	
corn***@cofc.edu
	
 
Dockery, Catherine M
	
Health Services
	
Administrative Specialist II
	
dock***@cofc.edu
	
 
Griesedieck, Catherine Grace
	
Political Science
	
 
	
grie***@cofc.edu
	
 
Hamilton, Catherine Palmer
	
Registrars Office
	
Temporary Employee
	
hami***@cofc.edu
	
(843)953-5668
Hartman, Hannah Catherine
	
Athletic Staff-E and G
	
Temporary Employee
	
hart***@cofc.edu
	
 
Holmes, Catherine D
	
English
	
Senior Instructor
	
holm***@cofc.edu
	
(843)953-5771
Kollath-Cattano, Christy Lynn
	
School of Edu-Health and Human Perf
	
Assistant Professor
	
koll***@cofc.edu
	
 ''')

PhoneRegex = re.compile(r''' ##not finding numbers instyle of 999999999 x12334.
                             ## will have to  add extentions to the part of code where it looks for the nonseperated number
# 000-000-0000, 000-0000, (999)999-9999,999.999.9999, 000-0000-0000 ext 1235, x:1234
(\d{10})|    #fullnumber no seperation
(\(?\d\d\d\)?-?)? #areacode(opt)
    #seperator
(\d\d\d\W)#first 3 digits
    #seperator
(\d\d\d\d\s)#last digets
(ext.(\s)?\d+)? #extension(opt)      
(x\d+)?

''', re.VERBOSE)
emailfinder = re.compile(r'''
([a-zA-Z0-9*+_$.]+ #first part
 @)   #@
([a-zA-Z0-9*+_$.]+)#secondpart
#(\.[a-z]{3-4})$ #.com/gov

''',re.VERBOSE)
mailobj = emailfinder.findall(emailmessage)


mobj = PhoneRegex.findall(message)

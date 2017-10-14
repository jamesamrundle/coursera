
import re

message = ''' Hello this is James, call me at 816-679-3017 so we can set up a time to meet. Thanks!'
816-679-3011 816-679-3012 (816)-679-3013'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
NumWParen= re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall(message), NumWParen.findall(message)
mo1 = NumWParen.findall(message)
for i in mo:
    print('The number : ' + str(i)+ ' was found.')

message2 = "816-679-3011 poop (816)679-3012 hamburger sandwich 8266793013 679-3014 ooooor 6793015"

PNUMRX = re.compile(r'((\d\d\d)?(\(\d\d\d\))?-?(\d\d\d-\d\d\d\d))|((\d\d\d)?(\d\d\d\d\d\d\d))')
#PNUMRX2 = re.compile(r'(\d\d\d)?(\d\d\d\d\d\d\d)')
mobj = PNUMRX.findall(message2)#, PNUMRX2.findall(message2)
                    

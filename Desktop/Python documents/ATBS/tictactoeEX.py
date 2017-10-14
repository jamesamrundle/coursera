#! /usr/bin/python3

import pprint

theBoard = {'top-L': ' ','top-M' : 'X', 'top-R': ' ',
            'mid-L' : ' ', 'mid-M': ' ','mid-R': ' ',
            'low-L' : ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

def boardPrint(tile):
    print(tile['top-L'] + ' | ' +tile['top-M'] + ' | ' + tile['top-R'])
    print('---------')
    print(tile['mid-L'] + ' | ' +tile['mid-M'] + ' | ' + tile['mid-R'])
    print('---------')
    print(tile['low-L'] + ' | ' +tile['low-M'] + ' | ' + tile['low-R'])


#better    #print(tile['top-L'],tile['top-M'],tile['top-R'],sep = " | ")

boardPrint(theBoard)

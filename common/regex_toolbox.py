# -*- coding: utf-8 -*-

'''
Created on 2013-3-24

@author: Qiqun Han
'''

import re

def split_string(delimiters, s):
    return re.split(delimiters, s)

if __name__ == '__main__':
    if 1:
        delimiters = '-| '
        s = 'micro-messages company'
        print split_string(delimiters, s)
        
    if 1:
        delimiters = '-|\|'
        s = 'micro-messages|company'
        print split_string(delimiters, s)
        
    if 1:
        delimiters = '[-|]'
        s = 'micro-messages|company'
        print split_string(delimiters, s)
        
    if 1:
        s = 'Oracle Corporation (NASDAQ:ORCL) is included in Apple (AA)'
        r = re.finditer(r'Oracle Corporation \((.+?)\)', s)
        
        for match in r:
            print match.group(0)
            print match.group(1)

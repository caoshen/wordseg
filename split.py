#-*- coding:utf-8 -*-

import codecs
import sys

def split(train, test):
    f = codecs.open(train,'r','utf-8')
    contents = f.read()
    contents = contents.split(u' ')
    f.close

    f = codecs.open(test, 'r','utf-8')
    lenlist = []

    for line in f:
        lenlist.append(len(line.rstrip()))
    f.close
    
#   print lenlist

    j = 0
    currentlen = 0
    for i in range(len(contents)):
        if currentlen < lenlist[j]:
            currentlen+=len(contents[i])
        else:
            contents.insert(i,u'\n')
            currentlen = 0
            j+=1
    
    f = codecs.open(train,'w','utf-8')
    f.write(' '.join(contents))
    f.close

def main():
    args = sys.argv[1:]
    split(args[0], args[1])

if __name__ =='__main__':
    main()


#-*- coding:utf-8 -*-
import codecs
import sys
import os
from tag import tag
from back import back

def back_new(test,linefile,temp,newtemp,train):
    f1 = codecs.open(test,'r','utf-8')
    
    i=0
    for line in f1:
        i=i+1
        
        f2 = codecs.open(linefile,'w','utf-8')
        f2.write(line)
        f2.close
        
        tag(linefile,temp)
        cmd = 'crf_test -m model temp >newtemp'
        os.system(cmd)
        back(newtemp,train)

        f3 = codecs.open(train,'a','utf-8')
        f3.write(u'\n')
        f3.close
        
  
        
    f1.close

def main():
    args = sys.argv[1:]
    back_new(args[0],args[1],args[2],args[3],args[4])

if __name__ == '__main__':
    main()


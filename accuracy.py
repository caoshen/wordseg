# -*- coding:utf-8 -*-

import sys
import codecs

def accuracy():
    f = codecs.open('result','r','utf-8')

    count = 0
    accuracy = 0
    for line in f:
        if line == u'\n': 
            continue
        count+=1
        test,train = line.rstrip().split('\t')[-2:]
        if test == train:
            accuracy+=1

    f.close()

    print float(accuracy)/count

if __name__ == '__main__':
    accuracy()

            

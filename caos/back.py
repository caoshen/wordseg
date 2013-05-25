# -*-coding:utf-8-*-

import codecs
import sys

def back(test, back):
    f = codecs.open(test,'r','utf-8')
    backfile = []
    words = ''
    for line in f:
        if line == u'\n':
            continue
        word = line.rstrip().split('\t')[0]
        train = line.rstrip().split('\t')[-1]
        if train == 'S':
            backfile.append(word)
        elif train == 'B'or train =='M':
            words +=word
        elif train == 'E':
            words +=word
            backfile.append(words)
            words = ''
    if words != '':
	backfile.append(words)	
	
    f.close

    f = codecs.open(back,'a','utf-8')
    f.write(' '.join(backfile))
    f.close
        
def main():
    args = sys.argv[1:]
    back(args[0], args[0]+'.back')

if __name__=='__main__':
    main()

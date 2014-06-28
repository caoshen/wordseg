#-*- coding:utf-8 -*-
import codecs
import sys

def seg(testfile, segfile):
    f = codecs.open(testfile, 'r', 'utf-8')
    fw = codecs.open(segfile, 'w', 'utf-8')

    for line in f.readlines():
        if line == u'\r\n' or line == u'\n':
            fw.write(u'\n')
        else:
            # remove spaces on the right
            word = line.rstrip().split(u'\t')[0]
            tag = line.rstrip().split(u'\t')[-1]
            # single word
            if tag == 'S':
                fw.write(' ' + word + ' ')
            # begin of word
            elif tag == 'B':
                fw.write(' ' + word)
            # mid of word
            elif tag == 'M':
                fw.write(word)
            # end of word
            elif tag == 'E':
                fw.write(word + ' ')
            else:
                continue
    f.close
    fw.close
	
def main():
    args = sys.argv[1:]
    seg(args[0], args[0] + '.seg')

if __name__ == '__main__':
    main()
                

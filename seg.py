#-*- coding:utf-8 -*-
import codecs
import sys

def seg(testfile, segfile):
    f = codecs.open(testfile, 'r', 'utf-8')

    seglist = []
    words = ''

    for line in f:
        if line == u'\r\n' or line == u'\n':
            seglist.append(u'\n')
        else:
            # remove spaces on the right
            word = line.rstrip().split(u'\t')[0]
            tag = line.rstrip().split(u'\t')[-1]
            # single word
            if tag == 'S':
                if words == '':
                    seglist.append(word)
                # condition like BMMS
                else:
                    seglist.append(words)
                    words = ''
                    seglist.append(word)
            # begin of word
            elif tag == 'B':
                # condition like BMMB
                if words != '':
                    seglist.append(words)
                    words = word
                else:
                    words = word
            # mid of word
            elif tag == 'M':
                words += word
            # end of word
            elif tag == 'E':
                words += word
                seglist.append(words)
                words = ''
            else:
                continue
    f.close

    f = codecs.open(segfile, 'w', 'utf-8')
    f.write('  '.join(seglist))
    f.close
	
    # remove space
    f = codecs.open(segfile, 'r', 'utf-8')
    get = []
    for line in f:
        get.append(line[:-1].strip() + u'\n')
    f.close
    f = codecs.open(segfile, 'w', 'utf-8')
    f.write(''.join(get))
    f.close

def main():
    args = sys.argv[1:]
    seg(args[0], args[0] + '.seg')

if __name__ == '__main__':
    main()
                

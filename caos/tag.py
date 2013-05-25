# -*- coding:utf-8 -*-

import codecs
import sys

def tag(training, tagfile):
    f = codecs.open(training, 'r', 'utf-8')
    contents = f.read()
    contents = contents.replace(u'\r',u'')
    contents = contents.replace(u'\n',u'')

    words = contents.split(' ')
#    print len(words)
    taglist = []
    punc = [u'，', u'、', u'：',  u'。', u'！', u'（', u'）', u'《', u'》', u'-', u'-', u'——']
#    num = ['1', '2' , '3', '4', '5', '6', '7', '8', '9', '0']
#    i=0
    for word in words:
#        i=i+1
#        if(i%100==0):
#            taglist.append(u'\r')
        if len(word)==0:
            continue
        elif len(word)==1:
            if word in punc:
                category = ' PUNC'
            else:
                category = ' CN'
            tagword=word+ category+ ' S'+ u'\n'
        elif len(word)==2:
            tagword=word[0]+' CN' +' B'+ u'\n'+ word[1]+ ' CN'+ ' E'+ u'\n'
        else:
            tagword=word[0]+' CN' +' B'+ u'\n'
            for midword in word[1:-1]:
                tagword+=midword+' CN' +' M'+ u'\n'
            tagword+=word[-1]+' CN' +' E'+ u'\n'
        taglist.append(tagword)
    
    fw = codecs.open(tagfile,'w','utf-8')
    fw.write(''.join(taglist))
    fw.close

def main():
    args = sys.argv[1:]
    
        
    tag(args[0], args[0] + '.data')

if __name__ == '__main__':
    main()

        
    

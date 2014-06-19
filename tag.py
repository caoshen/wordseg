# -*- coding:utf-8 -*-

import codecs
import sys

def tag(origin, tagfile):
    f = codecs.open(origin, 'r', 'utf-8')
    contents = f.read()
    contents = contents.replace(u'\r',u'')
    contents = contents.replace(u'\n',u'\n ')

    # if origin is a training file, then split the word
    # by space. If origin is a test file, transform it into
    # a list
    if origin.find('train') != -1:
        words = contents.split(' ')
    else:
        words = list(contents)

    # tagword is the chinese word after beging taged,
    # i.e. "上海" -> "上 CN B" "海 CN E"
    taglist = []
    punc = [u'，', u'、', u'：',  u'。', u'！', u'（', u'）', u'《', u'》', u'-', u'-', u'——']
    for word in words:
        if len(word) == 0:
            continue
        elif len(word) == 1:
            if word == u'\n':
                tagword = u'\n'
            elif word == u' ':
                continue
            elif word in punc:
                tagword = word + ' PUNC' + ' S' + u'\n'
            else:
                tagword = word + ' CN' + ' S' + u'\n'
        elif len(word) == 2:
            tagword = word[0] + ' CN' + ' B' + u'\n' + word[1]+ ' CN' + ' E' + u'\n'
        else:
            tagword = word[0] + ' CN' + ' B' + u'\n'
            for midword in word[1 : -1]:
                tagword += midword + ' CN' + ' M' + u'\n'
            tagword += word[-1] + ' CN' + ' E' + u'\n'
        taglist.append(tagword)
    
    fw = codecs.open(tagfile,'w','utf-8')
    # convert list to string
    fw.write(''.join(taglist))
    fw.close
    
def main():
    args = sys.argv[1:]
            
    tag(args[0], args[0] + '.data')

if __name__ == '__main__':
    main()

        
    

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
    
    
    for word in words:
        if len(word) == 0:
            continue
        elif len(word) == 1:
            if word == u'\n':
                tagword = u'\n'
            elif word == u' ':
                continue
            else:
                tagword = word + cat(word) + ' S' + u'\n'
        elif len(word) == 2:
            tagword = word[0] + cat(word[0]) + ' B' + u'\n' + word[1] + cat(word[1]) + ' E' + u'\n'
        else:
            tagword = word[0] + cat(word[0]) + ' B' + u'\n'
            for midword in word[1 : -1]:
                tagword += midword + cat(midword) + ' M' + u'\n'
            tagword += word[-1] + cat(word[-1]) + ' E' + u'\n'
        taglist.append(tagword)
    
    fw = codecs.open(tagfile,'w','utf-8')
    # convert list to string
    fw.write(''.join(taglist))
    fw.close

def cat(word):
    
    punc = [u'，', u'、', u'：',  u'。', u'！', u'（', u'）', u'《', u'》', u'-', u'-', u'%', u'*', u'/', u'.', u'°']
    num = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'0',
           u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'○' ,u'零', u'个', u'十', u'百', u'千', u'万', u'亿']
    time = [u'年', u'月', u'日', u'时', u'分', u'秒']

    if word in punc:
        return ' PUNC'
    elif word in num:
        return ' NUM'
    elif word in time:
        return ' TIM'
    else:
        return ' CN'
    
    
def main():
    args = sys.argv[1:]
            
    tag(args[0], args[0] + '.data')

if __name__ == '__main__':
    main()

        
    

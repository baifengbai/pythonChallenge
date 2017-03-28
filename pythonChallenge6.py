""" the page consist of a paypal donation button which redirects to paypal..
the comment after <html> says "zip" ... changing the url has /pc/def/zip.html
says "Yes. Find the zip." that means we have to find some zip file !! :D ... go
and change url as "/def/channle.zip" (channel is from the previous url) you
will get a zip file.. extract it and read the read me and run this script ..
(some changes will be required) """

t = open('90052.txt', 'r')
name = '90052.txt'
import re
count = 0
res1 = ['90052.txt']
r = re.compile('[0-9]')
for i in range(909):
        count += 1
        print count
        chk = t.read()
        f = chk.split(' ')
        for elem in f:
                if elem == 'comments' or elem == 'comment':
                        count = 999999999999999
        print name 
        print chk
        nothing = ''.join(re.findall(r, chk))
        name = nothing+'.txt'
        res1.append(name)
        t = open(name, 'r')

import zipfile

a = zipfile.ZipInfo('channel.zip')
for i in res1:
    for j in a.filelist:
        if j.filename == i:
            sys.stdout.write(j.comment)

""""
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
"""

# wow!! this is awesome: See the letters in the word

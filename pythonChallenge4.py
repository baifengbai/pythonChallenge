import urllib   
import re
from bs4 import BeautifulSoup

def scrape():
    #url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    r = re.compile('[0-9]')
    nothing = '60074'
    for i in range(218, 400):

        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing)


    	htmlfile = urllib.urlopen(url)
    	htmltext = htmlfile.read()
        print i
    	print url
    	print htmltext
    	nothing = ''.join(re.findall(r, htmltext))
    	#url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(num)
    	#soup = BeautifulSoup(htmltext)
    	#ans = soup.find('div', {'class':'article_body', 'itemprop':'articleBody'})
    	#print ans
scrape()


#ANSWER is in http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
# 250th iteration :D 
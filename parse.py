# fetching URLS
import urllib2

# Regular Expression
import re
regexp = re.compile(r"\:[\+\-][0-9:w]")

from HTMLParser import HTMLParser

#f = open('parse_out.txt','w')

# fetching URLS
response = urllib2.urlopen('http://www.ptt.cc/bbs/Stock/M.1398611057.A.2EF.html')
html = response.read()

# create a subclass and override the handler methods
#class MyHTMLParser(HTMLParser):
#   def handle_starttag(self, tag, attrs):
#      print "Encountered a start tag:", tag
#   def handle_endtag(self, tag):
#	  print "Encountered an end tag :", tag
#   def handle_data(self, data):
#	  print "Encountered some data  :", data

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
   def handle_data(self, data):
	 # split the stream with space ' '
	  strlist = data.split(' ')
	  pprice = data.strip(':')
	  pprice = u''.join(c for c in pprice if ('0' <= c <= '9' or c == '.') or c == '+' or c == '-' )
#	  pprice = filter(str.isdigit, pprice.encode('utf8'))
	  if (regexp.search(data)) :print "Encountered some data", pprice
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
#parser.feed('<html><head><title>Test</title></head>'
#           '<body><h1>Parse me!</h1></body></html>')

#need to decode to unicode to beforing feeding the data
parser.feed(html.decode("utf8"))

#f.close()#close the file

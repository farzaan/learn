import urllib.request
import urllib.parse
import urllib
	
def read_text():
	quotes = open("D:\FARZAAN\dev\ws\mygithub\learn\python-coursera\houston.txt")
	contentOfFile = quotes.read()
	print(contentOfFile)
	check_profanity(contentOfFile)

	#close afteryou open
	quotes.close()
def check_profanity(text_to_check):
	host = urllib.parse.quote(text_to_check)
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + host)
	output = connection.read()
	print(output)
read_text()
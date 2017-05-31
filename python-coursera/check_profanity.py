def read_text():
	quotes = open("D:\FARZAAN\dev\ws\mygithub\learn\python-coursera\houston.txt")
	contentOfFile = quotes.read()
	print(contentOfFile)
	print("rte")
	#close afteryou open
	quotes.close()

read_text()
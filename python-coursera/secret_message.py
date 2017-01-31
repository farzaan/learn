import os
def rename_thy_files():
	#makes list of file name
	path = r"/home/farzaan/Downloads/prank"
	fileList = os.listdir(path)

	#print path
	#rename them nao
	for file in fileList:
		newFilename = file.translate(None, "0123456789")
		#print newFilename
		os.rename(path + "/" + file, path + "/" + newFilename)

	

rename_thy_files()
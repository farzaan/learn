import os
def rename_thy_files():
	#makes list of file name
	path = r"/home/farzaan/Downloads/prank"
	fileList = os.listdir(path)

	print path
	#rename them nao
	for file in fileList:
		newFilename = file.translate(None, "0123456789")
		print file, newFilename
		os.rename(path + "/" + file, path + "/" + newFilename)

	return 

rename_thy_files()
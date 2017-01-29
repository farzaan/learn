import os
def rename_thy_files():
	#makes list of file name
	path = "prank"
	fileList = os.listdir(path)
	#rename them nao
	for file in fileList:
		newFilename = file.translate(None, "0123456789")
		print file, newFilename
		os.rename(path + "/" + file, newFilename)
	return file
print(rename_thy_files())


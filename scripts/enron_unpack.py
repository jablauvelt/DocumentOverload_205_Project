# Data are stored as .zip files for each Enron employee. This file pulls out the .txt files from each .zip file. 

# Execute in parallel 26 times using the letters of the alphabet (matched to last name of person)
# To execute, run : python enron_unpack.py <letter of alphabet>
# Execution time parallel 26 times on a m3.large machine is about 12 hours
# Best to kick it off a few hours before bedtime for fresh data in the morning
# python enron_unpack.py a
# python enron_unpack.py b
# python enron_unpack.py y
# python enron_unpack.py z

import zipfile
import os
import sys

for root, directories, filenames in os.walk('/enron/edrm-enron-v2/'): 
	for f in filenames:
		if f[:15] == 'edrm-enron-v2_' + sys.argv[1]: # allows user to specify letter from alphabet
			if f.find('xml.zip') > 0:
				# try/except statement bypasses any "bad zipfile" errors
				try:
					zf = zipfile.ZipFile(root + f)
					for z in zf.namelist():
						if z.find('.txt') > 0:
							if z.find('text_') == 0:
								# save .txt files to /enron_output/text_00* folders
								os.system("unzip " + root + f + " " + z + " -d /enron_output/")
				except:
					print (sys.exc_info()[0])

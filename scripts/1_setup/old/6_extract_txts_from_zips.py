# Data are stored as .zip files for each Enron employee. This file pulls out the .txt files from each .zip file. 

# Execute in parallel 26 times using the letters of the alphabet (matched to last name of person)
# To execute, run : nohup python 6_extract_txts_from_zips.py <letter of alphabet> &, e.g:
# nohup python 6_extract_txts_from_zips.py a &
# nohup python 6_extract_txts_from_zips.py b &
# ...
# nohup python 6_extract_txts_from_zips.py y &
# nohup python 6_extract_txts_from_zips.py z &

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
								os.system("unzip " + root + f + " " + z + " -d /enron_output")
				except:
					print (sys.exc_info()[0])
Contact GitHub API Training Shop Blog About

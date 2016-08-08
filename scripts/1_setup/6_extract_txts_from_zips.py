# Run in /enron_output/staging directory
# To run : $ python 6_extract_txts_from_zips.py
# Monitor progress with  $ find /enron_output/staging | wc -l
# Takes ~5 minutes to run
# The final product should have ~1,720,792 files

import os

for root, directories, filenames in os.walk('/enron/edrm-enron-v2/'):
	for f in filenames:
		if f.find('xml.zip') > 0:
			filename = root + f
			lastname = filename[filename.index('_')+1:][:filename[filename.index('_')+1:].index('_')]
			print("unzip -qq -j " + filename + " \"*.txt\" -x \"native*\" -d /enron_output/staging/staging_" + lastname + " &")
			os.system("unzip -qq -j " + filename + " \"*.txt\" -x \"native*\" -d /enron_output/staging/staging_" + lastname + " &")

import zipfile
import os
import sys

for root, directories, filenames in os.walk('/enron/edrm-enron-v2/'):
	for f in filenames:
		if f[:15] == 'edrm-enron-v2_' + sys.argv[1]:
			if f.find('xml.zip') > 0:
				try:
					zf = zipfile.ZipFile(root + f)
					for z in zf.namelist():
						if z.find('.txt') > 0:
							if z.find('text_') == 0:
								os.system("unzip " + root + f + " " + z + " -d /enron_output/")
				except:
					print (sys.exc_info()[0])

import zipfile
import os

for root, directories, filenames in os.walk('/enron/edrm-enron-v2/'):
	for f in filenames:
		if f.find('xml.zip') > 0:
			zf = zipfile.ZipFile(root + f)
			for z in zf.namelist():
				if z.find('.txt') > 0:
					os.system("unzip " + root + f + " " + z + " -d /enron_output/")

import os

for root, directories, filenames in os.walk('/enron/edrm-enron-v2/'):
	for f in filenames:
		if f.find('xml.zip') > 0:
			print f
			os.system("unzip " + root + f + " -d /enron_output/")

from pyspark import SparkContext
import re

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

#def get_zip_and_phone(line):
#	zipcodes = re.findall('[0-9]{5}', line)
#	if zipcodes:
#		return zipcodes[0]
#	else:
#		return 0

def get_zip_and_phone(tup):
        zipcodes = re.findall('[0-9]{5}', tup[1])
        if zipcodes:
		print tup[0]
                return zipcodes[0]
        else:
                return 0

#files = sc.wholeTextFiles('s3://docoverload/text_001/*')
#files = sc.textFile('file:///enron/edrm-enron-v2/unzipped_txt/text_001/*')
files = sc.wholeTextFiles('file:///enron/edrm-enron-v2/unzipped_txt/text_001/')


zips = files.map(get_zip_and_phone).filter(lambda s: s)


[i for i in zips.collect()]


import os
import datetime
import pymongo
import xmltodict

root = '/enron/edrm-enron-v2/unzipped'

print datetime.datetime.now().time()

client = pymongo.MongoClient()
db = client.xml_db
collection = db.xmls
xmls = collection.xmls

# for testing: /enron/edrm-enron-v2/unzipped/edrm-enron-v2_delainey-d_xml/zl_delainey-d_810_POO0_000.xml
for root, folders, files in os.walk(root):
	for idx, filename in enumerate(files):
		print str(idx) + '/' + str(len(files)) + ':' + filename
		print datetime.datetime.now().time()
		fullpath = root + '/' + filename
		with open(fullpath) as fd:
			doc = xmltodict.parse(fd.read())

		xml_id = xmls.insert_one(doc).inserted_id


print datetime.datetime.now().time()

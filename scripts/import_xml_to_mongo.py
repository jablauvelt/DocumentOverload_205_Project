import os
import datetime
import pymongo
import xml.etree.ElementTree as ET
import xmltodict

root = '/enron/edrm-enron-v2/unzipped'

client = pymongo.MongoClient()
db = client.xml_db
collection = db.xmls
xmls = collection.xmls
xmls.drop()

okstart = False
for root, folders, files in os.walk(root):
	for idx, filename in enumerate(files):
		
		if filename == '3.265045.D02MGGIEE2LBNOCEYFGEQYDZDUZS4KLUA.1.xml':
			okstart = True

		if not okstart: continue
		
		print str(idx) + '/' + str(len(files)) + ':' + filename
		print datetime.datetime.now().time()
		fullpath = root + '/' + filename

		try:
			tree = ET.parse(fullpath)
		except ET.ParseError:
			print "PARSE ERROR on ET.parse() -----------------------------------!!"
			continue

		try:
			docs = tree.getroot()[0][0]
		except IndexError:
			print "INDEX ERROR - bad tree --------------------------------------!!"
			continue

		for idx, child in enumerate(docs):
			if idx % 1000 == 0 or idx == len(docs)-1: 
				print str(idx) + '/' + str(len(docs)-1)

			orddict = xmltodict.parse(ET.tostring(child))
			xmls.insert_one(orddict)


import os
import datetime
import pymongo
import xml.etree.ElementTree as ET
import xmltodict

# Set root directory
root = '/enron/edrm-enron-v2/unzipped'

# Access MongoDB "xmls" collection
client = pymongo.MongoClient()
db = client.xml_db
collection = db.xmls
xmls = collection.xmls

# Check to see if user wants to add to existing collection, or reset it
if xmls.count():
	confirm =raw_input("The xmls collection already has " + str(xmls.count()) + " documents. Enter 'c' to add to this collection or 'r' to reset it and start from scratch.")
	if confirm = 'r':
		xmls.drop()

# Loop through each file in unzipped/ (all the files are xmls, and were put in
# there by extract_xml_metadata_from_zips.sh)
for root, folders, files in os.walk(root):
	for idx, filename in enumerate(files):
		
		# Print file name and time
		print str(idx) + '/' + str(len(files)) + ':  ' + filename
		print datetime.datetime.now().time()

		# Attempt to parse the XML file using the ElementTree package.
		# Some XML files are corrupt for unknown reasons - skipping these
		# in the interest of saving time.
		try:
			tree = ET.parse(root + '/' + filename)
		except ET.ParseError:
			print "PARSE ERROR on ET.parse() -----------------------------------!!"
			continue

		# Attempt to access the "Documents" within the tree. The first couple of layers
		# don't contain valuable information, but within them, the documents are repeated,
		# several thousand in each file.
		try:
			docs = tree.getroot()[0][0]
		except IndexError:
			print "INDEX ERROR - bad tree --------------------------------------!!"
			continue

		# We can't upload the full set of docs to MongoDB - each document we upload
		# to MongoDB needs to be an individual document (email) from an XML perspective too.
		# Each child is a document starting with <document> and ending with </document>
		for idx, child in enumerate(docs):
			# Print progress every 1000 documents
			if idx % 1000 == 0 or idx == len(docs)-1: 
				print str(idx) + '/' + str(len(docs)-1)

			# MongoDB can take a dict-like object, not a tree, so I use the xmltodict
			# package to convert the tree to an Ordereddict
			orddict = xmltodict.parse(ET.tostring(child))
			# Insert the ordered dict into the xmls collection.
			xmls.insert_one(orddict)


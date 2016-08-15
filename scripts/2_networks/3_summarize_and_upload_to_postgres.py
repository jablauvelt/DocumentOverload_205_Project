### Document Overload
### Make sure to start postgres first (bash: /data/start_postgres.sh)
### Takes about 30 minutes on m3.medium
import sys
import datetime
import re

import pymongo
import psycopg2
from pprint import pprint


start_time = datetime.datetime.now()
print 'Start time:'
print start_time

# Access MongoDB "xmls" collection
client = pymongo.MongoClient()
db = client.xml_db
collection = db.xmls
xmls = collection.xmls
tags = collection.tags

# Aggregate froms
froms = list(xmls.aggregate([{'$unwind': '$Document.Tags.Tag'},
                       {'$match': {'Document.Tags.Tag.@TagName': '#From'}},
                       {'$group': {'_id': '$Document.@DocID', '#From': {'$first': '$Document.Tags.Tag.@TagValue'}}}], allowDiskUse=True))

# Aggregate tos
tos = list(xmls.aggregate([{'$unwind': '$Document.Tags.Tag'},
                       {'$match': {'Document.Tags.Tag.@TagName': '#To'}},
                       {'$group': {'_id': '$Document.@DocID', '#To': {'$first': '$Document.Tags.Tag.@TagValue'}}}], allowDiskUse=True))

# Print mongodb aggregation time
print 'Time taken for mongodb aggregation:'
print str((datetime.datetime.now() - start_time).seconds * 1.0 / 3600) + ' hours'

# Connect to PostGres DB
print 'Uploading results to PostGres'
conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")

# Clear tables
cur = conn.cursor()
cur.execute("delete from email_from")
cur.execute("delete from email_to")
conn.commit()

# Insert email_froms
for fr in froms:
	try:
		cur.execute("insert into email_from (filename, email_from) values ('" + \
                     fr['_id'] + "', substring('" + re.sub("'", '', fr['#From']) + "' from 1 for 50))")
	except:
		print(sys.exc_info()[0])
		print fr

# Insert email_tos
for to in tos:
        try:
		for t in to['#To'].split(','):
	                cur.execute("insert into email_to (filename, email_to) values ('" + \
        	             to['_id'] + "', substring('" + re.sub("'", '', t) + "' from 1 for 50))")
        except:
                print(sys.exc_info()[0])
		print to

print 'Files uploaded to PostGres'

end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'

conn.commit()
conn.close()

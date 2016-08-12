### Document Overload

import pymongo
from pprint import pprint

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




### Dealing With Document Overload
### zipcode_phone.py
### Purpose: Search emails for zipcodes and phone numbers using Spark
###		and save counts of zips/phones to a text file.

from pyspark import SparkContext
import re
import datetime
import csv

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

# Search for zipcodes: works with sc.wholeTextFiles(), which returns a tuple of (filename, contents)
#def get_zip(tup):
#        zipcodes = re.findall('\\b[0-9]{5}\\b', tup[1])
#        if zipcodes:
#		# print tup[0] # tup[0] is the filename
#                return zipcodes[0]
#        else:
#                return 0

# Search for zipcodes: works with textFile()
def get_zip(content):
        zipcodes = re.findall('\\b[0-9]{5}\\b', content)
        if zipcodes:
                # print tup[0] # tup[0] is the filename
                return zipcodes[0]
        else:
                return 0

# Search for phone: works with textFile()
def get_phone(content):
        phones = re.findall('\\b[0-9]{3}[^0-9]?[0-9]{3}[^0-9]?[0-9]{4}\\b', content)
        if phones:
                # print tup[0] # tup[0] is the filename
                return re.sub('[^0-9]', '', phones[0])
        else:
                return 0


# Print start time
start_time = datetime.datetime.now()
print 'Start time:'
print start_time

# Get files - uncomment everything except the one you want to use
# Option 1: Combined text file from local file system (for testing only)
files = sc.textFile('file:///tmp/enron_emails_text_all.txt')
# Option 2: combined text file from s3
#files = sc.textFile('s3://docoverload/enron_emails_text_all.txt')
# Option 3: loose text files from file system (for testing only)
#files = sc.wholeTextFiles('file:///enron/edrm-enron-v2/unzipped_txt/text_000/')
# Option 4: loose text files directly from S3
#files = sc.wholeTextFiles('s3://docoverload/text_000')

# Zips:
# For each file, get the zip code and filter to non-blanks. Convert each zipcode to
# a tuple so it can be summarized with reduceByKey()
zips = files.map(get_zip).filter(lambda s: s).map(lambda s: (s, 1))

# Summarize counts by key (which is the zip code) and collect
smry_zips = zips.reduceByKey(lambda a, b: a + b).collect()

# Phones:
# For each file, get the phone number and filter to non-blanks. Convert each phone
# to a tuple so it can be summarized with reduceByKey().
phones = files.map(get_phone).filter(lambda s: s).map(lambda s: (s, 1))

# Summarize counts by key (which is the zip code) and collect
smry_phones = phones.reduceByKey(lambda a, b: a + b).collect()

# Print spark time
print 'Time Spark portion finished:'
print str((datetime.datetime.now() - start_time).seconds * 1.0 / 3600) + ' hours'

# Export zips to text file
print 'Saving zips to file:'
with open('/tmp/zips.csv', 'w') as fl:
	writer = csv.writer(fl)
	for i in smry_zips:
		writer.writerow(i)

# Export phones to text file
print 'Saving phones to file:'
with open('/tmp/phones.csv', 'w') as fl:
        writer = csv.writer(fl)
        for i in smry_phones:
                writer.writerow(i)


# Print end time
end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'


########################################
# TO DO
# - Get working with filename and combined files
# - save directly to S3 or to Postgres DB
########################################

### Dealing With Document Overload
### zipcode_phone.py
### Purpose: Search emails for zipcodes and phone numbers using Spark
###		and save counts of zips/phones to a text file.
### Takes about 10 minutes on a cluster with 1 master and 3 worker nodes, all m3.xlarge

from pyspark import SparkContext
import re
import datetime
import csv

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

# Search for zipcodes
def get_zip(content):
        zipcodes = re.findall('\\b[0-9]{5}\\b', content)
        if zipcodes:
                # print tup[0] # tup[0] is the filename
                return zipcodes[0]
        else:
                return 0

# Search for phone
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

# Combined text file from s3
files = sc.textFile('s3://docoverload/enron_emails_text_all.txt')

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


# Copy files to AWS S3
os.system("aws s3 cp /tmp/zips.csv s3://docoverload")
os.system("aws s3 cp /tmp/phones.csv s3://docoverload")
print 'Files copied to S3 as zips.csv and phones.csv'

# Print end time
end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'


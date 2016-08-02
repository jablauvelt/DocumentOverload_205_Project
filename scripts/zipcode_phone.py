from pyspark import SparkContext
import re
import datetime
import csv

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

# Works with sc.wholeTextFiles(), which returns a tuple of (filename, contents)
def get_zip(tup):
        zipcodes = re.findall('\\b[0-9]{5}\\b', tup[1])
        if zipcodes:
		# print tup[0] # tup[0] is the filename
                return zipcodes[0]
        else:
                return 0

# version for textFile
#def get_zip(content):
#        zipcodes = re.findall('\\b[0-9]{5}\\b', content)
#        if zipcodes:
#                # print tup[0] # tup[0] is the filename
#                return zipcodes[0]
#        else:
#                return 0


# Print start time
start_time = datetime.datetime.now()
print 'Start time:'
print start_time

# Get files
#files = sc.wholeTextFiles('s3://docoverload/text_000')
files = sc.wholeTextFiles('file:///enron/edrm-enron-v2/unzipped_txt/text_000/').coalesce(4)
#files = sc.textFile('file:///tmp/enron_emails_text_all.txt')

# For each file, get the zip code and filter to non-blanks
zips = files.map(get_zip).filter(lambda s: s)

# Convert each zipcode to a tuple so it can be summarized with reduceByKey()
zips2 = zips.map(lambda s: (s, 1))


# Summarize counts by key (which is the zip code) and collect
smry_zips = zips2.reduceByKey(lambda a, b: a + b).collect()

# Print spark time
print 'Time for Spark portion (before saving to file)'
print str((datetime.datetime.now() - start_time).seconds * 1.0 / 3600) + ' hours'

# Export to text file
with open('/tmp/test.csv', 'w') as fl:
	writer = csv.writer(fl)
	for i in smry_zips:
		writer.writerow(i)

# Print end time
end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'



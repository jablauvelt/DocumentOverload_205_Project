### Dealing With Document Overload
### 4_wordcount.py
### Purpose: Count words in emails
### Takes about 20 minutes on a cluster with 1 master and 3 worker nodes, all m3.xlarge

from pyspark import SparkContext
import os
import re
import datetime
import csv

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

# Print start time
start_time = datetime.datetime.now()
print 'Start time:'
print start_time

# Combined text file from s3
files = sc.textFile('s3://docoverload/enron_emails_text_all.txt')

counts = files.flatMap(lambda x: x.lower().split(' ')).map(lambda x: (re.sub("[^a-z0-9 ]", '', x), 1))
counts2 = counts.filter(lambda x: len(x) < 20).reduceByKey(lambda a, b: a + b).collect()

# Print spark time
print 'Time Spark portion finished:'
print str((datetime.datetime.now() - start_time).seconds * 1.0 / 3600) + ' hours'


# Export wrods to text file
print 'Saving words to file:'
with open('/tmp/wordcounts.csv', 'w') as fl:
	writer = csv.writer(fl)
	for i in counts2:
		writer.writerow(i)

# Copy files to AWS S3
os.system("aws s3 cp /tmp/wordcounts.csv s3://docoverload")
print 'File copied to S3 as wordcounts.csv'

# Print end time
end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'

sc.stop()

from operator import add
from pyspark import SparkContext
import re

sc = SparkContext(appName="PythonWordCount")

lines = sc.textFile('s3://docoverload12/enron_emails_text_all.txt')

counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)

output = counts.collect()

outfile = open('/home/ec2-user/wordcounts2.csv', 'w')

for (word, count) in output:

	clean_word =  word.encode('utf-8')[:30].replace(" ", "").replace("\t", "").replace("\n", "")

	if re.match("[\w]+$", clean_word):
		outfile.write("%s, %i" % (clean_word, count))
		outfile.write("\n")

outfile.close()

sc.stop()

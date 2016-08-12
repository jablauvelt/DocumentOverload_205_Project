# /home/w205/spark15/bin/spark-submit /enron_output/wordcount.py
# Spark piece requires approximately 40 minutes of execution time on m3.large machine
# Inserts into PostGres database requires approximately 30 minutes of execution time on m3.large machine

from __future__ import print_function

import sys
from operator import add
import psycopg2

from pyspark import SparkContext

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("delete from word_count")
conn.commit()

sc = SparkContext(appName="PythonWordCount")

lines = sc.textFile('/enron_output/enron_emails_text_all.txt')

counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)

output = counts.collect()

for (word, count) in output:
	try:
		if len(word.replace("\t", "").replace("\n", "").replace(" ", "")) < 20:
			print(word.replace("\t", "").replace("\n", "").replace(" ", ""), count)
			cur.execute("insert into word_count (word, count) values (%s, %s)", (word.replace("\t", "").replace("\n", "").replace(" ", ""), count))
	except:
		print (sys.exc_info()[0])
		conn.rollback()

conn.commit()
conn.close()
sc.stop()

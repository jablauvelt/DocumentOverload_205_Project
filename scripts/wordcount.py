# /home/w205/spark15/bin/spark-submit /enron_output/wordcount.py

from __future__ import print_function

import sys
from operator import add
import psycopg2

from pyspark import SparkContext

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("delete from word_count")
conn.commit()

if __name__ == "__main__":

	sc = SparkContext(appName="PythonWordCount")

#	lines = sc.textFile("/user/w205/enron_emails_text_all.txt", 1)
	lines = sc.textFile("/user/w205/3.930834.HZQ4RCCE2QEWC2S0AROHKWAKVHJIQNJRA.txt")

	counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)

	output = counts.collect()

	for (word, count) in output:
		try:
			print(word.replace("\t", "").replace("\n", "").replace(" ", ""), count)
			cur = conn.cursor()
			cur.execute("insert into word_count (word, count) values (%s, %s)", (word.replace("\t", "").replace("\n", "").replace(" ", ""), count))
			conn.commit()
		except:
			print (sys.exc_info()[0])
			conn.rollback()

sc.stop()
conn.close()

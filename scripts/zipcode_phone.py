# /home/w205/spark15/bin/spark-submit /enron_output/zipcode_phone.py

from __future__ import print_function

import sys
import psycopg2
import re

from pyspark import SparkContext

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("delete from zipcode_filename")
cur.execute("delete from phone_filename")
conn.commit()

if __name__ == "__main__":

	sc = SparkContext(appName="EnronEmailFiles")
	files = sc.wholeTextFiles("/user/w205/*.txt")

	file_output = files.collect()

	for (filename, content) in file_output:
		try:

			zipcode = re.findall('[0-9][0-9][0-9][0-9][0-9]', content)

			for z in zipcode:
				print(filename[filename.rfind("/") + 1:], z)
				cur = conn.cursor()
				cur.execute("insert into zipcode_filename (zipcode, filename) values (%s, %s)", (z, filename[filename.rfind("/") + 1:]))
				conn.commit()

			phone = re.findall('[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', content)

			for p in phone:
				print(filename[filename.rfind("/") + 1:], p)
				cur = conn.cursor()
				cur.execute("insert into phone_filename (phone, filename) values (%s, %s)", (p, filename[filename.rfind("/") + 1:]))
				conn.commit()

		except:
			print (sys.exc_info()[0])
			conn.rollback()

sc.stop()
conn.close()

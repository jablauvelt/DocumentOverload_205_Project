# /home/w205/spark15/bin/spark-submit /enron_output/zipcode_phone_emailtext.py

from __future__ import print_function
import sys
import psycopg2
import re
import email
import os
import gc
from pyspark import SparkContext
from pyspark import StorageLevel


def getsome(path):

	sc = SparkContext(appName="EnronEmailTextFiles")
	sc.setLogLevel("WARN")
	sc.parallelize(range(2), 1)
	counter = 0
	counter_print = 0

	for root, directories, filenames in os.walk(path):
		for f in filenames:

			file_be_processed = "file:" + root + f

			files = sc.wholeTextFiles(file_be_processed)

			counter = counter + 1
			counter_print = counter_print + 1

			if counter_print > 5:
				counter_print = 0
				print("Directory: " + root + ", Number of files processed: " + str(counter) + ", Objects Garbage Collected and Deallocated: " + str(gc.collect()))

			for (filename, content) in files.collect():
				try:

					zipcode = re.findall('[0-9][0-9][0-9][0-9][0-9]', content)

					for z in zipcode:
						cur.execute("insert into zipcode_filename (zipcode, filename) values (%s, %s)", (z, filename[filename.rfind("/") + 1:]))

					phone = re.findall('[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', content)

					for p in phone:
						cur.execute("insert into phone_filename (phone, filename) values (%s, %s)", (p, filename[filename.rfind("/") + 1:]))

					file = open(filename[filename.find('/'):])
					message = email.message_from_file(file)

					for key in message.keys():

						email_body = message.get_payload()
						cur.execute("insert into email_body (filename, email_body) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_body))

						if key.strip() == "From":

							email_from = message[key].replace("\t", "").replace("\n", "").replace(" ", "")
							cur.execute("insert into email_from (filename, email_from) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_from))

						elif key.strip() == "To":

							if message[key].find(">") > 0:
								for value in message[key].split('>,'):

									email_to = value.replace("\t", "").replace("\n", "").replace(" ", "")
									cur.execute("insert into email_to (filename, email_to) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_to))
	
							else:
								for value in message[key].split(','):

									email_to = value.replace("\t", "").replace("\n", "").replace(" ", "")
									cur.execute("insert into email_to (filename, email_to) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_to))

						elif key.strip() == "Cc" or key.strip() == "CC":

							if message[key].find(">") > 0:
								for value in message[key].split('>,'):

									email_cc = value.replace("\t", "").replace("\n", "").replace(" ", "")
									cur.execute("insert into email_cc (filename, email_cc) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_cc))

							else:

								for value in message[key].split(','):

									email_cc = value.replace("\t", "").replace("\n", "").replace(" ", "")
									cur.execute("insert into email_cc (filename, email_cc) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_cc))

						elif key.strip() == "Subject":

							email_subject = message[key].replace("\t", "").replace("\n", "")
							cur.execute("insert into email_subject (filename, email_subject) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_subject))

						elif key.strip() == "Date":

							email_date = message[key].replace("\t", "").replace("\n", "")
							cur.execute("insert into email_date (filename, email_date) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_date))

						elif key.strip() == "X-SDOC":

							email_sdoc = message[key].replace("\t", "").replace("\n", "")
							cur.execute("insert into email_sdoc (filename, email_sdoc) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_sdoc))

						elif key.strip() == "X-ZLID":
							
							email_zlid = message[key].replace("\t", "").replace("\n", "")
							cur.execute("insert into email_zlid (filename, email_zlid) values (%s, %s)", (filename[filename.rfind("/") + 1:], email_zlid))

						else:
							print("Data to be researched later:")
							print("KEY: " + key.strip())
							print("VALUE: " + message[key])

					conn.commit()
					file.close()

				except:
					print("Data Errors:")
					print("FILENAME: " + filename)
					print("SYSTEM ERROR: ", sys.exc_info()[0])
					conn.rollback()

	sc.stop()

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from zipcode_filename")
cur.execute("delete from phone_filename")
cur.execute("delete from email_from")
cur.execute("delete from email_to")
cur.execute("delete from email_cc")
cur.execute("delete from email_subject")
cur.execute("delete from email_date")
cur.execute("delete from email_sdoc")
cur.execute("delete from email_zlid")
cur.execute("delete from email_body")
conn.commit()

paths = (
	'/enron_output/text_007/',
	'/enron_output/text_006/',
	'/enron_output/text_005/',
	'/enron_output/text_004/',
	'/enron_output/text_003/',
	'/enron_output/text_002/',
	'/enron_output/text_001/',
	'/enron_output/text_000/'
	)

for p in paths:
	getsome(p)

conn.close()

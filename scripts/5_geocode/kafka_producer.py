# Used to submit data to kafka for processing

import psycopg2
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
counter = 0

# Python uses a large amount of memory when a large number of records are returned from postgres
# Thus, use a server side cursor to collection the records first and then batch them to python for processing
# This will place more pressure on the postgres database
cur.execute("DECLARE super_cursor BINARY CURSOR FOR select distinct zipcode from zipcode_filename")
while True:
	cur.execute("FETCH 1000 FROM super_cursor")
	rows = cur.fetchall()

	if not rows:
		break

	for row in rows:
		counter = counter + 1
		print counter, ": ", row[0]
		time.sleep(0.01)
		producer.send('getsome3', key="zipcode", value=row[0])

conn.close()

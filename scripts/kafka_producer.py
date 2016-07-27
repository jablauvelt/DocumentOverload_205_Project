# Used to submit data to kafka for processing

import psycopg2
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("DECLARE super_cursor BINARY CURSOR FOR select filename, zipcode from zipcode_filename limit 10")
while True:
	cur.execute("FETCH 1000 FROM super_cursor")
	rows = cur.fetchall()

	if not rows:
		break

	for row in rows:
		print row[0], row[1]
		producer.send('getsome', key=row[0], value=row[1])

conn.close()

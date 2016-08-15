# Approximate run time of 11 minutes to insert 2,680,000 records into Postgres, 30% CPU usage on m3.medium instance
# On the cluster, execute the following to persistently store the file in S3:	cp /home/ec2-user/wordcounts2.csv s3://docoverload
# github.com/RaRe-Technologies/smart_open
# Get yer pip on:	pip install smart_open

import psycopg2
import smart_open

counter = 0

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from word_count")
conn.commit()

for line in smart_open.smart_open('s3://docoverload12/wordcounts2.csv'):

	counter = counter + 1
	if counter % 10000 == 0:
		conn.commit()
		print "Number of rows committed: " + str(counter)

	word = line.replace("\n", "")[:line.replace("\n", "").index(',')]
	count = line.replace("\n", "")[line.replace("\n", "").index(',')+1:].strip()

	cur.execute("insert into word_count (word, count) values (%s, %s)", (word, count))

conn.commit()
conn.close()

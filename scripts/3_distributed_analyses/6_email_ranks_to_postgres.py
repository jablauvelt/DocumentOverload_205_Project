# Run time is less than a minute on a m3.medium host
# Grab file from s3 first: aws s3 cp s3://docoverload/enron_emails_ranks.txt /root/enron_emails_ranks.txt

import psycopg2

counter = 0

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from email_rank")
conn.commit()

infile = open('/root/enron_emails_ranks.txt', 'r')

for line in infile:

	counter = counter + 1
	if counter % 1000 == 0:
		conn.commit()
		print "Number of rows committed: " + str(counter)

	email = line.replace("\n", "")[:line.replace("\n", "").index(',')]
	rank = line.replace("\n", "")[line.replace("\n", "").index(',')+1:].strip()

	cur.execute("insert into email_rank (email, rank) values (%s, %s)", (email, rank))

conn.commit()
conn.close()

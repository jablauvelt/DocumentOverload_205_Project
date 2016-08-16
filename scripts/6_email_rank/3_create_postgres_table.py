# CREATE TABLE email_rank (email TEXT, rank REAL);
# Run time is less than a minute on a m3.medium host
# select * from email_rank order by rank desc;
# Kenneth Lay (CEO) and Jeffery Skilling (CFO) at the top of the email ranking list!  Exactly Right!

import psycopg2
import smart_open

counter = 0

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from email_rank")
conn.commit()

for line in smart_open.smart_open('s3://docoverload12/enron_emails_ranks.txt'):

	counter = counter + 1
	if counter % 1000 == 0:
		conn.commit()
		print "Number of rows committed: " + str(counter)

	email = line.replace("\n", "")[:line.replace("\n", "").index(',')]
	rank = line.replace("\n", "")[line.replace("\n", "").index(',')+1:].strip()

	cur.execute("insert into email_rank (email, rank) values (%s, %s)", (email, rank))

conn.commit()
conn.close()

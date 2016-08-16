# Generates a file of to and from emails from the postgres database to be ranked
# Approximate runtime of 5 minutes on m3.medium host to generate a file of 300Mb
# Run this on your single instance, before setting up and executing the cluster analyses
# When complete: aws s3 cp /root/enron_emails_to_from.txt s3://docoverload

import psycopg2

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("create index idx_email_to_filename on email_to (filename)")

outfile = open('/root/enron_emails_to_from.txt', 'w')

cur.execute("select filename, email_from from email_from")
email_from = cur.fetchall()

for efrom in email_from:

	cur.execute('select email_to from email_to where filename = %s', (efrom[0],))
	email_to = cur.fetchall()

	for eto in email_to:
		outfile.write(efrom[1] + " ::::: " + eto[0] + "\n")

outfile.close()

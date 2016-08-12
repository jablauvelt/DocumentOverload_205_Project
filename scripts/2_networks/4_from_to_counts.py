### DOCUMENT OVERLOAD
### 10 minutes on m3.medium

import datetime

import psycopg2

start_time = datetime.datetime.now()
print 'Start time:'
print start_time

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")


cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS from_to_counts;")
conn.commit()
#cur.execute("SELECT email_from, email_to, count(*) as count " + \
#		"FROM email_from a INNER JOIN email_to b ON a.filename = b.filename" + \
#		"GROUP BY email_from, email_to")
cur.execute("SELECT email_from, email_to, count(*) as count INTO from_to_counts " + \
                "FROM email_from a INNER JOIN email_to b ON a.filename = b.filename " + \
                "GROUP BY email_from, email_to;")


conn.commit()

conn.close()


# Print end time
end_time = datetime.datetime.now()
print 'End time:'
print end_time
print 'Total time elapsed: ' + str((end_time - start_time).seconds * 1.0 / 3600) + ' hours'

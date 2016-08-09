import psycopg2

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE word_count (word TEXT,
                               count int);''')

cur.execute('''CREATE TABLE machine_learning (filename TEXT,
                               probability_positive DECIMAL(17,15),
                               probability_negative DECIMAL(17,15),
                               conclusion TEXT);''')

cur.execute('''CREATE TABLE email_from (filename TEXT,
                               email_from TEXT);''')

cur.execute('''CREATE TABLE email_to (filename TEXT,
                               email_to TEXT);''')

cur.execute('''CREATE TABLE email_cc (filename TEXT,
                               email_cc TEXT);''')

cur.execute('''CREATE TABLE email_subject (filename TEXT,
                               email_subject TEXT);''')

cur.execute('''CREATE TABLE email_date (filename TEXT,
                               email_date TEXT);''')

cur.execute('''CREATE TABLE email_sdoc (filename TEXT,
                               email_sdoc TEXT);''')

cur.execute('''CREATE TABLE email_zlid (filename TEXT,
                               email_zlid TEXT);''')

cur.execute('''CREATE TABLE zipcode_filename (filename TEXT,
                               zipcode TEXT,
                               address TEXT,
                               longitude TEXT,
                               latitude TEXT);''')

cur.execute('''CREATE TABLE phone_filename (filename TEXT,
                               phone TEXT);''')

conn.commit()
conn.close()

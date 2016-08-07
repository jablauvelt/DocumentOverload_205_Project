import psycopg2

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE word_count (word TEXT,
                               count int);''')

cur.execute('''CREATE TABLE machine_learning (filename TEXT,
                               probability_positive DECIMAL(17,15),
                               probability_negative DECIMAL(17,15),
                               conclusion TEXT);''')

conn.commit()
conn.close()

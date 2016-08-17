#python 4_sentiment_analysis_to_postgres

from decimal import Decimal
import psycopg2
import smart_open

counter = 0

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from machine_learning")
conn.commit()

for line in smart_open.smart_open('s3://docoverload/sentiment_test.csv'):

        counter = counter + 1
        if counter % 1000 == 0:
                conn.commit()
                print "Number of rows committed: " + str(counter)

        fName, p_pos, p_neg, conclusion = line.replace("\n", "").split(",")
        conclusion = conclusion.strip();
        p_pos_dec = Decimal(p_pos)
        p_neg_dec = Decimal(p_neg)

        cur.execute("INSERT INTO machine_learning (filename,probability_positive,probability_negative,conclusion) \
                VALUES (%s,%s,%s,%s)", (fName, p_pos_dec, p_neg_dec, conclusion));

conn.commit()
conn.close()

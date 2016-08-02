# /home/w205/spark15/bin/spark-submit sentiment_analysis.py

import psycopg2
from pyspark import SparkContext
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

sc = SparkContext(appName="EnronSentimentAnalysis")
conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# clean up table
cur.execute("delete from machine_learning")

# select all email bodies
cur.execute("SELECT * FROM email_body LIMIT 5")
emails = cur.fetchall()

print "# of emails selected:", len(emails)

# sentiment analysis
for email in emails:
    filename = email[0]
    text = email[1]

    sentiment = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    classification = sentiment.sentiment.classification
    p_pos = sentiment.sentiment.p_pos
    p_neg = sentiment.sentiment.p_neg

    cur.execute("INSERT INTO machine_learning (filename,probability_positive,probability_negative,conclusion) \
          VALUES (%s,%s,%s,%s)", (filename, p_pos, p_neg, classification));

conn.commit()
conn.close()
sc.stop()

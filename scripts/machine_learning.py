# /home/w205/spark15/bin/spark-submit /enron_output/machine_learning.py
# machine learning requires python 2.7 from ApacheStorm Lab

import os
import sys
import psycopg2
from pyspark import SparkContext

paths = (
	'/enron_output/text_007/',
	'/enron_output/text_006/'
#	'file:/enron_output/text_005',
#	'file:/enron_output/text_004'
#	'file:/enron_output/text_003'
#	'file:/enron_output/text_002'
#	'file:/enron_output/text_001'
	)

sc = SparkContext(appName="EnronMachineLearning")

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("delete from machine_learning")
conn.commit()

train = [
('I love this sandwich.', 'pos'),
('this is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('this is my best work.', 'pos'),
("what an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('he is my sworn enemy!', 'neg'),
('my boss is horrible.', 'neg')
]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)

with open('/enron_output/machine_learning.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

for p in paths:
	for root, subdirs, files in os.walk(p):
		for f in files:
			try:
				file_to_classify = open(root + f, 'r')
				insert_file = f
				insert_prob_pos = str(round(cl.prob_classify(file_to_classify.read()).prob("pos"),5))
				insert_prob_neg = str(round(cl.prob_classify(file_to_classify.read()).prob("neg"),5))
				insert_conclusion = cl.classify(file_to_classify.read())
				print insert_file
				print insert_prob_pos
				print insert_prob_neg
				print insert_conclusion

				cur.execute("insert into machine_learning (filename, probability_positive, probability_negative, conclusion) values (%s, %s, %s, %s)", (insert_file, insert_prob_pos, insert_prob_neg, insert_conclusion))
				conn.commit()

			except:
				print(sys.exc_info()[0])

conn.commit()
conn.close()
sc.stop()

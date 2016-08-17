# /home/w205/spark15/bin/spark-submit 3_sentiment_analysis.py

from __future__ import print_function
import sys
import re
import email
import os
from pyspark import SparkContext
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

def text_preprocessor(s):
    #to lower case
    s = s.lower()

    #replace all digits to dddd
    s = re.sub(r'\d+','dddd', s)

    #remove non-letter characters with space
    s = re.sub(r'\W+', ' ', s)

    #replace I/we/he/she/it to he
    s = re.sub('(I|we|he|she|it)', 'he', s)

    #remove the/a/an/and/or
    s = re.sub('(the|a|an|and|or)', '', s)

    return s

sc = SparkContext(appName="EnronEmailTextFiles")
sc.setLogLevel("WARN")

tb = Blobber(analyzer=NaiveBayesAnalyzer())

counter = 0
counter_print = 0

outfile = open('/home/ec2-user/sentiment_test.csv', 'w')

for root, directories, filenames in os.walk('/enron/staging'):
        sc.parallelize(filenames, 8)

        for f in filenames:
                file_be_processed = 'file:' + root + '/' + f
                files = sc.wholeTextFiles(file_be_processed)

                counter = counter + 1
                counter_print = counter_print + 1

                if counter_print > 100:
                        counter_print = 0
                        print("Directory: " + root + ", Number of files analyzed: " + str(counter))

                for (filename, content) in files.collect():
                        try:
                                file = open(filename[filename.find('/'):])
                                message = email.message_from_file(file)
                                email_body = message.get_payload()
                                file.close()

                                sentiment = tb(text_preprocessor(email_body))
                                classification = sentiment.sentiment.classification
                                p_pos = sentiment.sentiment.p_pos
                                p_neg = sentiment.sentiment.p_neg
                                fName = filename.split('/')[3]

                                outfile.write("%s,%s,%s,%s\n" % (fName, str(p_pos), str(p_neg), classification))

                        except:
                                print("Data Errors:")
                                print("FILENAME: " + filename)
                                print("SYSTEM ERROR: ", sys.exc_info())

outfile.close()
sc.stop()

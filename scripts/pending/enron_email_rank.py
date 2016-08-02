# /home/w205/spark15/bin/spark-submit /enron_output/enron_email_rank.py

from __future__ import print_function

import re
import sys
import psycopg2
import os
from operator import add
from pyspark import SparkContext

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]


if __name__ == "__main__":

    # Initialize the spark context.
    sc = SparkContext(appName="PythonPageRank")

    try:
        os.remove('/enron_output/enron_emails_to_from_cc.txt')
    except:
        print("no file to remove")

    outfile = open('/enron_output/enron_emails_to_from_cc.txt', 'w')

    cur.execute("delete from email_rank")
    conn.commit()

    cur.execute("select filename, email_from from email_from limit 5000")
    email_from = cur.fetchall()

    for efrom in email_from:

        cur.execute('select email_to from email_to where filename = %s', (efrom[0],))
        email_to = cur.fetchall()
        for eto in email_to:
            outfile.write(efrom[1].replace("\r", "") + " " + eto[0].replace("\r", "") + "\n")

        cur.execute('select email_cc from email_cc where filename = %s', (efrom[0],))
        email_cc = cur.fetchall()
        for ecc in email_cc:
            outfile.write(efrom[1].replace("\r", "") + " " + ecc[0].replace("\r", "") + "\n")

    outfile.close()

    lines = sc.textFile('file:/enron_output/enron_emails_to_from_cc.txt', 1)

    # Loads all URLs from input file and initialize their neighbors.
    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()

    # Loads all URLs with other URL(s) link to from input file and initialize ranks of them to one.
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in range(int(1)):
        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    # Collects all URL ranks and dump them to console.
    for (link, rank) in ranks.collect():
        print("%s has rank: %s." % (link, rank))
	cur.execute("insert into email_rank (email, rank) values (%s, %s)", (link, rank))
	conn.commit()

    conn.close()
    sc.stop()

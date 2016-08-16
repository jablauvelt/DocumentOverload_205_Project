# spark-submit 4_rank_emails.py
# run this on cluster, if spark isn't installed on your instance
# Takes < 1 min on cluster
# grab file from s3 first: aws s3 cp s3://docoverload/enron_emails_to_from.txt /root/enron_emails_to_from.txt
# WHEN DONE, output file back to s3: aws s3 cp /root/enron_emails_ranks.txt s3://docoverload/enron_emails_ranks.txt

from operator import add
from pyspark import SparkContext

# Calculates EMAIL contributions to the rank of other EMAILS
def computeContribs(emails, rank):
	num_emails = len(emails)
	for email in emails:
		yield(email, rank / num_emails)

# Simple parse of email pair string into email pair
def parseNeighbors(emails):
	from_email = ""
	to_email = ""
	try:
		from_email = emails[:emails.index(':::::')].strip()
		to_email = emails[emails.index(':::::')+6:].strip()
	except:
		print("Bad Email Pair: " + emails)
	return from_email, to_email

if __name__ == "__main__":

	sc = SparkContext(appName="PythonEmailRank")

	lines = sc.textFile('file:///root/enron_emails_to_from.txt', 1)

	# Load all EMAILs input file and initialize EMAIL pairs
	links = lines.map(lambda emails: parseNeighbors(emails)).distinct().groupByKey().cache()

	# Load all EMAILs with other EMAIL(s) and initialize to rank of one
	ranks = links.map(lambda email_neighbors: (email_neighbors[0], 1.0))

	# Calculate and update EMAIL ranks continuously using a very basic PageRank algorithm
	for iteration in range(int(1)):

		# Calculate EMAIL contributions to the rank of other EMAIL(s)
		contribs = links.join(ranks).flatMap(lambda email_emails_rank: computeContribs(email_emails_rank[1][0], email_emails_rank[1][1]))

		# Re-calculates EMAIL ranks based upon neighbor EMAIL contributions
		ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

	# Collects all EMAIL ranks and dumps them to csv file
	outfile = open('/root/enron_emails_ranks.txt', 'w')
	for (email, rank) in ranks.collect():
		outfile.write("%s,%s\n" % (email, rank))
	outfile.close()

	sc.stop()

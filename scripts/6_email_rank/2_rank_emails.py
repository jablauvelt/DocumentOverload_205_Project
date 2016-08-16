# spark-submit /home/ec2-user/2_rank_emails.py
# please run this on a cluster
# WHEN DONE, output file back to s3: aws s3 cp /home/ec2-user/enron_emails_ranks.txt s3://docoverload/enron_emails_ranks.txt
# You may need to use AWS configure, if your cluster is not already configured for AWS CLI

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

    # read file from S3
	lines = sc.textFile('s3://docoverload12/enron_emails_to_from.txt')

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
	# Write to EBS as this is much faster than S3, then upload to S3 after processing complete, GO FAST, CLUSTER EXPENSIVE, TERMINATE!
	outfile = open('/home/ec2-user/enron_emails_ranks.txt', 'w')
	for (email, rank) in ranks.collect():
		outfile.write("%s,%s\n" % (email, rank))
	outfile.close()

	sc.stop()

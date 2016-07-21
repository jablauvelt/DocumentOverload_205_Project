#
# Aggregates all email text files into a single 11Gb file
# Monitor file size while generating from the command line using: du -hs /enron_output/enron_emails_text_all.txt
# Upload to Hadoop using the command: hdfs dfs -put /enron_output/enron_emails_text_all.txt /user/w205/enron_emails_text_all.txt
# Appoximate time to generate and upload to Hadoop is 30 minutes using a m3.medium host
#

import os

paths = (
		'/enron_output/text_000', 
		'/enron_output/text_001',
                '/enron_output/text_002',
                '/enron_output/text_003',
                '/enron_output/text_004',
                '/enron_output/text_005',
                '/enron_output/text_006',
                '/enron_output/text_007',
                '/enron_output/text_008',
                '/enron_output/text_009',
                '/enron_output/text_010',
                '/enron_output/text_011',
                '/enron_output/text_012',
                '/enron_output/text_013',
                '/enron_output/text_014',
                '/enron_output/text_015',
                '/enron_output/text_016',
                '/enron_output/text_017',
                '/enron_output/text_018',
                '/enron_output/text_019',
                '/enron_output/text_020',
                '/enron_output/text_021',
                '/enron_output/text_022'
	)

with open ('/enron_output/enron_emails_text_all.txt', 'w') as outfile:

	for p in paths:
		print p
		for root, directories, filenames in os.walk(p):
			for f in filenames:
				pf = p + "/" + f
				print pf
				with open(pf, 'r') as infile:
					outfile.write(infile.read())

#
# Aggregates all email text files into a single 11Gb file
# Monitor file size while generating from the command line using: du -hs /enron_output/enron_emails_text_all.txt
# Appoximate time to generate is 30 minutes using a m3.medium host
#

import os

with open ('/enron_output/enron_emails_text_all.txt', 'w') as outfile:

        for root, directories, filenames in os.walk('/enron_output/staging'):
                for f in filenames:
                        pf = os.path.join(root, f)
                        print pf
                        with open(pf, 'r') as infile:
                                outfile.write(infile.read())


# Aggregates all email text files into a single 11Gb file
# Monitor file size while generating from the command line using: du -hs /enron_output/enron_emails_text_all.txt
# Appoximate time to generate is 30 minutes using a m3.medium host
# I/O waits are clearly the most significant issue with this script; hence, buffer, read from /enron, write to /enron_output

import os
counter = 0

with open ('/enron_output/enron_emails_text_all.txt', 'w') as outfile:
        for root, directories, filenames in os.walk('/enron/staging'):
                for f in filenames:
                        pf = os.path.join(root, f)
                        counter = counter + 1
                        if counter % 10000 == 0:
                            print "Files Merged: " + str(counter)
                        with open(pf, 'r', 1000000) as infile:
                                outfile.write(infile.read())
                        infile.close()
outfile.close()

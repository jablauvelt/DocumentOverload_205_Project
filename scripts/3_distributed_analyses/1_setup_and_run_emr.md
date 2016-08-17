# Setup and run EMR

This file will walk you through the steps necessary to create an EMR cluster and run the files in this folder, which will run analyses in pyspark.

1. AWS -> EMR -> Create Cluster
2. Advanced Options
3. Check Spark box
4. Default location to us-east-1b just to be safe
5. Leave the cluster instances as m3.xlarge. I tried less expensive options but they didn't have enough memory to run distributed Spark, and I got errors. Make sure you have 3 worker nodes and one master node.
6. Select the "docoverload" s3 bucket
7. Use your EC2 key pair that you normally use.
8. Keep the default security groups
9. Create cluster / Finish
10. Go back to security groups (left sidebar in EC2), and edit the default Master Security Group that was just created and add open up the inbound port 22 for SSH.
11. Connect to the Master node the same way you would normally connect to an EC2 instance (use whatever the command is in the "Connect" window for the Master node in the EC2 instances list). But log in as ec2-user instead of root.
12. Exit out of the ec2-user; Use the root account by entering `sudo su` in bash.
13. Install dependencies:
    - `pip install -U textblob`
    - `python -m textblob.download_corpora`
13. Make new scripts on your master node (e.g., `vim /home/w205/doc_overload/2_parse_zips_and_phones.py`), and copy/paste in the code from scripts 2-5 in this folder:
    - `vi 2_parse_zips_and_phones.py`, i for insert and paste script
    - `vi 3_wordcount.py`, ''
    - `vi 4_rank_emails.py`, ''
14. In each script, change the name of the S3 bucket to match the one you created. 
15. Run the scripts in bash as follows: 
   -  `spark-submit 2_parse_zips_and_phones.py`
   -  `spark-submit 3_wordcount.py`
   -  `spark-submit 4_rank_emails.py`
16. Transfer output files to S3 (change bucket name to the bucket used for this project): 
    - `aws s3 cp wordcount.csv s3://docoverload/wordcount.csv` 
    - `aws s3 cp enron_emails_ranks.txt s3://docoverload/enron_emails_ranks.txt`
17. Close the cluster when you're done or your wallet will be very sorry.
18. Run the remaining scripts in this folder on a single instance. 


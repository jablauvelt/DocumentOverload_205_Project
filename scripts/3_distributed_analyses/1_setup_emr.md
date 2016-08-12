# Setup EMR

This file will walk you through the steps necessary to create an EMR cluster, which will run analyses in pyspark.

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
12. Exit out of the ec2-user Use the root account by entering 'sudo su' in bash.
13. Make a new script (e.g., `vim /home/w205/doc_overload/3_parse_zips_and_phones.py`), and copy/paste in the code from `3_parse_zips_and_phones.py`. Change the name of the S3 bucket to match the one you created.
14. Run the scripts 2_parse_zips_and_phones.py and 3_wordcount.py in bash as follows: 
  1. `spark-submit 2_parse_zips_and_phones.py`
  2. `spark-submit 3_wordcount.py`
15. Close the cluster when you're done or your wallet will be very sorry.


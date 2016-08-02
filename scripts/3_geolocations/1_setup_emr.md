# Setup EMR

This file will walk you through the steps necessary to create an EMR cluster, which will run analyses in pyspark.

1. AWS -> EMR -> Create Cluster
2. Advanced Options
3. Check Spark box
4. Default location to us-east-1b just to be safe
5. Leave the cluster instances as m3.xlarge. I tried less expensive options but they didn't have enough memory to run distributed Spark, and I got errors.
6. Select the "docoverload" s3 bucket
7. Keep the default security groups
8. Create cluster / Finish
9. Go back to security groups (left sidebar in EC2), and edit the default Master Security Group that was just created and add open up the inbound port 22 for SSH.
10. [Placeholder - create python script and copy paste it in? Or pull from S3? or from git?]
11. Run in bash, replacing the IP address with the IP of the master: `spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.1 --master spark://54.205.231.220 3_parse_zips_and_phones.py`


#Sentiment Analysis

This file will walk you through the steps necessary to run sentiment analyses in pyspark.

1. Make sure cluster is setup via 3_distributed_analyses/1_setup_emr.md
2. Run 2_setup_env_and_packages.sh to install dependencies
3. Run the script in bash as following:
    `spark-submit 3_sentiment_analysis.py`
4. When completed, copy output file to s3:
    `aws s3 cp /home/ec2-user/sentiment_test.csv s3://docoverload/sentiment_test.csv`
5. Run the following script in a single instance:
    `python 4_sentiment_analysis_to_postgres.py`

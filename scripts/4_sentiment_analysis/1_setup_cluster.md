
1. Run 2_setup_env_and_packages.sh to install dependencies
2. Make sure cluster is setup via 3_geolocations/1_setup_cluster.md
3. Run in bash, replacing the IP address with the IP of the master: `spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.1 --master spark://54.205.231.220 3_sentiment_analysis.py`

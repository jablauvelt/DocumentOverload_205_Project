# Complete instructions to run the project

In 1_setup folder:

1. Follow instructions in 1_setup_core_instance.md to set up the AWS instance
2. Copy and paste insructions from 2_setup_env_and_install_packages.sh in the instance. This will also clone the github repository so you don't have to copy and paste the rest of the scripts by hand.
3. `python 1_setup/3_create_postgres_db.py`
4. `python 1_setup/4_create_postgres_tables.py`
5. `chmod u+x 1_setup/5_extract_xml_metadata_from_zips.sh`
6. `1_setup/5_extract_xml_metadata_from_zips.sh` (~ 30 minutes on m3.medium)
7. `python 1_setup/6_extract_txts_from_zips.py`  (~ 10 minutes on m3.medium)
8. `python 1_setup/7_combine_txts.py` (~ 30 minutes on m3.medium)
9. Follow instructions on 8_setup_aws_cli_and_s3.md

In 2_networks folder:

1. Follow instructions in 1_setup_mongodb.md
2. `python 2_networks/2_import_xml_to_mongo.py`
3. `python 2_networks/3_summarize_and_upload_to_postgres.py`

In 3_distributed_analyses folder: 
Follow instructions in 1_setup_emr.md

In 4_sentiment_analysis folder: 
Follow instructions in 1_setup_cluster.md

In 5_geocode folder: 
Follow instructions in 1_setup_kafka.md

In 6_wordcloud folder: 
Follow instructions in 1_create_wordcloud.md

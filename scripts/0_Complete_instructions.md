# Complete instructions to run the project

In 1_setup folder:
1. Follow instructions in 1_setup_core_instance.md to set up the AWS instance
2. Copy and paste insructions from 2_setup_env_and_install_packages.sh in the instance. This will also clone the github repository so you don't have to copy and paste the rest of the scripts by hand.
3. `python 1_setup/3_create_postgres_db.py`
4. `python 1_setup/4_create_postgres_tables.py`
5. `chmod u+x 1_setup/5_extract_xml_metadata_from_zips.sh`
6. `1_setup/5_extract_xml_metadata_from_zips.sh`
7. `python 1_setup/6_extract_txts_from_zips.py`
8. `python 1_setup/7_combine_txts.py`
9. Follow instructions on 8_setup_aws_cli_and_s3.md

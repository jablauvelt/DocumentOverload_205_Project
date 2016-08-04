# Complete instructions to run the project

In 1_setup folder:
- Follow instructions in 1_setup_core_instance.md to set up the AWS instance
- Run 2_setup_env_and_install_packages.sh in the instance
- Before running 3_create_postgres_db, make sure that postgres is started 
	- Check with ps auxwww | grep postgres
	- If not started, run: cd /data , then: /data/start_postgres.sh
- Then run 3_create_postgres_db
- Then run 4_create_postgres_tables.py
- Run 5_extract_xml_metadata_from_zips.sh by :
	- chmod u+x 5_extract_xml_metadata_from_zips.sh
	- ./5_extract_xml_metadata_from_zips.sh
- Run 6_extract_txts_from_zips.py by :
	- nohup python 6_extract_txts_from_zips.py <letter> &
	- Go through all 26 letters
	- (this step takes ~4 hours)

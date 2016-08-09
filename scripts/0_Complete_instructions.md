# Complete instructions to run the project

In 1_setup folder:
1. Follow instructions in 1_setup_core_instance.md to set up the AWS instance
2. Run 2_setup_env_and_install_packages.sh in the instance
3. `python 1_setup/3_create_postgres_db.py`
4. `python 1_setup/4_create_postgres_tables.py`
5. `chmod u+x 1_setup/5_extract_xml_metadata_from_zips.sh`
6. `1_setup/5_extract_xml_metadata_from_zips.sh`
- Run 6_extract_txts_from_zips.py by :
	- nohup python 6_extract_txts_from_zips.py <letter> &
	- Go through all 26 letters
	- (this step takes ~4 hours)

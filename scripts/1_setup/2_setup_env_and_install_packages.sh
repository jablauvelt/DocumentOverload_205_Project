#!/bin/bash

# Instance setup; may need to adjust paths based on volume location

fdisk -l # take note of where the 100G volume is located
chmod a+rwx /data # makes the data folder rwx to all users
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh
# Takes ~6 minutes to complete
./setup_ucb_complete_plus_postgres.sh /dev/xvdf #CHANGE based on path to 100G volume, from above 

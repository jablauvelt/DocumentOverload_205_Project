#!/bin/bash

# Instance setup; may need to adjust paths based on volume location

fdisk -l # take note of where the 100G volume is located
chmod a+rwx /data # makes the data folder rwx to all users
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh
# Takes ~6 minutes to complete
./setup_ucb_complete_plus_postgres.sh /dev/xvdf #CHANGE based on path to 100G volume, from above 

# Python 2.7 install - since the Amazon instance comes with Python 2.6
sudo yum install python27-devel –y
# Check current system Python version
python --version
# --> Python 2.6.6 [for example]
# Rename the current version to reflect its correct version
mv /usr/bin/python /usr/bin/python266
# Create a symbolic link from the file in the path to the version you want to execute
ln -s /usr/bin/python2.7 /usr/bin/python
# Check that the shell picks up the version of Python you intended
python --version
#--> Python 2.7

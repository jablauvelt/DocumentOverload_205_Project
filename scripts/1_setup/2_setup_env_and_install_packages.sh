#!/bin/bash

# Instance setup; may need to adjust paths based on volume location

fdisk -l # take note of where the 100G volume is located
chmod a+rwx /data # makes the data folder rwx to all users
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh
# Takes ~6 minutes to complete
./setup_ucb_complete_plus_postgres.sh /dev/xvdf #CHANGE based on path to 100G volume, from above 

# Mount EBS volumes on the instance
# First, attach enron volume on aws
# Change paths based on where the volumes are
fdisk -l
mkdir /enron
mount -t ext4 /dev/xvdf /enron
mount -t ext4 /dev/xvdg /data

# Create a folder for output data
mkdir /enron_output


# Write all outputs to the enron_output folder

# Steps Taken to Setup the AWS Instance and attach the dataset

In EC2:

Instance setup
- Left sidebar: Instances -> Launch instance
- Search UCB MIDS under "Community AMIs" -< UCB W205 Spring 2016
- Under "instance type", select: General Purpose, m3.large
- For security group, select: Hadoop Cluster UCB
- Launch instance

Enron data volume setup
- Left Sidebar: Elastic Block Store -> Snaphots
- Filter to Public Snapshots
- Search: enron -> EDRM Enron DS v2 and v1
- Click Create Volume (create in same zone as your instance)
- Left Sidebar: Elastic Block Store -> Volumes
- Rename volume "enron"
- Create two other volumes (data: 100G, enron_output: 200G)
- Attach the 100G data volume to instance; wait to attach enron and enron_output until later steps

Connect to instance

Setting up instance (bash script):

fdisk -l # take note of where your 100G volume is located
chmod a+rwx /data # makes the data folder rwx to all users
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh
./setup_ucb_complete_plus_postgres.sh /dev/xvdf #CHANGE based on path to 100G volume, from above 

# Mount EBS volumes on the instance
# Change paths based on where the volumes are
fdisk -l
mkdir /enron
mount -t ext4 /dev/xvdf /enron
mount -t ext4 /dev/xvdg /data
mkfs.ext4 /dev/xvdh # This creates a filesystem on the 200G enron_output volume
mkdir /enron_output
mount -t ext4 /dev/xvdh /enron_output

# Write enron_unpack.py to the enron_output folder, and execute from there

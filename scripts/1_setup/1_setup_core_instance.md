# Steps Taken to Setup the AWS Instance and attach the dataset

###In EC2:

#### Instance setup
- Left sidebar: Instances -> Launch instance
- Search UCB MIDS under "Community AMIs" -< UCB W205 Spring 2016
- Under "instance type", select: General Purpose, m3.large
- For security group, select: Hadoop Cluster UCB
  - Make sure that port 5432 is open 
- Launch instance

#### Enron data volume setup
- Left Sidebar: Elastic Block Store -> Snaphots
- Filter to Public Snapshots
- Search: enron -> EDRM Enron DS v2 and v1
- Click Create Volume (create in same zone as the instance)
- Left Sidebar: Elastic Block Store -> Volumes
- Rename volume 'enron'
- Create another volume called 'data' (100G) and a volume called 'enron_output' (100G) (in the same zone as the instance)
- Attach the 100G data volume to instance; wait to attach enron and enron_output until later steps

#### Connect to instance, and run bash setup script (2_setup_env_and_install_packages.sh)

#### Mount enron and enron_output volumes on the instance
- First, attach enron and enron_output volumes on AWS Elastic Block Storage
- In bash on EC2 instance, create directories:
  - $ mkdir /enron
  - $ mkdir /enron_output
- Set up an ext4 filesystem on the /enron_output volume:
  - $ fdisk -l
  - $ mkfs.ext4 /dev/xvd_ 
- Mount volumes on instance
  - $ mount -t ext4 /dev/xvd_ /enron
  - $ mount -t ext4 /dev/xvd_ /enron_output



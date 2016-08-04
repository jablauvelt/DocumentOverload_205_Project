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
- Click Create Volume (create in same zone as the instance)
- Left Sidebar: Elastic Block Store -> Volumes
- Rename volume 'enron'
- Create another volume called 'data' (100G) (in the same zone as the instance)
- Attach the 100G data volume to instance; wait to attach enron until later steps

Connect to instance, and reference bash setup script

## Steps Taken to Setup the AWS Instance and attach the dataset

###In EC2:

#### Instance setup
- Left sidebar: Instances -> Launch instance
- Search UCB MIDS under "Community AMIs" -< UCB W205 Spring 2016
- Under "instance type", select: General Purpose, m3.large
- 3: Configure Instance Details -> Subnet: Default in us-east-1b
- 4: Add Storage -> Keep default 30 GB store
- 6: Configure Security Group -> Create a new group and open ports 4040, 5432, 50070, 8080, 10002, 10000, 7180, 8088 to Anywhere as Custom TCP rules, and open port 22 to Anywhere as SSH. If you already had the security group Hadoop Cluster UCB, this might match it.
- Launch instance and select or create your key pair

#### Enron data volume setup
- Left Sidebar: Elastic Block Store -> Snaphots
- Filter to Public Snapshots
- Search: enron -> EDRM Enron DS v2 and v1
- Click Create Volume (create in same zone as the instance - us-east-1b)
- Left Sidebar: Elastic Block Store -> Volumes
- Once it's "available", rename volume 'enron'
- Create a 100G volume called 'enron_output' 
  - Click Create Volume to do this.
  - Again, in the same zone as the instance)
- Attach both the `enron` and `enron_output` volume to the instance you just created.

#### Mount enron and enron_output volumes on the instance
- Connect to the instance: 
  - in AWS, click Instances
  - Check box next to the new instance and click connect
  - Copy the example SSH command
  - Navigate to the folder where you saved your key pair file
  - Paste and run the copied command
- Now that you're in n bash on the EC2 instance, create directories:
  - $ mkdir /enron
  - $ mkdir /enron_output
- Set up an ext4 filesystem on the /enron_output volume:
  - $ fdisk -l # identify which drive is which it is by the size shown by this command (should be around 100 GB)
  - $ mkfs.ext4 /dev/xvd_ # for example, /dev/xvdf. 
- Mount volumes on instance
  - $ mount -t ext4 /dev/xvd_ /enron
  - $ mount -t ext4 /dev/xvd_ /enron_output
- Create a "staging" directory in /enron_output
  - $ mkdir /enron_output/staging



#!/bin/bash

#!! do we need this? --> chmod a+rwx /enron_output # makes the data folder rwx to all users

### POSTGRES ------------------------------------------------------------------------
# Setup folders
mkdir /enron_output/pgsql
mkdir /enron_output/pgsql/data
mkdir /enron_output/pgsql/logs
chown -R postgres /enron_output/pgsql
sudo -u postgres initdb -D /enron_output/pgsql/data

#setup pg_hba.conf
sudo -u postgres echo "host    all         all         0.0.0.0         0.0.0.0               md5" >> /enron_output/pgsql/data/pg_hba.conf

#setup postgresql.conf
sudo -u postgres echo "listen_addresses = '*'" >> /enron_output/pgsql/data/postgresql.conf
sudo -u postgres echo "standard_conforming_strings = off" >> /enron_output/pgsql/data/postgresql.conf

# To start postgres service:
sudo -u postgres pg_ctl -D /enron_output/pgsql/data -l /enron_output/pgsql/logs/pgsql.log start
# Check that it's running:
ps auxwww | grep postgres


### PYTHON 2.7 ------------------------------------------------------------------------

# install build tools 
sudo yum install make automake gcc gcc-c++ kernel-devel git-core -y 

# install python 2.7 and change default python symlink 
sudo yum install python27-devel -y 
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python2.7 /usr/bin/python 

# yum still needs 2.6, so write it in and backup script 
sudo cp /usr/bin/yum /usr/bin/_yum_before_27 
sudo sed -i s/python/python2.6/g /usr/bin/yum 
sudo sed -i s/python2.6/python2.6/g /usr/bin/yum 

# should display now 2.7.5 or later: 
python -V 

# now install pip for 2.7 
sudo curl -o /tmp/ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo /usr/bin/python2.7 /tmp/ez_setup.py 
sudo /usr/bin/easy_install-2.7 pip 

### PYTHON PACKAGES ------------------------------------------------------------------------
# Install python packages
pip install psycopg2
pip install pymongo
pip install xmltodict
pip install smart_open

# Pull in scripts from GitHub Repository (this one), so you can run scripts from the command line.
# You will need to replace "your_username" with your git username and enter your password.
cd /home/w205
git clone https://your_username@github.com/jablauvelt/DocumentOverload_205_Project.git
cd DocumentOverload_205_Project/scripts


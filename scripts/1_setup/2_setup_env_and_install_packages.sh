#!/bin/bash

#!! do we need this? --> chmod a+rwx /enron_output # makes the data folder rwx to all users

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

### Start
# To start postgres service:
sudo -u postgres pg_ctl -D /enron_output/pgsql/data -l /enron_output/pgsql/logs/pgsql.log start
# Check that it's running:
ps auxwww | grep postgres

# Install python packages
pip install pymongo

# Pull in scripts from GitHub Repository (this one), so you can run scripts from the command line
cd /home/w205
git clone https://jablauvelt@github.com/jablauvelt/DocumentOverload_205_Project.git
cd /DocumentOverload_205_Project/scripts


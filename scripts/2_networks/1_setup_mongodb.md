# Set up MongoDB

## 1. Install 
(https://docs.mongodb.com/manual/tutorial/install-mongodb-on-amazon/)
- `touch /etc/yum.repos.d/mongodb-org-3.2.repo`
- `vim /etc/yum.repos.d/mongodb-org-3.2.repo`
- In vim, put the following text:
```
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
```
- ... then Esc + :wq + Enter
- `sudo yum install -y mongodb-org`
- `sudo service mongod start`
- `cat /var/log/mongodb/mongod.log` (This checks that the service is running correctly)

## 2. Get python 2.7 running in a virtual env, if you haven't already
The default Amazon setup has python 2.6 - we want to use 2.7
http://docs.python-guide.org/en/latest/dev/virtualenvs/
- Update pip: `pip install --upgrade pip`
- Change to w205 user: `su - w205`
  - You are now in /home/w205
- `mkdir enron_mongodb`
- `cd enron_mongodb`
- `virtualenv venv`
- `virtualenv -p /usr/bin/python2.7 venv`
- `source venv/bin/activate`
  - From now on, any package that you install using pip will be placed in the venv folder, isolated from the global Python installation.
- To deactivate and leave virtual environment: `deactivate`
- To delete a virtual environment, just delete its folder. (In this case, it would be `rm -rf venv`)

## 3. Install pymongo
- Make sure you are in the 2.7 virtualenv
- `python -m pip install pymongo`

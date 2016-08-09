# Set up MongoDB

## 1. Install MongoDB
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

## 2. Install pymongo
- `python -m pip install pymongo`

pip install -U textblob
python -m textblob.download_corpora

mkdir /data/w205
chown w205 /data/w205
sudo -u w205 wget -O /data/apache-maven-3.3.3-bin.tar.gz http://www.trieuvan.com/apache/maven/maven-3/3.3.3/binaries/apache-maven-3.3.3-bin.tar.gz
cd /data/ && sudo -u w205 tar xvzf /data/apache-maven-3.3.3-bin.tar.gz
sudo -u w205 git clone https://github.com/apache/incubator-zeppelin.git /data/zeppelin
cd /data/zeppelin
/data/apache-maven-3.3.3/bin/mvn -Pspark-1.5 -Dhadoop.version=2.6.0 -DskipTests -Phadoop-2.6 clean package
cp conf/zeppelin-env.sh.template conf/zeppelin-env.sh
cp /etc/hadoop/conf/*.xml conf/
cp /data/hadoop/hive/conf/hive-site.xml conf/
echo 'export ZEPPELIN_MEM="-Xmx2048m"' >> conf/zeppelin-env.sh

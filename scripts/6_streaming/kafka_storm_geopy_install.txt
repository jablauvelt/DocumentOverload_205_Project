*********************** KAFKA ***********************
-
1) wget http://apache.mirror.iweb.ca/kafka/0.10.0.0/kafka_2.11-0.10.0.0.tgz
-
2) tar xzf kafka_2.11-0.10.0.0.tgz
-
3) Running Zookeeper:  /root/kafka_2.11-0.10.0.0/bin/zookeeper-server-start.sh /root/kafka_2.11-0.10.0.0/config/zookeeper.properties
-
4) Running a Kafka Server: /root/kafka_2.11-0.10.0.0/bin/kafka-server-start.sh /root/kafka_2.11-0.10.0.0/config/server.properties
-
5) Creating a topic: /root/kafka_2.11-0.10.0.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic getsome3
-
6) Deleting a topic: /root/kafka_2.11-0.10.0.0/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic getsome3
-
7) List topics: /root/kafka_2.11-0.10.0.0/bin/kafka-topics.sh --list --zookeeper localhost:2181
-
*********************** STORM ***********************
-
1) sparse quickstart getsome
-
*********************** TROUBLESHOOTING ***********************
-
1) If Kafka blows up, try removing the following directory:  /tmp/kafka-logs

Watch out for hidden files (they are prefixed by a "."), you need to remove these manually (ls -a)
-
2) If you fill up your Kafka Queues, use kafka_consumer.py to clean them out ASAP.
-

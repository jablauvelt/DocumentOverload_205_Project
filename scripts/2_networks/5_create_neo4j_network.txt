## Instructions on how to export the data and create a network in Neo4j

#### Start postgres in the instance
$ /data/postgres.sh

#### Enter postgres command line
$ cd /data
$ psql finalproject postgres

#### Create edges table, limiting to email count more than 10 (takes ~5 min on a large machine)
SELECT email_from, email_to, count(*) as count INTO edges FROM email_from a INNER JOIN email_to b ON a.filename = b.filename GROUP BY email_from, email_to;
\copy (SELECT * FROM edges WHERE count >10) To '/enron_output/edges.csv' With CSV

#### Create nodes
SELECT email_from INTO nodes FROM edges WHERE count > 10;
INSERT INTO nodes SELECT email_to FROM edges WHERE count > 10;
\copy (SELECT DISTINCT email_from FROM nodes) To '/enron_output/nodes.csv' With CSV

#### Exit postgres cli
\q

# Upload csv files to s3 (change "docoverload" to whatever s3 bucket is used for this project)
aws s3 cp /enron_output/edges.csv s3://docoverload/edges.csv
aws s3 cp /enron_output/nodes.csv s3://docoverload/nodes.csv

### BEFORE MOVING ON: Go to S3 bucket and select edges.csv, nodes.csv; click "Actions" and select "Make puclic"

## In Neo4j

#### Clear the graph
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r

#### Load nodes, create index
LOAD CSV FROM "https://s3.amazonaws.com/s3enronoutput/nodes.csv" AS line
MERGE (:custodian {name:line[0]})

CREATE INDEX ON :custodian(name)

#### Load edges
LOAD CSV FROM
"https://s3.amazonaws.com/s3enronoutput/edges.csv" AS line
MATCH (u:custodian {name:line[0]})
MATCH (v:custodian {name:line[1]})
CREATE UNIQUE (u) -[:EMAILED { w: toInt(line[2])}]-> (v)


#### Visualizing the network
MATCH (n) OPTIONAL MATCH (n)-[r]-() RETURN n,r LIMIT 100

### More queries that could be of interest
#### Find employees by name; e.g., zupper
MATCH (zupper:custodian)
WHERE zupper.name STARTS WITH "zupp"
RETURN zupper

#### Shortest path between two employees
MATCH p=(zupper:custodian {name: 'zupper'})-
[:APPEARED*0..2]-(maggi:custodian {name: 'maggi'})
RETURN p, length(p)
ORDER BY length(p)
LIMIT 1

#### Finding communities
MATCH (zupper:custodian {name: 'zupper'}) -[e:APPEARED]-> (other) <-[f:APPEARED]- (maggi:custodian {name: 'maggi'})
RETURN other
ORDER BY e.w DESC, f.w DESC
LIMIT 5

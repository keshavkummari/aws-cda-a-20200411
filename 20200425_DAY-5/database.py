'''
Database :

1. RDS  (RDBMS - SQL)
- Traditional Applications, 
- ERP
- CRM
- e-commerce

    - Amazon Aurora
    - Postgre SQL 
    - MySQL
    - Mariadb
    - Oracle
    - Microsoft SQL Server 

https://www.mysql.com/products/workbench/
https://dbeaver.io/download/


create database aws;

create database cloudaws;

CREATE TABLE `cloudaws`.student(Id INT,NAME VARCHAR(50),Course VARCHAR(50) ,DOJ DATE,Fee INT)

INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (1,'Ronnie','Python','2017-03-23',40);
INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (2,'Sandeep','SQL','2017-03-23',54);
INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (3,'Sandy','PLSQL','2017-03-23',43);
INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (4,'Enrique','HTML','2017-03-23',23);
INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (5,'Abiel','PERL','2017-03-23',45);
INSERT INTO `cloudaws`.student(id,NAME,Course,DOJ,Fee) VALUES (6,'John','LINUX','2017-03-23',23);

select * from cloudaws.student;

Benefits:
    1. Easy to Administer
    2. Highly Scalable
    3. Highly Available
    4. Fast
    5. Secure
    6. Inexpensive

2. DynamoDB (No-SQL Database)
    - Key-Value 
    - High-Traffic WebApplications
    - e-commerce systems
    - Gaming Applications

# aws2 dynamodb describe-table --table-name cloudbinary

# aws2 dynamodb update-table --table-name cloudbinary --provisioned-throughput ReadCapacityUnits=20,WriteCapacityUnits=10

# aws2 dynamodb update-table --table-name cloudbinary --billing-mode PAY_PER_REQUEST

# aws2 dynamodb delete-table --table-name cloudbinary 

# aws2 dynamodb list-tables 

https://aws.amazon.com/dynamodb/pricing/on-demand/


3. ElastiCache (In-Memory) (Memcached & Redis)
    - Caching,
    - Session Mgmt
    - Gaming
    - Geospatial Applications

4. Neptune (Graph)
    - Fraud Detection
    - Social Networking
    - Reconmmendation Engines

5. Amazon Redshift (Warehouse -  RDS )

6. Amazon QLDB (Ledger)
    - Systems of Record
    - Suppy Chain
    - Registrations
    - Banking Transactions

7. Amazon DocumentDB (Document)
    - Content Management
    - Catalogs
    - User Profiles

8. Amazon Keyspaces (Apache Cassandra Service) (Wide Column)    

9. Amazon Timestream (Time Series)
    - IOT Applications,
    - DevOps
    - Industrial Telemetry


'''
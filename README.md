# Upgrad Capstone Project On Telcom data

**Problem statement**

This Capstone project is based on the domain of the telecom sector. We will be working with a telecom data set and will be required to develop a model to help a company run different marketing campaigns and data monetisation activities around it. We are required to build a model that will predict the demographics of certain users, i.e., their age and gender. 
Our aim is to predict the age and the gender of a particular user using this data. Once we have predicted the gender and age for each user, next task will be to map that particular user to the given target-specific ad campaigns. These campaigns aim to improve customer experience and open avenues for revenue generation through cross-selling and upselling activities, and for partnership with other companies for data monetisation activities.

**Part 1 tasks**

1. Using scoop extract the data from RDS to EMR, Using S3 read extract the data from S3 to EMR
2. Do basic sanity and count analysis on RDS (4 questions)
3. Create external hive tables and do HQL detailed analysis using HQL queries (might need to create few hive internal tables), create analytics report for 6 questions
4. Understand the data issues (event and non-event data)
5. Preparing data for modelling
  a. create 3 data sets, non-event data, event data, app data
  b. report the shape of the datasets
  c. dump data to s3
  
**O/P of Part 1**

**Upload a zip file titled MLC_CapstoneProject__MidSubmission_Your Name containing the following:**

1. The SQL queries and the corresponding results for the SQL tasks (SQLTasks.pdf) - point 2 from above is covered here
2. The script for ingesting the relevant data from AWS RDS and S3 to Hadoop (DataIngestion.txt) - point 1 from above is covered here
3. A report detailing the HQL queries for creating Hive tables and the various queries and results obtained for the HQL tasks mentioned on the platform (HQLTasks.pdf) - point 3 from above is covered here
4. The script to create the data necessary for the next modelling exercises. Do not forget to report the shape of the data set formed here. (DataPreparation.pdf) - point 4 and 5 above are covered here

order - DataIngestion.txt, SQLTasks.pdf, HQLTasks.pdf, DataPreparation.pdf

**RDS Information:**
Endpoint/Hostname: mlc-testcapstone.cyaielc9bmnf.us-east-1.rds.amazonaws.com
username: student
password: STUDENT123
db: mlctest

Command to establish a connection to the instance
mysql -h mlc-testcapstone.cyaielc9bmnf.us-east-1.rds.amazonaws.com -u student -p
STUDENT123
show databases;

**WIthin the RDS, you will find the following data sets:**
events
app_events
brand_devices
train

AWS S3: You have been provided with the public s3 links for the following data sets:
app_labels: https://capstone-project-mlc-metadata.s3.amazonaws.com/app_labels_new.txt
label_categories: https://capstone-project-mlc-metadata.s3.amazonaws.com/label_categories.csv

# Upgrad Capstone Project On Telcom data

**Problem statement**

This Capstone project is based on the domain of the telecom sector. We will be working with a telecom data set and will be required to develop a model to help a company run different marketing campaigns and data monetisation activities around it. We are required to build a model that will predict the demographics of certain users, i.e., their age and gender. 
Our aim is to predict the age and the gender of a particular user using this data. Once we have predicted the gender and age for each user, next task will be to map that particular user to the given target-specific ad campaigns. These campaigns aim to improve customer experience and open avenues for revenue generation through cross-selling and upselling activities, and for partnership with other companies for data monetisation activities.

**Part 2 tasks**

Model Building Subtasks
1.	Reading Data
  a)	Read the data from S3 in EC2
2.	Cleaning Data
  a)	Example: Geospatial Data (Lat and Long =0 and btw -1 and 1)
  b)	Other Data Cleaning required - missing values and appropriate imputation required
3.	Basic EDA and Visualisation - Ec2 in python notebooks, include necessary libraries
  1.	Plot appropriate graphs representing the distribution of age and gender in the data set [univariate].
      -age and gender are the target variables, so distribution/% of male and female are there in the dataset has to be analysed
  2.	Boxplot analysis for gender and age [bivariate].
      -trend analysis btw the gender(male and female) and with the age
  3.	Plot the percentage of the device_ids with and without event data. 
      -some % of device ids have event data and some dont - plot this over a graph
  4.	Plot a graph representing the distribution of events over different days of a week. 
      -events associated wit ts, with ts figure different days of weeks, then plot it over sun-sat...and analyse the distribution and pattern
  5.	Plot a graph representing the distribution of events per hour [for one-week data].
      -events per hour, similar to 4, choose 1 week of data
  6.	The difference in the distribution of events per hour for Male and Female consumers. [Show the difference using an appropriate chart for one-week data.]
      -same as 5 1 week of data, trends where males are more active vs females
  7.	Is there any difference in the distribution of Events for different Age Groups over different days of the week? [Consider the following age groups: 0–24, 25–32, 33–45, and 46+]
      -plot event data over differnt days of the week from timestamp, analysse for agegrps
  8.	Stacked bar chart for the top 10 mobile brands across male and female consumers.
      -top 10 mobile brands
      -stacked bar chart of male and females for each of the brand
  9.	Prepare a chart representing the ten frequently used applications and their respective male and female percentage.
      -most frequent 10 of them
      -% of female n male
      -some apps are heavily used by males nd some by females
  10.	List the top 10 mobile phone brands bought by customers by age groups. [Consider the following age groups: 0–24, 25–32, 33–45, and 46+]
      -first take age grps and then plot of the top the mobile brands
3.1 Feature Engineering tasks
    -Considering the events data, you can create a feature called Average Events, which can give you an estimate of how long the users' mobile phones are active.
    -You can use the information related to the location of the users (latitude and longitude data) to create features representing changes in the latitude and longitude details at different times of the day.
    -You can create features such as Median Latitude and Median Longitude for different event ids.
    -You can also group the existing categories to create a new supercategory that will establish a significance in predicting the outcome variable.
4.	Advanced Visualisation and Clustering
  a)	Geospatial Visualisation
      -basemap one of the Matplotlib toolkits under the mpl_toolkits
      1.	Plot the visualisation plot for a sample of 1 lakh data points.
          -sample 1 lakh data points of lat n long and visualize the data poitns on the map and analyse
      2.	Compare the event visualisation plots based on the users' gender information. [This can be done on the sample of 1 lakh data points.]
          -sample of 1 lakh points. visualization of several events or differnt lat and long on the map basis the gender info - different plot for male and female and check for differneces
      3.	Compare the event visualisation plots based on the following age groups:
        a)	0–24 
        b)	25–32
        c)	32+
  b)	DBSCAN Clustering as a preprocessing technique
      -clustering
  c)	Final Data Preparation and Train-Test Splitting
      Convert categorical data to numerical data
      -one hot/label encoding from pandas
      -csr matrix from scipy - sparse matrix
      -use the mapping file to split the device ids in train and device ids in test
11th Jan 2023 --------------------------------------------------------------------------------------------------------------------------
5.	Model Building: Different Models
  a)	Segmenting the data [Scenario 1 and Scenario 2] 
  b)	Gender and Age Prediction
  c)	Model Evaluation
18th Jan 2023 --------------------------------------------------------------------------------------------------------------------------
Deployment Subtasks
1.	Select the best model based on the model evaluation metrics for only Scenario 1 [age and gender prediction]
2.	Export the models as pickle files and save the pickle files
3.	Keep the test split created prior to the model building phase safe in order to integrate it with the flask application
4.	Create a flask application that can be exposed as an API endpoint 
  a)	Design a flask application
  b)	Dockerize the application
  c)	Deploy the application on EC2
23rd Jan 2023 --------------------------------------------------------------------------------------------------------------------------

**O/P of Part 2**

**Upload a zip file titled MLC_CapstoneProject__FinalSubmission_Your Name containing the following:**

Order - 

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

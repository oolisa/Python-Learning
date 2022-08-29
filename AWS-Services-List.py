# AWS List of Services

#1. Create an empty list. 
awsservices_list = []

#2. Populate the list using append or insert.

awsservices_list.append("EC2")
awsservices_list.append("IAM")
awsservices_list.append("S3")
awsservices_list.append("VPC")
awsservices_list.append("CloudFormation")
awsservices_list.append("Elastic Beanstalk")

#3. Print the list and length of the list.
print(awsservices_list)
print (len(awsservices_list))

#4. Remove two specific services from the list by name or by index.

awsservices_list.remove("VPC")
awsservices_list.remove("CloudFormation")
print(awsservices_list)

#5. Print the new list and the new length of the list.

print(awsservices_list)
print (len(awsservices_list))









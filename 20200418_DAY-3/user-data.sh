#!/bin/bash
sudo apt-get update -y 
sudo  apt-get install vim curl wget unzip tree git -y 
sudo apt-get -y install apache2 
cd /var/www/html/
sudo git clone https://github.com/keshavkummari/codewithckk.git
cd /var/www/html/codewithckk/
sudo mv * /var/www/html/ 



A Launch Configuration :

STEP-1 : AMI(Linux | Windows)

STEP-2 : Instance Type 

STEP-3 : User Data 

STEP-4 : EBS Volumes

STEP-5 : Security Groups

STEP-6 : SSH Key Pairs

AutoScaling :

STEP-1 : Min Size / Max Size / Initial Capacity 

STEP-2 : Network + Subnets Information

STEP-3 : Loadbalancer 

STEP-4 : Scaling Policies :
            
            Increase Scaling :
            
            CloudWatch Alarms 

            Decrease Scaling : 

            CloudWatch Alarms 

100 Users  ====>> 200 

t2.micro instance 1 core process and 1 gb  : 46 

MIN Instances are  : 2  (92 Users ) + 2 instance (92 Users ) = 200 Users (80 Users)

 
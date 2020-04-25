'''

STEP-1 : Create a Security Group and allow port number 2049

STEP-2 : Create EFS :

    - Associate with 2 Availability Zones
    - Map Security Group

STEP-3 : Launch 2 EC2 instances part of two different AZ's 
    
    - Execute UserData 
    - Map EFS part of Webserver DocumentRoot 

https://docs.aws.amazon.com/efs/latest/ug/mount-fs-auto-mount-onreboot.html
'''
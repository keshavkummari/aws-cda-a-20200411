#!/bin/bash
sudo yum update -y
sudo yum install httpd24 -y 
sudo service httpd start
sudo chkconfig httpd on
sudo su
host_name=`curl -s http://169.254.169.254/latest/meta-data/local-hostname`
echo "<html><head><title>Server-1</title></head><body><h1>Server-1</h1><h2>$host_name</h2></body></html>" > /var/www/html/index.html
echo "$host_name" >> /var/www/html/index.html
echo "done"

#!/bin/bash
sudo yum update -y
sudo yum install httpd24 -y 
sudo service httpd start
sudo chkconfig httpd on
sudo su
host_name=`curl -s http://169.254.169.254/latest/meta-data/local-hostname`
echo "<html><head><title>Server-2</title></head><body><h1>Server-2</h1><h2>$host_name</h2></body></html>" > /var/www/html/index.html

#!/bin/bash
yum install wget* curl* vim* unzip* -y
yum update -y
yum install http* --skip-broken -y
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-c3bb5d40.efs.us-east-1.amazonaws.com:/ /var/www/html/ 
cd /opt/
wget https://www.free-css.com/assets/files/free-css-templates/download/page231/bizexpress-v1.0.1.zip
unzip *.zip
cd Biz*
mv * /var/www/html/
chkconfig httpd on
service httpd start



mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-70c714f1.efs.us-east-1.amazonaws.com:/ /var/www/html/

[root@ip-172-31-92-221 ~]# df -TH
Filesystem     Type      Size  Used Avail Use% Mounted on
devtmpfs       devtmpfs  506M   62k  506M   1% /dev
tmpfs          tmpfs     517M     0  517M   0% /dev/shm
/dev/xvda1     ext4      8.4G  1.2G  7.2G  15% /

# AutoScalingGroup + Application Load Balencer Lab
This is my second lab in my Exam. Ask you to create Auto Scaling Group + Application Load Balencer + Target Group on your own.

### Prepare
Create your own VPC for simulate the Lab. You can create a new VPC with new featu


```
yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y httpd mariadb-server
systemctl start httpd
systemctl enable httpd
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
```
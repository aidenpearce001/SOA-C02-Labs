# AutoScalingGroup + Application Load Balencer Lab
This is my second lab in my Exam. Ask you to create Auto Scaling Group + Application Load Balencer + Target Group on your own.

### Prepare
Create your own VPC for simulate the Lab. You can create a new VPC with new feature by one click or do it the old way.

### Start the Lab

#### There are three requirements:

- Create 2 Security group
    - First Security Group for ALB which only allow inbound on port 80
    - Second Security Group for ASG which only allow traffic from ALB on port 80
- Create ALB
    - Internet facing
    - Security Group only allow inbound on port 80
    - Health check path: index.html
- Create ASG with
    - launch configuration:
        - Instance type: t3.nano
        - Security Group : Only allow traffic from ALB
        - User Data
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
    - Group Size:
        - Minimum and Desired Capacity: 2
        - Maximum Capacity : 4
    - Create Target Tracking Policy with:
        - Average CPU ultilization : 75 

<b>First requirement:</b>

<b>Second requirement:</b>

<b>Third requirement:</b>
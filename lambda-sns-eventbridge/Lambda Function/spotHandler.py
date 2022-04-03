import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
REGION = os.environ['REGION']

ec2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):

    init_script = """
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
      echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php"""

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        InstanceMarketOptions={
        'MarketType': 'spot',
        'SpotOptions': {
            'MaxPrice': '0.005',
            'SpotInstanceType': 'one-time',
            'InstanceInterruptionBehavior': 'terminate'
        }
        },
        UserData=init_script)

    instance_id = instance['Instances'][0]['InstanceId']
    print(instance_id)

    return instance_id
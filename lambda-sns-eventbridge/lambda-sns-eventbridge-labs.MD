# EventBridge + Lambda + SNS Lab
This is the first lab that i got in my SOA-CO02 Exam. It's already have 2 lambda Funtion and the lab ask you to:
- Using EventBridge to run the first lamda function every 15 minutes
- Setup SNS Topic (Without Subscribe) and the Second Lambda Function it's running a new Spot Instance if one Spot Instance got terminated (You cant view the Lambda Function). And using EventBridge to trigger SNS topic

### Prepare 


You now have an SNS topic that CloudWatch Events can send the EC2 Spot Interruption Notification to, let’s configure CloudWatch to do so. In the AWS Management Console, go to Cloudwatch -> Events -> Rules and click Create Rule.

Under Service Name select EC2 and under Event Type select EC2 Spot Instance Interruption Warning

On the right side of the console, click Add Target, scroll down and select SNS topic -> select your topic name, Your result should look like this:

Click Configure Details in the bottom right corner.

Provide a name to your CloudWatch Events rule and click Create rule.

<p align="center">
  <img  width="460" height="300" src="Images/0.PNG">
</p>

1. Creating  
2.
3.
4.

Let's navigate to AWS Identity and Access Management (IAM) to create a role for our AWS Lambda function.
Select Role > Create Role > Select AWS service > Select Lambda As a use case and create a role with the below policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "ec2:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

AMI
Key: AMI
Value: Open EC2 in a new browser tab, click Launch Instance and copy and paste the ami value listed after Amazon Linux 2.
2. INSTANCE_TYPE
Key: INSTANCE_TYPE
Value: t2.micro
3. KEY_NAME
Key: KEY_NAME
Value: The name of the EC2 key pair you created earlier.
4. REGION
Key: REGION
Value: The name of the Region.
5. SUBNET_ID
Key: SUBNET_ID
Value: Navigate to VPC > Subnets, and copy and paste the ID of one of the public subnets in your VPC.

{
    "instance": "$.detail.instance",
    "state": "$.detail.state"
}

"Instance <instance> is in <state>"



{"version":"0","id":"6009a9f4-cc7a-8a77-46f2-310520b31e0f","detail-type":"EC2 Spot Instance Interruption Warning","source":"aws.ec2","account":"<account-id>","time":"2019-05-27T04:52:57Z","region":"eu-west-1","resources":["arn:aws:ec2:eu-west-1b:instance/i-0481ef86f172b68d7"],"detail":{"instance-id":"i-0481ef86f172b68d7","instance-action":"terminate"}}
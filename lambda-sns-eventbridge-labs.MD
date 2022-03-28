# Spot Instance Interruption Handler

## Introduction
[Amazon EC2 Spot instances](https://aws.amazon.com/ec2/spot/) are spare EC2 capacity offered with an up to 90% discount compared to On-Demand pricing with the only consideration that they can be reclaimed with a two-minute warning if EC2 needs the capacity back. This two minutes warning is provided via the local EC2 metadata endpoint of each instance type (http://169.254.169.254/latest/meta-data/spot/instance-action) and via a an (optional) [Amazon EventBridge event](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-eventbridge-rule.html), which can trigger a set of actions to gracefully handle the interruption.


You now have an SNS topic that CloudWatch Events can send the EC2 Spot Interruption Notification to, let’s configure CloudWatch to do so. In the AWS Management Console, go to Cloudwatch -> Events -> Rules and click Create Rule.

Under Service Name select EC2 and under Event Type select EC2 Spot Instance Interruption Warning

On the right side of the console, click Add Target, scroll down and select SNS topic -> select your topic name, Your result should look like this:

Click Configure Details in the bottom right corner.

Provide a name to your CloudWatch Events rule and click Create rule.
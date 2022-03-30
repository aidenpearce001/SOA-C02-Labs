# SOA-C02-Labs

1. Creating Eventbridge for each Lambda Funtion:
- Creating a Schedule Eventbridge that excute Lambda Funtion every 15 minutes
- Creatung a source event from lambda when a Spot Instance Termination and pulish to SNS Topic (SNS Topic dont have to create any notification subscribe)
2. Create ASG + ALB
- Create Security Group for ALB only allow 80 from Internet
- Create Security Group for Target Group only allow 80 from ALB SG
- Create Target Group
- Creat ALB with health check /index.php
- Create Auto Scaling Group with Lauch temaple:
 - Specific AMI that they give
 - T3.nano
- Create Target Tracking Group with atleast 2 Instance running and maximim Instance it's 4. Scaling when Average CPU above 75
3. Create AWS WAF
- AWS managed Rules SQLi
- Custom rate-based rule deny if 100 request in 5 mins (default) to URi path: /login
- Custom rule allow only IP-set 
4. Create 2 S3 bucket
- Enable encrypt at Rest 
- Access logging
5. Create VPC Prive + VPC Public with Nat Gateway
6. Create RDS Backup plan 
- Monthly
- Daily 

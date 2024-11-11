import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-06b21ccaeff8cd686',
    InstanceType='t2.micro',
    KeyName='remote',
    MaxCount=1,
    MinCount=1
)

import boto3
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    client = ec2.create_tags(
       Resources=[
       '****************',
       ],
       Tags=[
        {
            'Key': 'Name',
            'Value': 'PracticeLambda',
        },
        {
            'Key': 'Dept',
            'Value': 'AWSFocusGroup'
        }
        ])


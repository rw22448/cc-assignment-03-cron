import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table("active-users-dev")

scan = table.scan()

with table.batch_writer() as batch:
    for active_user in scan['Items']:

        batch.delete_item(
            Key = {
                'username': active_user['username']
            }
        )

print(table.scan());
import os
import time
import boto3
from dotenv import load_dotenv


def main():
    load_dotenv()
    sqs_region_name = os.getenv('SQS_REGION_NAME')
    sqs_access_key_id = os.getenv('SQS_ACCESS_KEY_ID')
    sqs_secret_access_key = os.getenv('SQS_SECRET_ACCESS_KEY')
    output_queue_name = os.getenv('OUTPUT_QUEUE_NAME')

    sqs = boto3.resource('sqs',
                         region_name=sqs_region_name,
                         aws_access_key_id=sqs_access_key_id,
                         aws_secret_access_key=sqs_secret_access_key)
    queue = sqs.get_queue_by_name(QueueName=output_queue_name)
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        for msg in messages:
            print(msg.body)
            msg.delete()
        time.sleep(1)
        print('Waiting for message...')


if __name__ == '__main__':
    main()

import os
import json
import boto3
from dotenv import load_dotenv


def main():
    load_dotenv()
    sqs_region_name = os.getenv('SQS_REGION_NAME')
    sqs_access_key_id = os.getenv('SQS_ACCESS_KEY_ID')
    sqs_secret_access_key = os.getenv('SQS_SECRET_ACCESS_KEY')
    input_queue_name = os.getenv('INPUT_QUEUE_NAME')

    task = """{"id": "123", "type": "tts", "content": "xin chào nami", "rate": 1.0, "accent": 1, "audio_format": "mp3"}"""
    task = json.loads(task)

    sqs = boto3.resource('sqs',
                         region_name=sqs_region_name,
                         aws_access_key_id=sqs_access_key_id,
                         aws_secret_access_key=sqs_secret_access_key)
    queue = sqs.get_queue_by_name(QueueName=input_queue_name)
    res = queue.send_message(MessageBody=json.dumps(task))
    print(res)


if __name__ == '__main__':
    main()

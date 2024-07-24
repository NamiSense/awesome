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

    task = """{"id": "1058e5e2-3b15-400b-88df-de344f8d95d8", "type": "analysis", "url": "https://nmw-for-qa.s3.ap-southeast-1.amazonaws.com/jpsaas-ex/Call-01.wav?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0yIkcwRQIhALmKuxTG8b1c8wFsSPW5rqD%2Bg0R0xDVrpF6XQjO%2B648XAiAY7vOlx7iuUzB1RPI%2BKSonaO%2FXQwTVpmVdp0XNGiCo1iqJAwhbEAEaDDMzNzE5NTI4NzM0MiIMFkJbYJyQJ8xoS5FWKuYCIa4bH4d7eNhsn9%2Bhlgjga9D4AyTognbo2F20zoVJ0THHOjNJAJyTcbudkAivYYTsmsZrhL2cD6c2zXvlsnpWTNmYFArOS7gbbrrBgWD61%2F9V1gOUANaWRoEeZEcLP%2BbJ4nE4DhSOwu4I4GYHfDKZ8UfcwqgheA28pvTFOWYDlI3D%2FEG%2BQKopCVySQxbdBHs%2BUq4rPQJSHw57YWueaA4PAdH4Ex%2F1OodBE%2Bv3Cd3x%2BpzdTxmFkO9zh9SS4PpmSLq0N9aYmdNzfPssdPCm9FYaRcylqw0qBa7Z8AHYo88EZYJmbmpT1s6D8dAVDi7PWR8A6noFCqsXHSeSinK7D5gG%2BlVVkqwQULBDwUsJkT9bqYNWONYtoFw6sg0ACASCXZfbCCMKzueEnPbG7GMdzyYq2L3oPDn%2BwTfLyVyO6%2FkJRfKuRS0vDqW%2BliTm0OBJ5yKMUaEKNXGW5XkjUyj6GJ%2FzQ%2Fh4rvrdZjCrz760BjqzAnLLttP8WM1NuTIrvAS7S5iroK3rWb80xlQflrHyvpQ1z2pN%2BYpuREx7WA4yAqi2%2BGSSadajEesrRwA%2BlMBqCHHuRYLWvLa%2B23u%2BdaDAEzIPb3p878FVRHaqdm9nKcwMdTEdofk52gtJL%2F%2FdIScYUctLVYxKwxjGMc8sTJEq5LRdhalb1WuGgO6eC85AlLe5V3thkD%2F%2FCV3YjHqdXPs4GsL8jEbc%2F0GILzgAOVLCjC2iFYdj42K6KxpHtsM5uVqM%2FZ0Hwr2oJzXURp25Ajn6ELt7mD70Se6PPrRuDBXbP6hapxa99mC0xKV%2BZi1VznZL6RbDYt5spcTpb5jFhpTmhogmzbWFNIsYuVfVndjEoEFDZrav2%2FrVHaM5%2BFJprByIVp1ALtOVVOw7BdkcM5pjIuVi2jc%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240711T130438Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAU5ATHYMXKY7WK556%2F20240711%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=dd1a36a288aa804b1c6d3897e9acbec1a9a80e02971505c55752789a4a5eed60", "lang": "jp", "num_speakers": 2}"""
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

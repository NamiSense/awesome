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
    tenant_id = os.getenv('TENANT_ID')

    task = """{"id": "1058e5e2-3b15-400b-88df-de344f8d95d8", "type": "analysis", "url": "https://nmw-for-qa.s3.ap-southeast-1.amazonaws.com/jpsaas-ex/Call-01.wav?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0xIkYwRAIgb3eZ92grXHiTnqMS%2Bw1v%2FkOdyB1%2Fa6O1kOSx18lsKSUCIAyL%2FAfLaAPEIEPFd%2BQL6NlAKuwwhbidscWZ2OZUOQ80KpIDCMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMzM3MTk1Mjg3MzQyIgxYYCVfAyRWfEVH5Qsq5gJ1LWlgfGVqKKBBkh3CnmM71y976lBjgiCLH5DkvqzQTrgfq0mMLbWTpR9q55Sl0y1xZ6sGpqD1lmYu5Tpi55BNCptVJZWbk6SuP8xRIC2vDq3a6IUH1Xo2sbE6WxAOFSS5RZw0xxiIAg0fc1rFoeGYOgHCoqIxXIAxzCitjHNqdVeztu7RItO911VCoqq9gqeqr%2BhEolAMcgTAjMCIuOSmp1PBaAQhGDHvn81b8C%2B4n7oLbwEnS03qgYbwL2qr82XF3smgnB5mRkZ3nHGCqkWjIo2YeAuAFCdmlFQaqa3riQFAjwewwWy%2F4Oro7urW41Cv0qpAtclyhPzS8hZVnbpbcNkkFmA3gUytcZT4qkK6y0P95VBhoUus5y2HvwQQaAnStxKnhx5QAGRfiUY4ZWsNtnwIyXBalzTrG3NBIotO4SUbCPoyJpisAdlryd2USOiognxnn%2FY6k89aTheikYX1p63kTBswMIeO%2FbcGOrQCuWMrIHHoA%2FRlZdaDbXRi7X8d2YMpFyZmqPTW3FArz0KT7w9XjlvAI9%2FGicPtqxXDERx%2BAY9ygzgxTjq9iDzBf%2F3ZkUvBiOVrrY55pZ7eYzm%2Fq%2BRZ1AaxHHTtj3UcqX5fT6aaSFH9dBvMP7YrwDnLrD%2BGf0zJkZ%2BZ2Iea4FF66nvi%2FNrDi3pibDS4B3IVvXkvEm5NNjFnjI0Pfno8rbgrXuTe8GBgydM%2Bxj8XeszDa4LWQY2KnkjzncaMDJ0bN2bxGLL4VXaovmfNZc7nL0YbzqvYRf20JkickgisF0smWq1FqAUwUYazlC9ksHRCEWoA615E1sX%2FYlNUADbQT217%2BfBYGm2PFWIzZgkZmTcpyU4i5pez8ysF9qFXQ75a7ev%2FTRIDBxpnreAxYVqaYxHJdXVHaiw%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241004T022326Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAU5ATHYMXITPY5PR7%2F20241004%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=0f4684399bfb5208af6f7239f067a71eb4563d6bb6d0257771de4ed4aa013490", "lang": "jp", "num_speakers": 2}"""
    task = json.loads(task)
    task['tenant_id'] = tenant_id

    sqs = boto3.resource('sqs',
                         region_name=sqs_region_name,
                         aws_access_key_id=sqs_access_key_id,
                         aws_secret_access_key=sqs_secret_access_key)
    queue = sqs.get_queue_by_name(QueueName=input_queue_name)
    res = queue.send_message(MessageBody=json.dumps(task))
    print(res)


if __name__ == '__main__':
    main()

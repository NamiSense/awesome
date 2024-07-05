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

    task = """{"id": "1058e5e2-3b15-400b-88df-de344f8d95d8", "type": "analysis", "url": "https://nmw-for-qa.s3.ap-southeast-1.amazonaws.com/jpsaas-ex/JP%20Callcenter%20-%2001%20-%20Very%20Good%20Quality%20-%20New%20costomer.wav?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLXNvdXRoZWFzdC0yIkcwRQIgTJQujs1RL%2F8EQY%2FjEGS0XvZ8rMTbDWpKRd%2FEkccF7gYCIQCyrrIZmPxOUtHYMsnoWBJfmMz87vQxzwNQJv5i55qtWSqSAwi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDMzNzE5NTI4NzM0MiIM39kPu7GlB%2FHc2QthKuYCC%2Bg%2FuAuByP1xsylAfFHIsNMxfvGnvtNqkywuucgt0GiiqKQxaHuob%2FOfyCu3j45TyiwDQWmS%2BCWn0gUk8b5%2BOYAZhFekrHZS8RCozKsaZb%2BLmjj6UvkVnL3CyEis76CkvD4ogBKZH9MrSuDjQAOyi6YNoG4%2BroUiFqdoGMhAC9bc2yleD743TsRQDZAB56dz24rJn4VB5ivPwLScHxFrV16FyO%2FWrzhuYGXS4fBk1Jt%2B3GoPOnRJ4Fg8vFa6KzCJq0H7WBK44J9%2FuuOumzxCQuQOTdVbqjVdIKmc3reera8mhuMRLtMhEDb555BlMCjly94JyvglcCV3EaE%2B8PV5LjWxhcW2g5D7f%2BKh0ZTgYifkoRVvtzHkYgMmFS3SjIUlRSNExijgy5vp5BmojPjaKlHHQC5R%2BQ%2BBrt5T5fbXSKniOMzOo1M0%2BHX4UJCTXV1gPq3yH05Q6GtDSp5UC3ytd6XTxqGFnDDa1p20BjqzAmQ9bSGmAJDYarbWWcmMAEB%2BzkOuE%2B8ehIIZDW0v6fIW%2FCT1VMAfKnvrDQkkQDRQwmJNEpefKON%2Fwend3belllEryNcuCrX0tKhz6CA4yUgPafW6XzWVd9hzczWMpzBXokHBXkS7mL9fq7TuYqW%2FmWfF%2Bl1pl9Se3b6kY9V%2FUEV2qPaL%2FTGGERz%2BDY21yyhkXrLHUbBuk%2F0JDdWxie0ShTCD%2BYfcuhqy5CJeHUN9lSrkf8xuhlngbxpHIG1ZMYf2f4DOcRcsCsuOrInYRoFRikj0QTEgzVJ7G2zOL4pZ1STVELQnkUt39HNuV56IZJmyTLyi3gS%2Fq2nOc9bw%2F0cwjGiqmoqe2cU7VKSrYv8g1d5EtxwljLC0nv1Z%2F%2FZXJCW7QtF2PSid3ei2nNe8Slni7ZcadB8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240705T040501Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAU5ATHYMXHRMVVRVK%2F20240705%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Signature=4c596212935827cf52ed02dd0141ad52695787a146cc9368079b06e82006dd98", "lang": "jp", "num_speakers": 2}"""
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

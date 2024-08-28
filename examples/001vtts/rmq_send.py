import os
import pika
import json
from dotenv import load_dotenv


def main():
    load_dotenv()
    rmq_host = os.getenv('RMQ_HOST')
    rmq_port = os.getenv('RMQ_PORT')
    rmq_username = os.getenv('RMQ_USERNAME')
    rmq_password = os.getenv('RMQ_PASSWORD')
    input_queue_name = os.getenv('INPUT_QUEUE_NAME')

    task = """{"id": "123", "type": "tts", "content": "xin chào nami", "rate": 1.0, "accent": 1, "audio_format": "mp3"}"""
    task = json.loads(task)

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=rmq_host, port=rmq_port,
        credentials=pika.PlainCredentials(rmq_username, rmq_password)))
    channel = connection.channel()

    channel.queue_declare(queue=input_queue_name)

    channel.basic_publish(exchange='', routing_key=input_queue_name,
                          body=json.dumps(task, ensure_ascii=False).encode('utf-8'))
    connection.close()


if __name__ == '__main__':
    main()

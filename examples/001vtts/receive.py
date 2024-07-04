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
    output_queue_name = os.getenv('OUTPUT_QUEUE_NAME')

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=rmq_host, port=rmq_port,
        credentials=pika.PlainCredentials(rmq_username, rmq_password)))
    channel = connection.channel()

    channel.queue_declare(queue=output_queue_name)

    def callback(ch, method, properties, body):
        json_body = json.loads(body)
        print(json_body)

    channel.basic_consume(queue=output_queue_name,
                          on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    main()

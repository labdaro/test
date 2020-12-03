import pika
import sys

credentail = pika.PlainCredentials('face-recognition', 'face123')
connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.0.226', port=5672, virtual_host='/', credentials=credentail))
channel = connection.channel()

channel.queue_declare(queue='home', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='home',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
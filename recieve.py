import pika
import time

credentail = pika.PlainCredentials('face-recognition', 'face123')
connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.0.226', port=5672, virtual_host='/', credentials=credentail))
channel = connection.channel()

channel.queue_declare(queue='home', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='home', on_message_callback=callback)

channel.start_consuming()
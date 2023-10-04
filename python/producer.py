import os
import pika

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')  # You can change this if needed
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel

channel.exchange_declare(exchange='test_exchange')  # declare exchange
channel.queue_declare(queue='test_queue')  # declare queue
# create binding between queue and exchange
channel.queue_bind(queue='test_queue', exchange='test_exchange', routing_key='tests')

# publish message
channel.basic_publish(
    body='Hello RabbitMQ!',
    exchange='test_exchange',
    routing_key='tests'
)
print(' Message sent.')
channel.close()
connection.close()

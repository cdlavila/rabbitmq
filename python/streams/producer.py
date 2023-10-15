import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

# Declare a Stream, named test_stream
channel.queue_declare(
  queue='test_stream',
  durable=True,
  arguments={"x-queue-type": "stream"}
)

# Publish a message to the test_stream
channel.basic_publish(
  exchange='',
  routing_key='test_stream',
  body='Welcome email message'
)
print("Message sent.")
channel.close()
connection.close()
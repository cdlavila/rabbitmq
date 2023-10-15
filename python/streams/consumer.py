import pika, os, time

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel

# Declare our stream
channel.queue_declare(
  queue='test_stream',
  durable=True,
  arguments={"x-queue-type": "stream"}
)

def send_welcome_email(msg):
  print("Welcome Email task processing")
  print(" [x] Received " + str(msg))
  time.sleep(5) # simulate sending email to a user --delays for 5 seconds
  print("Email successfully sent!")
  return

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  send_welcome_email(body)

# Set the consumer QoS prefetch
channel.basic_qos(
  prefetch_count=100
)

# Consume messages published to the stream
channel.basic_consume(
  'test_stream',
  callback,
  # arguments={"x-stream-offset": 50}
  # arguments={"x-stream-offset": "fist"}
  # arguments={"x-stream-offset": "last"}
)

# start consuming (blocks)
channel.start_consuming()
connection.close()
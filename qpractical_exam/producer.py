import pika

# RabbitMQ connection URL
connection_url = "the_url_provided_by_cloudamqp"
queue_name = "the_queue_name_provided_by_cloudamqp"
routing_key = "the_routing_key_provided_by_cloudamqp"
exchange_name = "the_exchange_name_provided_by_cloudamqp"

# Create a connection to the RabbitMQ server
parameters = pika.URLParameters(connection_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

try:
    # Declare the exchange
    channel.exchange_declare(exchange=exchange_name, exchange_type="direct")

    # Declare the queue
    channel.queue_declare(queue=queue_name, durable=True)

    # Bind the queue to the exchange with the specified routing key
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    # Message content
    message_body = "Hi CloudAMQP, this was fun!"

    # Create a persistent message
    properties = pika.BasicProperties(
        delivery_mode=2,  # Make the message persistent
    )

    # Publish the message
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message_body,
        properties=properties
    )

    print("Message sent!")

finally:
    # Delete the exchange and the bindings
    channel.exchange_delete(exchange=exchange_name)

    # Close the channel and the connection
    channel.close()
    connection.close()

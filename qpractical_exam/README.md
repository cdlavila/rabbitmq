# Practical Exam

## Description

Connect to the RabbitMQ server with:
amqps://student:XYR4yqc.cxh4zug6vje@rabbitmq-exam.rmq3.cloudamqp.com/mxifnklj

On this broker, we have created a queue, called exam.

Your task is to send a message with the payload Hi CloudAMQP, this was fun! to the queue exam.

The message needs to be a persistent message and make use of the routing key: 267958c0-b8bd-4778-8250-8d2db452d058.

Any exchange you create must be called exchange.267958c0-b8bd-4778-8250-8d2db452d058. You are not allowed to use one of the pre-declared exchanges, such as amq.topic.

Important! When the message is sent, you need to make sure the exchanges and bindings you have created are deleted. Also, that you close the connection to the server.

## Run the solution

```bash
python3 producer.py
```
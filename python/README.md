# RabbitMQ Examples in Python

This repository contains examples of using RabbitMQ in Python.

## Installation

1. Run `cd python`
2. Make sure you have Python 3 installed, if yes, skip to step 5, otherwise go to step 3.
3. Run `python3 -m venv venv` [OPTIONAL]
4. Run `source venv/bin/activate` [OPTIONAL]
5. Run `pip3 install -r requirements.txt`
6. Run `cd queues` or `cd streams` to go to the respective directory
7. Run `python3 consumer.py` to start the consumer 
8. Run `python3 producer.py` to start the producer
9. See the messages being sent and received in the terminal
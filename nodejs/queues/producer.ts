import { AMQPClient, AMQPChannel, AMQPQueue } from '@cloudamqp/amqp-client'

async function startPublisher(): Promise<void> {
  try {
    // Set up a connection to the RabbitMQ server
    const cloudAMQPURL: string = 'amqp://guest:guest@localhost:5672/' // Replace if needed
    const connection: AMQPClient = new AMQPClient(cloudAMQPURL)
    await connection.connect()
    const channel: AMQPChannel = await connection.channel()

    console.log("[✅] Connection over channel established")

    // Declare the exchange and queue, and create a binding between them
    await channel.exchangeDeclare('emails', 'direct')
    const queue: AMQPQueue = await channel.queue('email.notifications')
    await channel.queueBind('email.notifications', 'emails', 'notification')

    // Publish a message to the exchange
    const sendToQueue = async (routingKey: string, email: string, name: string, body: string): Promise<void> => {
      const message: { email: string, name: string, body: string } = { email, name, body }
      const jsonMessage: string = JSON.stringify(message);
      await queue.publish(jsonMessage, { contentType: 'application/json', contentEncoding: 'utf-8', headers: { routingKey } })
      console.log("[📥] Message sent to queue", message)
    };

    // Send some messages to the queue
    await sendToQueue("notification", "example@example.com", "John Doe", "Your order has been received");
    await sendToQueue("notification", "example@example.com", "Jane Doe", "The product is back in stock");
    await sendToQueue("resetpassword", "example@example.com", "Willem Dafoe", "Here is your new password");


   setTimeout(() => {
      // Close the connection
      connection.close()
      console.log("[❎] Connection closed")
      process.exit(0)
    }, 500);
  } catch (error) {
    console.error(error)

    // Retry after 3 second
    setTimeout(() => {
      startPublisher()
    }, 3000)
  }
}

// Last but not least, we have to start the publisher and catch any errors
(async (): Promise<void> => {
    await startPublisher();
})()
import { AMQPClient, AMQPChannel, AMQPQueue, AMQPMessage } from '@cloudamqp/amqp-client'

async function startConsumer(): Promise<void> {
  // Set up a connection to the RabbitMQ server
  const cloudAMQPURL: string = 'amqp://guest:guest@localhost:5672/' // Replace if needed
  const connection: AMQPClient = new AMQPClient(cloudAMQPURL)
  await connection.connect()
  const channel: AMQPChannel = await connection.channel()

  console.log("[✅] Connection over channel established")

  const queue: AMQPQueue = await channel.queue('email.notifications')

  let counter: number = 0;

  await queue.subscribe({noAck: false}, async (msg: AMQPMessage): Promise<void> => {
    try {
      console.log(`[📤] Message received (${++counter})`, msg.bodyToString())
      await msg.ack()
    } catch (error) {
      console.error(error)
    }
  })

  // When the process is terminated, close the connection
  process.on('SIGINT', () => {
    channel.close()
    connection.close()
    console.log("[❎] Connection closed")
    process.exit(0)
  });
}

startConsumer().catch(console.error);
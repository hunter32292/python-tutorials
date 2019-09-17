import pika

class Receiver(object):

    # Create basic Configuration of the class and its config
    def initializer(self, settings=None):
        self.settings = settings

    # Create an initial rabbit queue config
    def rabbit_queue(self, queue_name):
        print("Starting Config Rabbit ...")
        # Setup Basic connection to Rabbit host
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="localhost",
            port=5672,
            virtual_host='/',
            credentials=pika.PlainCredentials("guest", "guest"),
        ))
        self.channel = connection.channel()

    def read_from_queue(self, func, queue_name):
        print("Reading From '%s'..." % queue_name)
        # print("Callback: %s" % func)
        # print("Channel: %s" % self.channel)
        # Subscribe to Queue
        # If there is a message, run func with message payload
        try:
            self.channel.queue_declare(queue=queue_name, durable=True)
            self.channel.basic_consume(func,queue_name)
            self.channel.start_consuming()
        except Exception as e:
            print("Failed to consume: %s" % e)
            
        

    def ack_message(self, method_frame):
        self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        print("Message Ack'd")
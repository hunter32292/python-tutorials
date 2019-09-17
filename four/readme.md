# Working with Python Workers and RabbitMQ

Create a new directory or workspace called: **exercise-four**

`mkdir exercise-four`

### Requirements

Pip install:
- pika

#### Do this at the start:
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install -MODULE NAME-`

### Creating a simple python worker, to run against messages (event)
The worker will be broken up into three files:
1. The Receiver - Which should connect, validate, and accept event
2. The Working Logic - Which should run against the accepted event and do the main work against the message
3. The Producer - Which should connect, validate, and submit another event
```
X X         XX X X X X     X X    
X   X        X       X     X   X  
X     X       X      X     X     X
X   X        X       X     X   X  
X X         XX X X X X     X X    
Receiver - WorkingLogic - Producer
```
# 1. Create a Simple Receiver object, to accept message from RabbitMQ
Create a Receiver object, to process messages as a client to some sort of event bus (RabbitMQ)

1. `touch receiver.py` will create the file we need
2. Fill out the information below:

```
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
            host="0.0.0.0",
            port=5671,
            virtual_host='/',
            credentials=pika.PlainCredentials("guest", "guest"),
        ))
        self.channel = connection.channel()

    def read_from_queue(self, func, queue_name):
        print("Reading From '%s'..." % queue_name)
        # Subscribe to Queue
        # If there is a message, run func with message payload
        try:
            self.channel.queue_declare(queue=queue_name, durable=True)
            self.channel.basic_consume(func,queue_name)
            # Start consuming from the queue
            self.channel.start_consuming()
        except Exception as e:
            print("Failed to consume: %s" % e)
            
        

    def ack_message(self, method_frame):
        self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        print("Message Ack'd")
```

# 2. Create a WorkerLogic object, that will run against the Event from the Receiver
Create a Main file (working_logic), to handle the messages from Receiver and the output to Producer.

1. `touch working_logic.py` will create the file we need
2. Fill out the information below:

```
from receiver import Receiver
from producer import Producer
import json

rec = Receiver()

def working_logic(channel, method_frame, header_frame, body):
    # Pull maintenance_window_name out of queue payload
    print("Received from queue: %s" % body.decode('utf-8'))
    payload = json.loads(body.decode('utf-8'))
    message = payload.pop('message', [])
    prod = Producer()
    prod.create_message(message)
    print("Produced response and Ack'ing")
    rec.ack_message(method_frame)

if __name__ == "__main__":
    rec.rabbit_queue("receiver_queue")
    rec.read_from_queue(working_logic,"receiver_queue")
```

# 3. Create a Producer object, that will submit another event after the WorkingLogic is done
Create a Producer, to handle the events we're going to pass on during out workflow.
> This will be a very simple, `print()` worker although we can make a more complex worker in the future

1. `touch producer.py` will create the file we need
2. Fill out the information below:

```
class Producer(object):

    # Create basic Configuration of the class and its config
    def initializer(self, settings=None):
        self.settings = settings

    def create_message(self, message):
        print("Here is the message: %s" % message)

```

# 4. Using Docker, start a RabbitMQ Server and connect to it with your worker, then test out a simple message in the Queue
To test our new worker locally we will create a Docker container with RabbitMQ on our local machine

```
docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 8080:15672 rabbitmq:3-management

This will create a UI at: http://0.0.0.0:8080/#/
Login
username: guest
password: guest

Run your worker:
python3 working_logic.py

Then create a message in http://0.0.0.0:8080/#/queues/%2F/receiver_queue
{ "message" : "Hello!" }
 
```
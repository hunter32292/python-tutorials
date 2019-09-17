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
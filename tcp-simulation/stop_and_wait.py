# simple stop-and-wait simulation

import random

def send_packet(packet_id):
    print(f"sending packet {packet_id}")
    
    # simulate loss
    if random.random() < 0.3:
        print("packet lost")
        return False
    
    print("ack received")
    return True

for i in range(5):
    success = False
    while not success:
        success = send_packet(i)

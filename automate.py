import time

def send_message(msg):
    print(f"Sending message: {msg}")
    time.sleep(2)
    print("Message sent!")

while True:
    msg = input("Enter a message: ")
    send_message(msg)

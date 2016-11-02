#!/usr/bin/python3
import os

def create_fifo():
    try:
        os.mkfifo( "this.pipe")
    except:
        pass
    
def write_messages_from_b():
    while True:
        message = input("write a message: ")
        with open("this.pipe","w") as thispipe:
          thispipe.write(message + " : this comes from b")

if __name__ == "__main__":
    create_fifo()
    write_messages_from_b()
#!/usr/bin/python3
import os

def create_fifo():
    try:
        os.mkfifo( "this.pipe")
    except:
        pass
def read_messages():
    while True:
        with open("this.pipe","r") as thispipe:
            message = thispipe.read()
            if message != "":
                print(message)
            else:
                time.sleep(.3)

if __name__ == "__main__":
    create_fifo()
    read_messages()
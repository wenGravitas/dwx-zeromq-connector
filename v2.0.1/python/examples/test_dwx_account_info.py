# -*- coding: utf-8 -*-
"""
    test_dwx_account_info.py
    --
    @author: Your Name
    
    This script tests the account information retrieval from the DWX ZeroMQ MT4 EA.
"""

import zmq
import time

class DWXTestClient:
    def __init__(self, host='localhost', push_port=32768, pull_port=32769):
        self.context = zmq.Context()
        self.push_socket = self.context.socket(zmq.PUSH)
        self.pull_socket = self.context.socket(zmq.PULL)

        self.push_socket.connect(f'tcp://{host}:{push_port}')
        self.pull_socket.connect(f'tcp://{host}:{pull_port}')

    def send_command(self, command):
        self.push_socket.send_string(command)

    def receive_response(self):
        return self.pull_socket.recv_string()

    def test_account_info(self):
        print("Requesting account information...")
        self.send_command("GET_ACCOUNT_INFO")
        time.sleep(1)  # Wait for the response
        response = self.receive_response()
        print("Received response:", response)

    def close(self):
        self.push_socket.close()
        self.pull_socket.close()
        self.context.term()

if __name__ == "__main__":
    client = DWXTestClient()
    try:
        client.test_account_info()
    finally:
        client.close()

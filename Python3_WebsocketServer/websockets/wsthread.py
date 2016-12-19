# -*- coding: utf-8 -*-

import threading
from websockets.websocket import Websocket


class WebsocketThread(threading.Thread):

    connected = True
    client = 0
    channel = 0
    details = 0
    server = 0
    websocket = Websocket()

    def __init__(self, channel, details, client, server):
        super(WebsocketThread, self).__init__()
        self.channel = channel
        self.details = details
        self.client = client
        self.server = server

    def run(self):
        self.connected = True

        msg = "Server: Device #{0} connected at {1}"
        print((msg.format(self.client.clientid, self.details[0])))

        self.websocket.do_handshake(self.channel)

        while self.connected:
            self.interact(self.channel)

    def stop(self):
        self.connected = False
        self.channel.close()

    def interact(self, channel):
        encodeddata = channel.recv(8192)
        data = self.websocket.decode_data(encodeddata)
        channel.send(bytes(encodeddata)) 
        if data[2] == 8:
            msg = "Client #{0} closed connecting, bye!"
            print((msg.format(self.client.clientid)))
            self.channel.close()
            self.connected = False
        else:
            msg = "Received data from client #{0} saying: {1}"
            print((msg.format(self.client.clientid, data[0])))

            if data[0] == "hallo":
                response = self.websocket.encode_data(True, "hey browser")
                channel.send(response)
                
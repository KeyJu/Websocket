# -*- coding: utf-8 -*-
import time


class Wsclient:

    clientid = 0
    socket = 0
    lastTimeSeen = time.time()

    def __init__(self, socket, clientid):
        self.clientid = clientid
        self.socket = socket

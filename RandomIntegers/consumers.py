import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

# this websocket block the application for 100 sec
class RandomIntConsumer(WebsocketConsumer):
    def connect(self):
        print(type(self))
        print('channel_name',self.channel_name)
        print('channel_layer',self.channel_layer)
        print('channel_layer_alias',self.channel_layer_alias)
        print('channel_receive',self.channel_receive)
        print('groups',self.groups)
        print('base_send',self.base_send)

        self.accept()

        for i in range(100):
            self.send(json.dumps({'message':i}))
            sleep(1)


import channels.layers


channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync
async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
async_to_sync(channel_layer.receive)('test_channel')


aa={'groups': [], 'scope': {'type': 'websocket', 'path': '/ws/chat/pushpakl/', 'raw_path': '/ws/chat/pushpakl/', 'headers': [('host', '127.0.0.1: 8000'), ('user-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 85.0) Gecko/20100101 Firefox/85.0'), ('accept', '*/*'), ('accept-language', 'en-US,en;q=0.5'), ('accept-encoding', 'gzip, deflate'), ('sec-websocket-version', '13'), ('origin', 'http://127.0.0.1:8000'), ('sec-websocket-extensions', 'permessage-deflate'), ('sec-websocket-key', 'pVPsapEmXlGQrH1u+gdPjg=='), ('dnt', '1'), ('connection', 'keep-alive, Upgrade'), ('cookie', 'csrftoken=gFtyU1Cw3uVtSZI33srLscNqZouLQedegwrtpsHuEhVpMQu5aBD0XlTl5zzwZhXE'), ('pragma', 'no-cache'), ('cache-control', 'no-cache'), ('upgrade', 'websocket')], 'query_string': '', 'client': ['127.0.0.1', 60298], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'cookies': {'csrftoken': 'gFtyU1Cw3uVtSZI33srLscNqZouLQedegwrtpsHuEhVpMQu5aBD0XlTl5zzwZhXE'}, 'session': '<django.utils.functional.LazyObject object at 0x7f25a3e39670>', 'user': '<channels.auth.UserLazyObject object at 0x7f25a3d4d7c0>', 'path_remaining': '', 'url_route': {'args': (), 'kwargs': {'room_name': 'pushpakl'}}}, 'channel_layer': '<channels_redis.core.RedisChannelLayer object at 0x7f25a3d4d670>', 'channel_name': 'specific.274adb85ba144f5a84be5aa275afb397!0681e89de25a4579bc3dd1895c62f4fb', 'channel_receive': 'functools.partial(<bound method RedisChannelLayer.receive of <channels_redis.core.RedisChannelLayer object at 0x7f25a3d4d670>>, specific.274adb85ba144f5a84be5aa275afb397!0681e89de25a4579bc3dd1895c62f4fb)', 'base_send': '<asgiref.sync.AsyncToSync object at 0x7f25a34ef340>'}





from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
from asgiref.sync import async_to_sync

async_to_sync(channel_layer.send)("specific.b654b330e25f489daf54f135722a59eb!5b5a38293090486bba0e656ec3e69c69", {
    "type": "chat.message",
    "message": "Hello there!",
})
# this is also works 
############################# DON'T KNOW WHY ?
async_to_sync(channel_layer.send)("specific.3b8fa0c4d0bf46038d63881ce8c1be47!99cc35db9dbe4224a61cea24587bb2e8", {
    "type": "chat_message",
    "message": "Hello there!",
})

async_to_sync(channel_layer.group_send)('chat_pushpak1',{
    "type": "chat.message",
    "message": "Hello there!",
})
# this is also works 
############################# DON'T KNOW WHY ?
async_to_sync(channel_layer.group_send)('chat_pushpak1',{
    "type": "chat_message",
    "message": "Hello there!",
})

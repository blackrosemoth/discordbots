#!/usr/bin/env python3

"""Baby's First Discord Bot"""
#201345024 - Permissions Integer

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        #print(self)
    async def on_message(self, message):
        print(f'Message from {message.author} in {message.guild} and {message.channel}: "{message.content}"')
      #  print(message)
    async def on_raw_message_edit(self, payload):
        new = payload.data
        old = payload.cached_message.content
        user = new.get("author").get("username")
        msg = new.get("content")
        print(f'User {user} edited message "{old}" to "{msg}"')
client = MyClient()

client.run('OTY4NjQzMzM1NjYzMjU1NjQy.Ymh1Zw.J9rz8kek7UFmv1czJSp92yo0fQc')
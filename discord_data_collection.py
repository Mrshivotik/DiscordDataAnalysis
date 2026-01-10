import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}!')

    async def on_message(self, message):
        if message.author != self.user:
            return
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'scan':
            async for msg in message.channel.history(limit=100000000, oldest_first = True):
                timelist.append(msg.created_at.strftime('%Y-%b-%d'))
                print(msg.created_at.strftime('%Y-%b-%d'))
        if message.content == 'clear list':
            timelist.clear()
        if message.content == 'show list':
            print(timelist)
        if message.content == 'save list':
            file = open(r'D:\pythonproject\data\data.txt', 'w') # Any directory goes here to save your data
            file.write(str(timelist))
            file.close()
        if message.content == 'save list as string':
            with open(r'D:\pythonproject\data\data.txt', 'w')as f: # Any directory goes here to save your data
                for t in timelist:
                    f.write(f'{t}\n')


timelist = []


client = MyClient()
client.run('Token')
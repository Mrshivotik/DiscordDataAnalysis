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
            async for msg in message.channel.history(limit=100, oldest_first = True):
                datalist.append(f'{msg.created_at.strftime('%Y-%b-%d')} {msg.author.name}')
                print(f'{msg.created_at.strftime('%Y-%b-%d')} {msg.author.id}')

        if message.content == 'clear list':
            datalist.clear()

        if message.content == 'show list':
            print(datalist)

        if message.content == 'save list':
            file = open(r'D:\pythonproject\data\data.txt', 'w') # Any directory goes here to save your data
            file.write(str(datalist))
            file.close()

        if message.content == 'save list as string':
            with open(r'D:\pythonproject\data\data.txt', 'w')as f: # Any directory goes here to save your data
                for data in datalist:
                    f.write(f'{data}\n')



datalist = []


client = MyClient()
client.run('Token')
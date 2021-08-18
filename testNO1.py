import discord
import asyncio

client = discord.Client()

token = "NzY2Mjg1OTI4NTA2OTgyNDYw.X4hJYg.01R6HACSeQZdzdFF9QtiBuefSB8"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('봇이 활동중에 표시될 이름')
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(token)
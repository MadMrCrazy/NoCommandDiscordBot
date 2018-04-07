import discord
import logging
crae = discord.Client()
token = input("Bot Token :")
hiddenChannel = discord.Object(id="432132167792066560")
async def GamePresence():
    await crae.wait_until_ready()
    await crae.change_presence(game=discord.Game(name='With Shadows'))

@crae.event
async def on_ready():
    TheMessage = "blank"
    while TheMessage != "exit":
        TheMessage = input()
        await crae.send_message(hiddenChannel, TheMessage)

crae.loop.create_task(GamePresence())
crae.run(token)
    

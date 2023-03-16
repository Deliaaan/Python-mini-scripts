import discord
import asyncio

# Coloca el token de tu bot de Discord aquí
token = 'MTA4NTc3NzQ2MjYwNjE4MDQzMg.Gsuj8V.hv-KD5pxG2FQpnbmTw7fk_wRmKa2kTbnbYJsLw'
server_id = '744338116332093523'

# Coloca el ID del canal de origen aquí
canal_origen_id = 831991368867512431

# Coloca el ID del canal de destino aquí
canal_destino_id = 1085790776283385906


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('El bot está listo y conectado al servidor de Discord!')

    # Obtener los canales del servidor
    server = client.get_guild(server_id)


@client.event
async def on_message(message):
    if message.channel.id == canal_origen_id:
        canal_destino = client.get_channel(canal_destino_id)
        await canal_destino.send(f'{message.author}: {message.content}')
        if message.attachments:
            for attachment in message.attachments:
                await canal_destino.send(attachment.url)

# Inicia el bot y lo conecta al servidor de Discord
client.run(token)
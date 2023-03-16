import discord
import asyncio

# Coloca el token de tu bot de Discord aquí
token = 'AQUI_PEGA_EL_TOKEN_DE_TU_BOT_DE_DISCORD'

# Coloca el ID del canal de origen aquí
canal_origen_id = 1234567890

# Coloca el ID del canal de destino aquí
canal_destino_id = 0987654321

client = discord.Client()

@client.event
async def on_ready():
    print('El bot está listo y conectado al servidor de Discord!')

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
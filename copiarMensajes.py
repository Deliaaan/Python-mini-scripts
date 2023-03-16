import discord

# Autenticarse con la API de Discord
client = discord.Client()
token = 'aqui va el token del bot'
server_id = 'id del server'

# Conectar al servidor
@client.event
async def on_ready():
    print('Conectado al servidor')

    # Obtener los canales del servidor
    server = client.get_guild(server_id)
    channel_origen = server.get_channel('id_del_canal_origen')
    channel_destino = server.get_channel('id_del_canal_destino')

    # Obtener los mensajes del canal de origen
    messages = await channel_origen.history(limit=None).flatten()

    # Crear un nuevo canal si aún no existe
    if channel_destino is None:
        channel_destino = await server.create_text_channel('nombre_del_nuevo_canal')

    # Enviar los mensajes al nuevo canal
    for message in messages:
        await channel_destino.send(message.content)

# Iniciar el cliente de Discord
client.run(token)

import discord
from discord.ext import commands
import discum
import requests
import json


canales =canales = {
 '1191855182959628359':'https://discord.com/api/webhooks/1191856297226801223/zLqo9gAq7GK8dNZgLaIC5WFA6jstGeDF7SQyw1vugDpmfJtwPmSfF2buiVdQF4cbPxYJ'
}


TOKEN = 'NDgxNjAyNjAzODU2NDI5MDc2.GjjWA-.eKKrOwkDHt7cZxAzr9Xd4Z1FpQkHQPcDlIFX8Q'

bot = discum.Client(token=TOKEN)
                                                                                                                                           
@bot.gateway.command
def on_message(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        channel_id = message['channel_id']

        if channel_id in canales:

                WH = canales[channel_id]
                
                if '38143' in message:
                    requests.post(WH, headers={'Content-Type': 'application/json'}, json={"content": "@here"})    
                



bot.gateway.run(auto_reconnect=True)


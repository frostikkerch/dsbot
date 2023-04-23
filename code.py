import discord
import requests

client = discord.Client()

# Установка заголовка авторизации с использованием предоставленного API ключа
headers = {'Authorization': 'Bearer ' + https://api.warframe.market/v1}


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/wtb'):
        item_name = message.content.split(' ')[1]
        url = f'https://api.warframe.market/v1/items/{item_name}/orders?include=item&platform=pc&status=ingame&time_filter=hour'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            orders = data['payload']['orders']
            orders.sort(key=lambda order: order['platinum'])
            orders = orders[:7]

            response_text = f"Top 7 {item_name} WTB listings on Warframe Market:\n"
            for order in orders:
                response_text += f"{order['platinum']}p | {order['quantity']} available | {order['user']['ingame_name']} ({order['user']['status']})\n"
            await message.channel.send(response_text)

        else:
            await message.channel.send(f"Error {response.status_code} occurred while processing your request.")


client.run(8148caae55f25a1156523831dbe3933e6059e694765b3f3b07f9d0ff156334bf)
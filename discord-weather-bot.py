import requests, json
import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents = intents)

def get_weather(city):
    try:
        base_url = "https://api.weatherapi.com/v1/current.json?key=9b025c4d727e4376907105502231612"
        complete_url = base_url + "&q=" + city
        response =  requests.get(complete_url) 
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        wicon_url = 'https:' + result['current']['condition']['icon']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed = discord.Embed(title=f"Hi, there! \n This is {city}'s Weather today", description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name="Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.set_thumbnail(url=wicon_url)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed

@client.event
async def on_message(message):
    if message.content.lower().startswith("!weather"):
            city = message.content[slice(9, len(message.content))].lower()
            result = get_weather(city)
            await message.channel.send(embed=result)

print("Bot is has started running")
client.run('MTE4NTUxMTMwMzU1NzY5NzU4Ng.GrF6em.Q6innyjE-WdYd0BTYDyP9lcaOunHYbj4KAE8ko')
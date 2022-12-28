import discord
import os
from discord.ext import commands
import requests



client = commands.Bot(command_prefix= '.')



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="over Agent47's Ninja World"))
  print(f'Bot connected as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
        return
  if message.content.startswith('hi'):
    await message.channel.send('hi there :)')
    await client.process_commands(message)
    return




  incoming_msg = message.content
  # Set the API endpoint URL and the request body
  url = "https://api.openai.com/v1/completions"
  data = {
    "model": "text-davinci-002",
    "prompt": incoming_msg,
    "max_tokens": 4000,
    "temperature": 0
  }
  
  # Set the API key as a header
  openai_token = os.environ['openai_token']
  headers = {"Authorization": openai_token}
  
  # Make the POST request
  response = requests.post(url, json=data, headers=headers)
  
  # Check the status code to see if the request was successful
  if response.status_code == 200:
      # Print the response data
      msgs = response.json()
      await message.channel.send(msgs['choices'][0]['text'])
  else:
      # Print the error message
      print(f"Request failed with status code {response.status_code}: {response.text}")


  
  
  await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')



@client.command(pass_context = True)
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not connected")
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.event
async def on_voice_state_update(member, before, after,):
    
    ch = client.get_channel(1057151243564231500)
    if before.channel is None and after.channel is not None:
      channel_name = after.channel.name
      await ch.send(f'{member.mention} has joined to {str(channel_name)}')
      

    if before.channel is not None and after.channel is None:
      channel_name = before.channel.name
      await ch.send(f'{member.mention} has left from {str(channel_name)}')









    
@client.command()
async def socials(ctx):
    embed1=discord.Embed(title="click here", url="https://www.youtube.com/Agent47_live", color=0xff0000)
    embed1.set_author(name="YouTube", url="https://www.youtube.com/Agent47_live")
    embed1.set_thumbnail(url="https://www.iconpacks.net/icons/2/free-youtube-logo-icon-2431-thumb.png")
    #embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed1)

    embed2=discord.Embed(title="click here", url="https://www.facebook.com/notagent47", color=0x3b5998)
    embed2.set_author(name="Facebook", url="https://www.facebook.com/notagent47")
    embed2.set_thumbnail(url="https://1000logos.net/wp-content/uploads/2021/04/Facebook-logo.png")
    #embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed2)

    embed3=discord.Embed(title="click here", url="https://www.instagram.com/ahmedberuny/?hl=en", color=0x8a3ab9)
    embed3.set_author(name="Instagram", url="https://www.instagram.com/ahmedberuny/?hl=en")
    embed3.set_thumbnail(url="https://i.pinimg.com/originals/c6/73/fd/c673fd5bf25ebe8904c45bd90145d71f.png")
    #embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed3)

    embed4=discord.Embed(title="click here", url="https://twitter.com/AhmedBeruny", color=0x00aced)
    embed4.set_author(name="Twitter", url="https://twitter.com/AhmedBeruny")
    embed4.set_thumbnail(url="https://assets.stickpng.com/images/580b57fcd9996e24bc43c53e.png")
    #embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed4)

    embed5=discord.Embed(title="click here", url="https://www.twitch.tv/agent47_live", color=0x6441a5)
    embed5.set_author(name="Twitch", url="https://www.twitch.tv/agent47_live")
    embed5.set_thumbnail(url="http://pngimg.com/uploads/twitch/twitch_PNG13.png")
    #embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed5)





my_secret = os.environ['token']

client.run(my_secret)

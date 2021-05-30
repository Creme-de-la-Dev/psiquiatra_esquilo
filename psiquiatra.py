import discord as dc
import os
import asyncio

bot_token = os.environ['token']

client = dc.Client()

vitima_id = 364826611041697822 # id do esquilo (davis)
psico_id = 325407029382348801 # id do ale

class Psiquiatra():
    def __init__(self):
      self.juntos = False

    async def comecar_sessao(self):
      print('comecar_sessao')
      self.juntos = True
      await start_paciencia()

    def kill(self):
      print('psiquiatra morreu :c')
      self.juntos = False

psiquiatra = Psiquiatra() # criar o psiquiatra

async def start_paciencia():
  paciencia = 0
  print('comecou a contar')
  while psiquiatra.juntos:
      paciencia += 1
      print ("Paciencia do Esquilo:")
      print(paciencia)
      await asyncio.sleep(2) # sleep(300)

print('Psiquiatra foi criado')
print(psiquiatra)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.content.startswith('gay'):
    await message.channel.send("Ih ala")

async def checar_ale(channel):
  if channel == None:
    print('nao temos ale...')
    psiquiatra.kill()

async def start_psiquiatra(member, after):
  print('start_psiquiatra')
  if any(m.id == vitima_id for m in after.channel.members):
    await psiquiatra.comecar_sessao()

@client.event
async def on_voice_state_update(member, before, after):
  if member.id == psico_id:
    print('alhe fez algo...')
    if after.channel != None:
      await start_psiquiatra(member, after)
    await checar_ale(after.channel)

client.run(bot_token)

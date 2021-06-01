import discord as dc
import os
import asyncio
import youtube_dl

bot_token = os.environ['token']

client = dc.Client()

# Youtube Setup

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(dc.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

#codigo copiado acima https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1#

vitima_id = 364826611041697822 # id do esquilo (davis)
psico_id = 325407029382348801 # id do ale

#text_channel = client.get_channel(847958499165601846)

class Psiquiatra():
    def __init__(self):
      self.juntos = False
      self.voice_channel = None
      self.text_channel = None

    async def comecar_sessao(self):
      print('comecar_sessao')
      self.juntos = True
      await start_paciencia()

    def kill(self):
      print('psiquiatra morreu :c')
      self.juntos = False

psiquiatra = Psiquiatra() # criar o psiquiatra

def print_medidor_de_paciencia(odio):
  mini_odio = int(odio / 5)
  porcentagem = mini_odio * "#"
  faltam = 20 - len(porcentagem)
  string = "Calculando agonia de esquilo... \n" + str(odio) +  '% [' +  (mini_odio * "#") +  (faltam * "=") + "]"
  
  return string

async def start_paciencia():
  agonia_do_esquilo = 0
  print('comecou a contar')
  while psiquiatra.juntos:
      agonia_do_esquilo += 1
      if agonia_do_esquilo <= 100 and agonia_do_esquilo % 5 == 0:
        await psiquiatra.text_channel.send(print_medidor_de_paciencia(agonia_do_esquilo))
        if agonia_do_esquilo % 25 == 0:
          await play_susto_grito()
      await asyncio.sleep(1) # sleep(110)

print('Psiquiatra foi criado')
print(psiquiatra)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.content.startswith('gay'):
    await message.channel.send("Ih ala")
  if message.content.startswith('joyce'):
    psiquiatra.text_channel = message.channel

async def checar_ale(channel):
  if channel == None:
    print('nao temos ale...')
    psiquiatra.kill()

async def start_psiquiatra(member, after):
  print('start_psiquiatra')
  # if any(m.id == vitima_id for m in after.channel.members):
  psiquiatra.voice_channel = after.channel
  await psiquiatra.comecar_sessao()

@client.event
async def on_voice_state_update(member, before, after):
  if member.id == psico_id:
    print('alhe fez algo...')
    if after.channel != None:
      await start_psiquiatra(member, after)
    await checar_ale(after.channel)

async def play_susto_grito():
  filename = await YTDLSource.from_url('https://www.youtube.com/watch?v=HEW9E0R1yn8&ab_channel=tiagobmarinho')
  psiquiatra.voice_channel.play(dc.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))

  
client.run(bot_token)


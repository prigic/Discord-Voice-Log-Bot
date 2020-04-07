import asyncio
import discord


# - Config -
CHANNEL_NAME = "voice-notice"
BOT_TOKEN = "NDYyNDk3OTU0ODg5MjAzNzIy.DhoUJw.te7BlAYVD4pLVx1wVJTZLuIuzig"
#-----------

client = discord.Client()
server_ch = {}

def find_channel(server, refresh = False):
    if not refresh and server in server_ch:
        return server_ch[server]
    for channel in client.get_all_channels():
        if channel.server == server and channel.name == CHANNEL_NAME:
            server_ch[server] = channel
            return channel
    return None

@client.event
async def on_voice_state_update(member_before, member_after):
    server = member_after.server
    channel = find_channel(server)
    
    voice_channel_before = member_before.voice_channel
    voice_channel_after = member_after.voice_channel
    
    if voice_channel_before == voice_channel_after:
        return
    
    if voice_channel_before == None:
        msg = "%s 님이 보이스 채팅방 `%s` 에 연결하셨습니다" % (member_after.mention, voice_channel_after.name)
    else:
        if voice_channel_after == None:
            msg = "%s 님이 보이스 채팅방 `%s` 를 떠났습니다" % (member_after.mention, voice_channel_before.name)
        else:
            msg = "%s 님이 보이스 채팅방 `%s` 에서  `%s` 으로 이동하셨습니다" % (member_after.mention, voice_channel_before.name, voice_channel_after.name)
    try:
        await client.send_message(channel, msg)
    except:
        channel = find_channel(server, refresh = True)
        if channel == None:
            print("에러: 로그를 기록 할 텍스트 채팅방 #%s 가 서버 %s에 없습니다" % (CHANNEL_NAME, server))
        else:
            try:
                await client.send_message(channel, msg)
            except discord.DiscordException as exception:
                print("에러: 서버 %s에서 로그를 기록 할 텍스트 채팅방 #%s에 예외가 발생하였습니다. 예외: %s" % (server, CHANNEL_NAME, exception))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOT_TOKEN)

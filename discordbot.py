from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import gacha
import stew
import member
import fishing

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!', reference=message)

    #가챠
    if message.content.startswith(f'{PREFIX}가챠'):
        gacha_result = gacha.getGacha()
        gacha_message = '뾰로롱...! <'+gacha_result+'>이(가) 나왔다!'
        await message.channel.send(gacha_message, reference=message)

    #다이스(1d100)
    if message.content.startswith(f'{PREFIX}다이스'):
        d = random.randrange(1,101)
        embed = discord.Embed(description=":game_die:도르르륵... 챠킹!",
                            color=0x000000)
        embed.add_field(name=d, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #스튜
    if message.content.startswith(f'{PREFIX}스튜'):
        stew_result = stew.getStew()
        embed = discord.Embed(title="맛있는 만년 스튜!", 
                              description="어떤 맛일까? 한 그릇 떠 담으면, 이것은...", 
                              color=0xe34f4f)
        embed.add_field(name=":stew:"+stew_result, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #랜덤멤버
    if message.content.startswith(f'{PREFIX}랜덤'):
        member_result = member.selectmember()
        embed = discord.Embed(title="랜덤 멤버",
                              description=member_result,
                              color=discord.Color.orange())
        await message.channel.send(embed=embed, reference=message)

    #낚시
    if message.content.startswith(f'{PREFIX}낚시'):
        fish_result = fishing.getFish()
        fsize = fishing.sizing()
        text1 =''
        text2 =''

        if fish_result == '실패':
            text1 = '이런!'
            text2 = '물고기가 도망갔다. 아무것도 낚지 못했다...'

        elif fish_result == '직박구리 씨':
            text1 = '바닷속을 점검하던 직박구리 씨?!'
            text2 = '\"삐이이익!!!! 파티서펀트!!!!! 이것은 공무집행방해입니다!!!!\" 직박구리 씨는 호통을 치고 날아갔다...'

        elif fish_result == '쓰레기' or fish_result =='돌멩이' or fish_result =='1아티' or fish_result =='유리병':
            text1 = fish_result+'을(를) 낚았다!'
            text2 = '물고기가 아니잖아!'
        
        elif fish_result == '고래상어' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
            fsize = fsize + 100

            text1 = fish_result+'을(를) 낚았다!'
            text2 = '성과 기록: 무려 '+str(fsize)+'cm?!'
    
        else:
            text1 = fish_result+'을(를) 낚았다!'
            text2 = '성과 기록: '+str(fsize)+'cm'

        embed = discord.Embed(title = '즐거운 낚시 시간!',
                              description = '낚싯대를 잡아당기면...',
                              color = discord.Color.blue)
        embed.add_field(name = text1, value = text2, inline=False)

        await message.channel.send(embed=embed, reference=message)



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
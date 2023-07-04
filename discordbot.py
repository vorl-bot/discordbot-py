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
import fishingresult
import shoot
import alcohol

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
        
        fish = fishingresult.fishresult()

        text1 = fish[0]
        text2 = fish[1]        

        embed = discord.Embed(title = '즐거운 낚시 시간!',
                              description = '낚싯대를 잡아당기면...',
                              color = discord.Color.blue())
        embed.add_field(name = text1, value = text2, inline=False)

        await message.channel.send(embed=embed, reference=message)

    #복권
    if message.content.startswith(f'{PREFIX}복권'):
        lotto = []
        ltext = ''
        while len(lotto) < 3:
            number = str(random.randrange(1,10))
            newnum = list(number)
            lotto = lotto+newnum
            ltext = ltext+number

        embed=discord.Embed(title=':dollar:'+'일일복권', 
                            description="결과: "+ltext, 
                            color=0x89fb9c)
                
        await message.channel.send(embed=embed, reference=message)

    #사격
    if message.content.startswith(f'{PREFIX}사격'):

        shooting = shoot.shootingresult()

        st1 = shooting[0]
        st2 = shooting[1]

        embed = discord.Embed(title = '사격 결과',
                              description = '',
                              color = discord.Color.dark_magenta())
        embed.add_field(name = st1, value = st2, inline=False)

        await message.channel.send(embed=embed, reference=message)

    #술
    if message.content.startswith(f'{PREFIX}주류'):
        alcohol_result = alcohol.bar()
        embed = discord.Embed(title="바텐더의 추천 메뉴!", 
                              description="바텐더는 당신의 앞에 잔을 하나 내려놓았다...", 
                              color=discord.Color.gold())
        embed.add_field(name=":cocktail:"+alcohol_result, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
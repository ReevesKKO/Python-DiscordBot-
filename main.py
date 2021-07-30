import discord 
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import os
import datetime
from datetime import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	DiscordComponents(bot)
	print('Готово')


#@bot.command()
#async def тест(ctx, *, arg):
#	await ctx.send(arg)	

@bot.command(pass_context=True)
async def Выбор(ctx, *, message: str):
    channel = bot.get_channel(855430707664650251) #logs
    await channel.send(message)
    
    if "7656" in message:
    	await ctx.message.add_reaction("✅")
    else:
    	await ctx.message.add_reaction("❌")

@bot.command(pass_context=True)
async def TDM(ctx, *, arg = None):
    emb= discord.Embed(
    	title='TeamDeathMatch [ЗАЯВКИ ПРИНИМАЮТСЯ ДО 20:15]',
    	description='ПВП Долг - Свобода.\nПравила оговариваются перед началом игры. \n\nЗаполнять строго по форме в ЛИЧКУ БОТУ: \n\n!Выбор TDM [steam_id64] [Ник] [Ник желаемого товарища(можно пустым)]', 
    	timestamp=datetime.today(),
    	color=0xa84300,
    )

    channel = bot.get_channel(854867255199137833) #news
    msg = await channel.send(embed=emb)


@bot.command(pass_context=True)
async def xsend(ctx, *, message: str):
    channel = bot.get_channel(853428194681946112) #чат #await message.channel.send("<@&id_роли>") 
    if channel:
        await channel.send(message)

@bot.command(pass_context=True)
async def news(ctx, *, arg = None):
    emb= discord.Embed(
    	title='Поддержка проекта.',
    	description='В данный момент собрано на хост: [1078|3500]',
    	timestamp=datetime.now(),
    	color=0xa84300,
    )
    channel= bot.get_channel(854806079014436885) #news
    msg = await channel.send(embed=emb)
    #await msg.add_reaction('👍')
    #await msg.add_reaction('👎')

#@bot.event 
#async def on_message(message):
#	if '#' in message.content:
#		await message.author.send(f'{message.author.mention}, команда для выбора пресета. Подробнее: !Пресет')

@bot.event 
async def on_raw_reaction_add(payload):
	ourMessageID = 854706417239195648

	if ourMessageID == payload.message_id: 
		member = payload.member
		guild = member.guild

		emoji = payload.emoji.name
		if emoji == "✅":
			role = discord.utils.get(guild.roles, name='DM')
		await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
	ourMessageID = 854706417239195648

	guild = await(bot.fetch_guild(payload.guild_id))
	emoji = payload.emoji.name
	if emoji == "✅":
			role = discord.utils.get(guild.roles, name='DM')
	member = await(guild.fetch_member(payload.user_id))
	if member is not None: 
		await member.remove_roles(role)
	else: 
		print("Member not found")

@bot.command(pass_context=True)
async def run(ctx):
	embed = discord.Embed(
		title="Добро пожаловать на STALKER Deathmatch сервер!",
		url="https://discord.gg/BHvnFac3",
		description='Нажимая на реакцию, Вы соглашаетесь с правилами и политикой сервера.',
		timestamp=datetime.now(),
		color=0xa84300,
	)
	msg = await ctx.send(embed=embed)
	await msg.add_reaction('✅')

@bot.command()
async def Пресет(ctx):
	await ctx.send(
		embed=discord.Embed(
		title="Выбор группировки.", 
		description='На выбор даётся 6 основных группировок трилогии STALKER. \nКаждый пресет даёт сигнатурную одежду выбранной группировки. \nКрасная кнопка возвращает рандомный спавн пресета. \n\n **Важно!!! По умолчанию каждый игрок спавнится в рандомной группировке. \nВыбранный пресет обновляется раз в рестарт на сервере.**',
		timestamp=datetime.now(),
		color=0xa84300),

		components=[
			Button(style=ButtonStyle.green, label="Выбор пресета"),
			Button(style=ButtonStyle.red, label="Вернуть рандомный пресет")
		]
	)

	response = await bot.wait_for("button_click")
	if response.channel == ctx.channel:
		if response.component.label == "Выбор пресета":
			await response.respond(embed=discord.Embed(color=0xa84300,title="Доступные пресеты: \nДолг \nСвобода \nМонолит \nНаемники \nВоенные \nБратва \nЗаполнять по форме: \n!Выбор [steam_id64] [nickname] [группировка]"))
		else:
			await response.respond(embed=discord.Embed(color=0xa84300,title="Заполнять по форме: \n!Выбор steam_id64 nickname Рандом"))

bot.run('ODUzOTAyNTM4Mzg1MjYwNTg1.YMcItQ.bHbbE9dhX9OJ4TQ4MuqCkOMOqHs')


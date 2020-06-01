import discord
import json
import requests
import asyncio
from discord.ext import commands

poeBot = commands.Bot(command_prefix = '.')

@poeBot.command()
async def currency(ctx, *, item: str = "all"):
    req = requests.get('https://poe.ninja/api/data/currencyoverview?league=Delirium&type=Currency&language=en')
    data = req.json()
    tracker = 0
    curPage = 1
    maxPage = 0
    tempHold = []
    content = []
    list = ""
    for i in data["lines"]:
        if item.lower() in "chaos orb":
            await ctx.send("Give an actual name or use all")
            break
        elif item.lower() in i["currencyTypeName"].lower() or item.lower() == "all":
            price = i["receive"]["value"]
            if int(price/1000) != 0:
                price = round(price/1000, 1)
                tempHold.append(i["currencyTypeName"] + ': ' + str(price) + 'K <:emoji_name:715777677352632434>')
            else:
                if (str(price).index('.')) == 1:
                    price = round(price, 2)
                    tempHold.append(i["currencyTypeName"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
                else:
                    price = round(price, 1)
                    tempHold.append(i["currencyTypeName"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
    if int(len(tempHold)) == 0:
        return
    maxPage = int(len(tempHold)/4)
    for i in range(0, len(tempHold)-1):
        if tracker == 4:
            content.append(list)
            list = ""
            tracker = 0
        list += tempHold[i] + '\n'
        tracker += 1
    content.append(list)
    message = await ctx.send(f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
    if maxPage == 1:
        await message.add_reaction("❌")
    else:
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")
        await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️","➡️","❌"]

    while True:
        try:
            reaction, user = await poeBot.wait_for("reaction_add", timeout = 15, check = check)

            if str(reaction.emoji) == "➡️" and curPage != maxPage:
                curPage += 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "❌":
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@poeBot.command()
async def fragment(ctx, *, item: str = "all"):
    req = requests.get('https://poe.ninja/api/data/currencyoverview?league=Delirium&type=Fragment&language=en')
    data = req.json()
    tracker = 0
    maxPage = 0
    curPage = 1
    list = ""
    tempHold = []
    content = []
    for i in data["lines"]:
        if item.lower() in i["currencyTypeName"].lower() or item.lower() == "all":
            price = i["receive"]["value"]
            if int(price/1000) != 0:
                price = round(price/1000, 1)
                tempHold.append(i["currencyTypeName"] + ': ' + str(price) + 'K <:emoji_name:715777677352632434>')
            else:
                if (str(price).index('.')) == 1:
                    price = round(price, 2)
                    tempHold.append(i["currencyTypeName"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
                else:
                    price = round(price, 1)
                    tempHold.append(i["currencyTypeName"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
    maxPage = int(len(tempHold)/4)
    for i in range(0, len(tempHold)-1):
        if tracker == 4:
            content.append(list)
            list = ""
            tracker = 0
        list += tempHold[i] + '\n'
        tracker += 1
    content.append(list)
    message = await ctx.send(f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
    if maxPage == 1:
        await message.add_reaction("❌")
    else:
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")
        await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️","➡️","❌"]

    while True:
        try:
            reaction, user = await poeBot.wait_for("reaction_add", timeout = 15, check = check)

            if str(reaction.emoji) == "➡️" and curPage != maxPage:
                curPage += 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "❌":
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@poeBot.command()
async def wstone(ctx, *, item: str = "all"):
    req = requests.get('https://poe.ninja/api/data/itemoverview?league=Delirium&type=Watchstone&language=en')
    data = req.json()
    maxPage = 0
    curPage = 1
    tracker = 0
    tempHold = []
    list = ""
    content = []

    for i in data["lines"]:
        if item.lower() not in i["name"].lower() and item.lower() != "all":
            pass
        elif item.lower() in i["name"].lower() or item.lower() == "all":
            price = round(i["chaosValue"], 1)
            tempHold.append(i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434>' + ' > ' + str(i["mapTier"]) + ' Uses')
    if len(tempHold) == 0:
        return
    maxPage = int(len(tempHold)/4)
    for i in range(0, len(tempHold)-1):
        if tracker == 4:
            content.append(list)
            list = ""
            tracker = 0
        list += tempHold[i] + '\n'
        tracker += 1
    content.append(list)
    message = await ctx.send(f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
    if maxPage == 1:
        await message.add_reaction("❌")
    else:
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")
        await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️","➡️","❌"]

    while True:
        try:
            reaction, user = await poeBot.wait_for("reaction_add", timeout = 15, check = check)

            if str(reaction.emoji) == "➡️" and curPage != maxPage:
                curPage += 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "❌":
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@poeBot.command()
async def oil(ctx, *,item: str = "all"):
    req = requests.get('https://poe.ninja/api/data/itemoverview?league=Delirium&type=Oil&language=en')
    data = req.json()
    curPage = 1
    maxPage = 0
    tracker = 0
    tempHold = []
    content = []
    list = ""
    for i in data["lines"]:
        if item.lower() in i["name"].lower() or item.lower() == "all":
            price = round(i["chaosValue"], 1)
            tempHold.append(i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
    maxPage = int(len(tempHold)/4)
    for i in range(0, len(tempHold)-1):
        if tracker == 4:
            content.append(list)
            list = ""
            tracker = 0
        list += tempHold[i] + '\n'
        tracker += 1
    content.append(list)
    message = await ctx.send(f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
    if maxPage == 1:
        await message.add_reaction("❌")
    else:
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")
        await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️","➡️","❌"]

    while True:
        try:
            reaction, user = await poeBot.wait_for("reaction_add", timeout = 15, check = check)

            if str(reaction.emoji) == "➡️" and curPage != maxPage:
                curPage += 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "❌":
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@poeBot.command()
async def fossil(ctx, *, item: str = "all"):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=Fossil&language=en")
    data = req.json()
    list = ""
    for i in data["lines"]:
        if item.lower() not in i["name"].lower() and item.lower() != "all" or item.lower() in "fossil":
            pass
        elif item.lower() in i["name"].lower() or item.lower() == "all":
            price = round(i["chaosValue"], 1)
            list += i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434> \n'
    if list:
        await ctx.send(list)
    else:
        return

@poeBot.command()
async def resonator(ctx, *, item: str = "all"):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=Resonator&language=en")
    data = req.json()
    list = ""
    for i in data["lines"]:
        if item.lower() in i["name"].lower() or item.lower() == "all":
            price = round(i["chaosValue"], 1)
            list += i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434> \n'
    await ctx.send(list)

@poeBot.command()
async def div(ctx, *, item: str = "all"):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=DivinationCard&language=en")
    data = req.json()
    tracker = 0
    curPage = 1
    maxPage = 0
    list = ""
    tempHold = []
    content = []
    for i in data["lines"]:
        if item.lower() == "all":
            if i["chaosValue"] > 10:
                if int(i["chaosValue"]/1000) != 0:
                    price = round(i["chaosValue"]/1000, 1)
                    tempHold.append(i["name"] + ': ' + str(price) + 'K <:emoji_name:715777677352632434>')
                else:
                    price = round(i["chaosValue"], 1)
                    tempHold.append(i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
        elif item.lower() in i["name"].lower() and len(item) >= 3:
            if int(i["chaosValue"]/1000) != 0:
                price = round(i["chaosValue"]/1000, 1)
                await ctx.send(i["name"] + ': ' + str(price) + 'K <:emoji_name:715777677352632434>')
            else:
                price = round(i["chaosValue"], 1)
                await ctx.send(i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')
    if len(tempHold) == 0:
        return
    maxPage = int(len(tempHold)/4)
    for i in range(0, len(tempHold)-1):
        if tracker == 4:
            content.append(list)
            list = ""
            tracker = 0
        list += tempHold[i] + '\n'
        tracker += 1
    content.append(list)
    message = await ctx.send(f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
    if maxPage == 1:
        await message.add_reaction("❌")
    else:
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")
        await message.add_reaction("❌")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["⬅️","➡️","❌"]

    while True:
        try:
            reaction, user = await poeBot.wait_for("reaction_add", timeout = 15, check = check)

            if str(reaction.emoji) == "➡️" and curPage != maxPage:
                curPage += 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                await message.edit(content=f'[Page {curPage}/{maxPage}]\n{content[curPage-1]}')
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "❌":
                await message.delete()
                break
            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

@poeBot.command()
async def gem(ctx, *, item: str = "", level: int = 1, quality: int = 0, corrupted: bool = False):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=SkillGem&language=en")
    data = req.json()
    for i in data["lines"]:
        if item.lower() in i["name"].lower() and i["gemLevel"] == level and i["gemQuality"] == quality and i["corrupted"] == corrupted:
            price = round(i["chaosValue"], 1)
            await ctx.send(i["name"] + ': ' + str(price) + '<:emoji_name:715777677352632434>')

    #embed = discord.Embed(
    #    colour = discord.Colour.blue()
    #)
    #file = discord.File("./Images/EchoPlus.png")
    #embed.set_author(name="Awakened Gem", icon_url="attachment://EchoPlus.png")
    #embed.set_thumbnail(url="attachment://EchoPlus.png")
    #embed.add_field(name="Gem Level:", value="1")
    #embed.add_field(name="Gem Quality:", value="0%")
    #embed.add_field(name="Corrupted:", value="No")
    #embed.add_field(name="Current Price:", value="X Chaos")
    #await ctx.send(file = file, embed=embed)

@poeBot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount)

poeBot.run('NzE1Njg2NzIwNjA3MjIzODc5.XtQ2uQ.FRDIwaGIyUS_ZBnT3gEM7tum1KU')

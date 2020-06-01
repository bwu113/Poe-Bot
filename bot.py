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
    if item.lower() in "the" or len(item) < 3:   #FIX THIS LOGIC
        return
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
async def gem(ctx, *, item: str = ""):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=SkillGem&language=en")
    data = req.json()
    maxPage = 0
    curPage = 1
    gemList = []
    corrupt = ""
    pic = ""
    if len(item) < 3 or item.lower() in "support":
        return
    for i in data["lines"]:
        if item.lower() in i["name"].lower():
            if i["corrupted"] == True:
                corrupt = "Yes"
            else:
                corrupt = "No"
            if int(i["chaosValue"]/1000) != 0:
                price = round(i["chaosValue"]/1000, 1)
                embed = discord.Embed(
                    colour = discord.Colour.blue()
                )
                embed.set_author(name=i["name"], icon_url=i["icon"])
                embed.set_thumbnail(url=i["icon"])
                embed.add_field(name="Gem Lvl:", value= i["gemLevel"], inline = True)
                embed.add_field(name="Gem %:", value=i["gemQuality"], inline = True)
                embed.add_field(name="Corrupted:", value=corrupt, inline = True)
                if int(i["exaltedValue"]) > 0:
                    embed.add_field(name="Exalted Price:", value=str(round(i["exaltedValue"], 1)) + '<:emoji_name:715777693223878676>')
                    embed.add_field(name="Chaos Price:", value=str(price) + 'K <:emoji_name:715777677352632434>')
                else:
                    embed.add_field(name="Current Price:", value=str(price) + 'K <:emoji_name:715777677352632434>')
                gemList.append(embed)
            else:
                price = round(i["chaosValue"], 1)
                embed = discord.Embed(
                    colour = discord.Colour.blue()
                )
                embed.set_author(name=i["name"], icon_url=i["icon"])
                embed.set_thumbnail(url=i["icon"])
                embed.add_field(name="Gem Lvl:", value= i["gemLevel"], inline = True)
                embed.add_field(name="Gem %:", value=i["gemQuality"], inline = True)
                embed.add_field(name="Corrupted:", value=corrupt, inline = True)
                if int(i["exaltedValue"]) > 0:
                    embed.add_field(name="Exalted Price:", value=str(round(i["exaltedValue"], 1)) + '<:emoji_name:715777693223878676>')
                    embed.add_field(name="Chaos Price:", value=str(price) + '<:emoji_name:715777677352632434>')
                else:
                    embed.add_field(name="Current Price:", value=str(price) + '<:emoji_name:715777677352632434>')
                gemList.append(embed)
    if len(gemList) == 0:
        return
    maxPage = len(gemList)
    gemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
    message = await ctx.send(embed = gemList[curPage-1])
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
                gemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = gemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                gemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = gemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                gemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = gemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                gemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = gemList[curPage-1])
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
async def base(ctx, mods: str, *, item: str = ""):
    req = requests.get("https://poe.ninja/api/data/itemoverview?league=Delirium&type=BaseType&language=en")
    data = req.json()
    maxPage = 0
    curPage = 1
    itemList = []
    if len(item) < 3:
        return
    for i in data["lines"]:
        if item.lower() in i["name"].lower() and mods.lower() == str(i["variant"]).lower() and i["levelRequired"] >= 83:
            if int(i["chaosValue"]/1000) != 0:
                price = round(i["chaosValue"]/1000, 1)
                embed = discord.Embed(
                    colour = discord.Colour.blue()
                )
                embed.set_author(name=i["name"], icon_url=i["icon"])
                embed.set_thumbnail(url=i["icon"])
                embed.add_field(name="iLvl:", value= i["levelRequired"], inline = True)
                embed.add_field(name="Influence:", value= i["variant"], inline = True)
                embed.add_field(name="Type:", value = i["itemType"], inline = True)
                if int(i["exaltedValue"]) > 0:
                    embed.add_field(name="Exalted Price:", value=str(round(i["exaltedValue"], 1)) + '<:emoji_name:715777693223878676>', inline = True)
                    embed.add_field(name="Chaos Price:", value=str(price) + 'K <:emoji_name:715777677352632434>', inline = True)
                else:
                    embed.add_field(name="Current Price:", value=str(price) + 'K <:emoji_name:715777677352632434>', inline = True)
                itemList.append(embed)
            else:
                price = round(i["chaosValue"], 1)
                embed = discord.Embed(
                    colour = discord.Colour.blue()
                )
                embed.set_author(name=i["name"], icon_url=i["icon"])
                embed.set_thumbnail(url=i["icon"])
                embed.add_field(name="iLvl:", value= i["levelRequired"], inline = True)
                embed.add_field(name="Influence:", value= i["variant"], inline = True)
                embed.add_field(name="Type:", value = i["itemType"], inline = True)
                if int(i["exaltedValue"]) > 0:
                    embed.add_field(name="Exalted Price:", value=str(round(i["exaltedValue"], 1)) + '<:emoji_name:715777693223878676>', inline = True)
                    embed.add_field(name="Chaos Price:", value=str(price) + '<:emoji_name:715777677352632434>', inline = True)
                else:
                    embed.add_field(name="Current Price:", value=str(price) + '<:emoji_name:715777677352632434>', inline = True)
                itemList.append(embed)
    if len(itemList) == 0:
        return
    maxPage = len(itemList)
    itemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
    message = await ctx.send(embed = itemList[curPage-1])
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
                itemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = itemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "➡️" and curPage == maxPage:
                curPage = 1
                itemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = itemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage > 1:
                curPage -= 1
                itemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = itemList[curPage-1])
                await message.remove_reaction(reaction, user)
            elif str(reaction.emoji) == "⬅️" and curPage == 1:
                curPage = maxPage
                itemList[curPage-1].set_footer(text = f'[Page {curPage}/{maxPage}]')
                await message.edit(embed = itemList[curPage-1])
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
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount)

poeBot.run('NzE1Njg2NzIwNjA3MjIzODc5.XtQ2uQ.FRDIwaGIyUS_ZBnT3gEM7tum1KU')

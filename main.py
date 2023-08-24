import json
import disnake
import func.battles
import func.wpn_stats
from disnake.ext import commands

with open('secrets.json', 'r') as openfile:
    secrets = json.load(openfile)

token = secrets['token']
bot = commands.InteractionBot(
    command_sync_flags=commands.CommandSyncFlags.default(), reload=True)


@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(
        type=disnake.ActivityType.watching, name="Agent 3"))

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.slash_command(name='ping', description="Check the bot's latency.")
async def ping(ctx):
    # Check out O.R.C.A.'s latency
    await ctx.send(f'Pong... `{round(bot.latency * 1000000)}μs`\nPong... `{round(bot.latency * 1000)}ms`')


# ================================================================ STAGES ==============================================================
@bot.slash_command(name="current_stages",
                   description="Get the current battle stages")
async def stages(ctx, mode: commands.option_enum({
    "Regualar Battle": "turf",
    "Anarchy Series": "series",
    "Anarchy Open": "open",
    "X Battles": "xbattle",
    "Salmon Run": "salmon"
})):
    if mode == "turf":
        await ctx.send(embeds=func.battles.getRegularStages())
    elif mode == "open":
        await ctx.send(embeds=func.battles.getAnarchyStages(True))
    elif mode == "series":
        await ctx.send(embeds=func.battles.getAnarchyStages(False))
    elif mode == "xbattle":
        await ctx.send(embeds=func.battles.getXBattles())
    elif mode == "salmon":
        await ctx.send(embeds=func.battles.getSalmon())


@bot.slash_command(name="rotation_summary", description="Get the summary of the current Splatoon 3 rotation in all modes")
async def summary(ctx):
    await ctx.send(embed=func.battles.getSummary())

# ============================================================== WEAPON STATS ==============================================================
with open('weapons.json', 'r') as openfile:
    wpn_data = json.load(openfile)
def theChoices(wpnClass):
    choices = {}
    for wpn in wpn_data.keys():
        if wpn_data[wpn]['class'] == wpnClass:
            choices.update({wpn_data[wpn]["name"]: wpn})
    return commands.option_enum(choices)

@bot.slash_command(name='weapon_stats', description='Stats for weapons')
async def weapon(ctx):
    pass

@weapon.sub_command(name='shooters', description='Stats for shooters')
async def shooters(ctx, weapon:theChoices("Shooter")):
    await ctx.send(embed=func.wpn_stats.shooter_stats(weapon))

@weapon.sub_command(name='rollers', description='Stats for rollers')
async def rollers(ctx, weapon:theChoices("Roller")):
    await ctx.send(embed=func.wpn_stats.roller_stats(weapon))

@weapon.sub_command(name='chargers', description='Stats for Chargers')
async def chargers(ctx, weapon:theChoices('Charger')):
    await ctx.send(embed=func.wpn_stats.charger_stats(weapon))

# ================================================================ MUSIC ===================================================================



bot.run(token)
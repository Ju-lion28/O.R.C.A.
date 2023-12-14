import os
import json
import random
import disnake
import datetime
import func.battles
import func.wpn_stats
from disnake.ext import commands
from disnake import TextInputStyle


with open("secrets.json", "r") as open_file:
    secrets = json.load(open_file)

token = secrets["token"]
bot = commands.InteractionBot(
    command_sync_flags=commands.CommandSyncFlags.default(), reload=True
)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=disnake.Activity(type=disnake.ActivityType.watching, name="Agent 3")
    )

    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.slash_command(name="ping", description="Check the bot's latency.")
async def ping(ctx):
    # Check out O.R.C.A.'s latency
    await ctx.send(
        f"Pong... `{round(bot.latency * 1000000)}μs`\nPong... `{round(bot.latency * 1000)}ms`"
    )


@bot.slash_command(name="help")
async def help(ctx):
    embed_dict = {
        "title": "HELP",
        "description": """
		dw im here to help you
		but bro tbh its not that deep all the commands have descriptions that i (the developer) have painstakingly put in for you
		""",
        "color": func.battles.rndColour()[random.randint(0, 1)],
        "timestamp": datetime.datetime.now().isoformat(),
        "author": {
            "name": "O.R.C.A.",
            # "url": "https://disnake.dev/",
            "icon_url": "https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925",
        },
        "thumbnail": {
            "url": "https://hpsny.org/wp-content/uploads/2015/02/help-153094_1280.png"
        },
        # "fields": [
        # 	{"name": "You need help with this command", "value": "This is not gonna help you lamo", "inline": "false"},
        # ],
        # "image": {"url": "https://disnake.dev/assets/disnake-banner-thin.png"},
        "footer": {
            "text": "Brought to you by your Omniscient Recording Computer of Alterna",
            "icon_url": "https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925",
        },
    }
    await ctx.send(embed=disnake.Embed.from_dict(embed_dict))


# # Subclassing the modal.
# class MyModal(disnake.ui.Modal):
#     def __init__(self):
#         # The details of the modal, and its components
#         components = [
#             disnake.ui.TextInput(
#                 label="Name",
#                 placeholder="Foo Tag",
#                 custom_id="name",
#                 style=TextInputStyle.short,
#                 max_length=50,
#             ),
#             disnake.ui.TextInput(
#                 label="Description",
#                 placeholder="Lorem ipsum dolor sit amet.",
#                 custom_id="description",
#                 style=TextInputStyle.paragraph,
#             ),
#         ]
#         super().__init__(title="Create Tag", components=components)

#     # The callback received when the user input is completed.
#     async def callback(self, inter: disnake.ModalInteraction):
#         embed = disnake.Embed(title="Tag Creation")
#         for key, value in inter.text_values.items():
#             embed.add_field(
#                 name=key.capitalize(),
#                 value=value[:1024],
#                 inline=False,
#             )
#         await inter.response.send_message(embed=embed)


# @bot.slash_command(name="tags")
# async def tags(inter: disnake.AppCmdInter):
#     """Sends a Modal to create a tag."""
#     await inter.response.send_modal(modal=MyModal())

# ================================================================ STAGES ==============================================================
@bot.slash_command(name="current_stages", description="Get the current battle stages")
async def stages(
    ctx,
    mode: commands.option_enum(
        {
            "Regular Battle": "turf",
            "Anarchy Series": "series",
            "Anarchy Open": "open",
            "X Battles": "xbattle",
            "Salmon Run": "salmon",
        }
    ),
):
    if mode == "turf":
        await ctx.send(embeds=func.battles.getRegularStages(),
                       components=[disnake.ui.Button(label="Next", 
                                                     style=disnake.ButtonStyle.success, 
                                                     custom_id="nextTurf"
                                                     )])
    elif mode == "open":
        await ctx.send(embeds=func.battles.getAnarchyStages(True),
                       components=[disnake.ui.Button(label="Next", 
                                                     style=disnake.ButtonStyle.success, 
                                                     custom_id="nextOpen"
                                                     )])
    elif mode == "series":
        await ctx.send(embeds=func.battles.getAnarchyStages(False),
                       components=[disnake.ui.Button(label="Next", 
                                                     style=disnake.ButtonStyle.success, 
                                                     custom_id="nextSeries"
                                                     )])
    elif mode == "xbattle":
        await ctx.send(embeds=func.battles.getXBattles(),
                       components=[disnake.ui.Button(label="Next", 
                                                     style=disnake.ButtonStyle.success, 
                                                     custom_id="nextX"
                                                     )])
    elif mode == "salmon":
        await ctx.send(embeds=func.battles.getSalmon(),
                       components=[disnake.ui.Button(label="Next", 
                                                     style=disnake.ButtonStyle.success, 
                                                     custom_id="nextSalmon"
                                                     )])


@bot.listen("on_button_click")
async def next_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ['nextTurf','nextOpen','nextSeries','nextX','nextSalmon']:
        return
    else:
        node = 1

    if inter.component.custom_id == 'nextTurf':
        await inter.response.send_message(embeds=func.battles.getRegularStages(node))
    if inter.component.custom_id == 'nextOpen':
        await inter.response.send_message(embeds=func.battles.getAnarchyStages(isSeriesOpen=True, node = node))
    if inter.component.custom_id == 'nextSeries':
        await inter.response.send_message(embeds=func.battles.getAnarchyStages(isSeriesOpen=False, node = node))
    if inter.component.custom_id == 'nextX':
        await inter.response.send_message(embeds=func.battles.getXBattles(node = node))
    if inter.component.custom_id == 'nextSalmon':
        await inter.response.send_message(embeds=func.battles.getSalmon(node = node))

@bot.slash_command(
    name="rotation_summary",
    description="Get the summary of the current Splatoon 3 rotation in all modes",
)
async def summary(ctx):
    await ctx.send(embed=func.battles.getSummary())


# ============================================================== WEAPON STATS ==============================================================
with open("weapons.json", "r") as open_file:
    wpn_data = json.load(open_file)


def theChoices(wpnClass):
    choices = {}
    for wpn in wpn_data.keys():
        if wpn_data[wpn]["class"] == wpnClass:
            choices.update({wpn_data[wpn]["name"]: wpn})
    return commands.option_enum(choices)


@bot.slash_command(name="weapon_stats", description="Stats for weapons")
async def weapon(ctx):
    pass


@weapon.sub_command(name="shooters", description="Stats for shooters")
async def shooters(ctx, weapon: theChoices("Shooter")):
    await ctx.send(embed=func.wpn_stats.shooter_stats(weapon))


@weapon.sub_command(name="rollers", description="Stats for rollers")
async def rollers(ctx, weapon: theChoices("Roller")):
    await ctx.send(embed=func.wpn_stats.roller_stats(weapon))


@weapon.sub_command(name="chargers", description="Stats for Chargers")
async def chargers(ctx, weapon: theChoices("Charger")):
    await ctx.send(embed=func.wpn_stats.charger_stats(weapon))


# ================================================================ MUSIC ===================================================================


bot.run(token)
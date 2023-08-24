import disnake
import requests
import json
import random
import datetime
import dateutil.parser as dp


def reload():
    response = requests.get('https://splatoon3.ink/data/schedules.json')
    json_data = json.loads(response.text)

    return json_data


def rndColour(salmon=False):
    if salmon:
        colours = [
            (0x435bf3, 0x067e63),
            (0xc44b21, 0x067e63),
            (0xc64184, 0x067e63),
            (0x9361ea, 0x067e63),
            (0xdda024, 0x067e63),
            (0xb4d933, 0x067e63)
        ]
    else:
        colours = [
            (0x1a1aae, 0xe38d24),
            (0xa0c937, 0xba30b0),
            (0xbecd41, 0x6325cd),
            (0xde6624, 0x343bc4),
            (0xcd510a, 0x6e04b6),
            (0xc12d74, 0x2cb721),
            (0x1bbeab, 0xc43a6e),
            (0x1ec0ad, 0xd74b31),
            (0xd0be08, 0x3a0ccd),
            (0xceb121, 0x9025c6)
        ]
    return random.choice(colours)


def getImages(imgId1, imgId2):
    json_data = reload()
    images = json_data["data"]["vsStages"]["nodes"]
    stageImg1 = ''
    stageImg2 = ''

    for stage in images:
        if stage["vsStageId"] == imgId1:
            stageImg1 = stage["originalImage"]["url"]
        elif stage["vsStageId"] == imgId2:
            stageImg2 = stage["originalImage"]["url"]

    imgs = [stageImg1, stageImg2]

    return imgs


def iso2epoch(iso):
    return int(dp.parse(iso).timestamp())


def getRegularStages():
    json_data = reload()
    stages = json_data["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsStages"]
    mode = json_data["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsRule"]

    stageName1, stageName2 = stages[0]["name"], stages[1]["name"]

    stageImgId1 = stages[0]["vsStageId"]
    stageImgId2 = stages[1]["vsStageId"]

    turfImages = getImages(stageImgId1, stageImgId2)

    startTime = json_data["data"]["regularSchedules"]["nodes"][0]["startTime"]
    endTime = json_data["data"]["regularSchedules"]["nodes"][0]["endTime"]

    colour = rndColour()

    stage1 = disnake.Embed(
        title=stageName1,
        description=f"""
        `Game Mode:  `**REGULAR BATTLE -> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[0]),
        timestamp=datetime.datetime.now()
    )
    stage1.set_image(url=turfImages[0])
    stage1.set_thumbnail(
        url="https://www.pngkey.com/png/full/41-416334_turf-wars-icon-splatoon-2-turf-war-symbol.png")
    stage1.set_author(
        name="CURRENT REGULAR BATTLE STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/4/48/S2_Icon_Regular_Battle.svg/250px-S2_Icon_Regular_Battle.svg.png",
    )
    stage1.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stage2 = disnake.Embed(
        title=stageName2,
        description=f"""
        `Game Mode:  `**REGULAR BATTLE -> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now()
    )
    stage2.set_image(url=turfImages[1])
    stage2.set_thumbnail(
        url="https://www.pngkey.com/png/full/41-416334_turf-wars-icon-splatoon-2-turf-war-symbol.png")
    stage2.set_author(
        name="CURRENT REGULAR BATTLE STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/4/48/S2_Icon_Regular_Battle.svg/250px-S2_Icon_Regular_Battle.svg.png",
    )
    stage2.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stageEmbeds = [stage1, stage2]

    return stageEmbeds


def getAnarchyStages(isSeriesOpen):
    json_data = reload()
    if isSeriesOpen:
        matchType = 1
    else:
        matchType = 0

    anarchyDict = ["**SERIES**", "**OPEN**"]

    stages = json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][matchType]["vsStages"]
    mode = json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][matchType]["vsRule"]

    stageName1, stageName2, stageId1, stageId2 = stages[0]['name'], stages[
        1]['name'], stages[0]['vsStageId'], stages[1]['vsStageId']
    anarchyImages = getImages(stageId1, stageId2)

    startTime = json_data["data"]["bankaraSchedules"]["nodes"][0]["startTime"]
    endTime = json_data["data"]["bankaraSchedules"]["nodes"][0]["endTime"]

    colour = rndColour()

    thumbnails = {
        "Tower Control": "https://cdn.wikimg.net/en/splatoonwiki/images/b/bc/S3_icon_Tower_Control.png",
        "Clam Blitz": "https://cdn.wikimg.net/en/splatoonwiki/images/e/e3/S3_icon_Clam_Blitz.png",
        "Rainmaker": "https://cdn.wikimg.net/en/splatoonwiki/images/1/12/S3_icon_Rainmaker.png",
        "Splat Zones": "https://cdn.wikimg.net/en/splatoonwiki/images/3/38/S3_icon_Splat_Zones.png"
    }

    stage1 = disnake.Embed(
        title=stageName1,
        description=f"""
        `Game Mode:  `{anarchyDict[matchType]} **-> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[0]),
        timestamp=datetime.datetime.now()
    )
    stage1.set_image(url=anarchyImages[0])
    stage1.set_thumbnail(url=thumbnails[mode['name']])
    stage1.set_author(
        name=f"CURRENT ANARCHY {anarchyDict[matchType][2:-2]} STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/c5/S2_Icon_Ranked_Battle.svg/250px-S2_Icon_Ranked_Battle.svg.png",
    )
    stage1.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stage2 = disnake.Embed(
        title=stageName2,
        description=f"""
        `Game Mode:  `{anarchyDict[matchType]} **-> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now()
    )
    stage2.set_image(url=anarchyImages[1])
    stage2.set_thumbnail(url=thumbnails[mode['name']])
    stage2.set_author(
        name=f"CURRENT ANARCHY {anarchyDict[matchType][2:-2]} STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/c5/S2_Icon_Ranked_Battle.svg/250px-S2_Icon_Ranked_Battle.svg.png",
    )
    stage2.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stageEmbeds = [stage1, stage2]

    return stageEmbeds


def getXBattles():
    json_data = reload()

    stages = json_data["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsStages"]
    mode = json_data["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsRule"]

    stageName1, stageName2, stageId1, stageId2 = stages[0]['name'], stages[
        1]['name'], stages[0]['vsStageId'], stages[1]['vsStageId']
    xImages = getImages(stageId1, stageId2)

    startTime = json_data["data"]["xSchedules"]["nodes"][0]["startTime"]
    endTime = json_data["data"]["xSchedules"]["nodes"][0]["endTime"]

    colour = rndColour()

    thumbnails = {
        "Tower Control": "https://cdn.wikimg.net/en/splatoonwiki/images/b/bc/S3_icon_Tower_Control.png",
        "Clam Blitz": "https://cdn.wikimg.net/en/splatoonwiki/images/e/e3/S3_icon_Clam_Blitz.png",
        "Rainmaker": "https://cdn.wikimg.net/en/splatoonwiki/images/1/12/S3_icon_Rainmaker.png",
        "Splat Zones": "https://cdn.wikimg.net/en/splatoonwiki/images/3/38/S3_icon_Splat_Zones.png"
    }

    stage1 = disnake.Embed(
        title=stageName1,
        description=f"""
        `Game Mode:  `**X BATTLE -> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[0]),
        timestamp=datetime.datetime.now()
    )
    stage1.set_image(url=xImages[0])
    stage1.set_thumbnail(url=thumbnails[mode['name']])
    stage1.set_author(
        name=f"CURRENT X BATTLE STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/3e/S3_Icon_X_Battle.svg/40px-S3_Icon_X_Battle.svg.png",
    )
    stage1.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stage2 = disnake.Embed(
        title=stageName2,
        description=f"""
        `Game Mode:  `**X BATTLE -> {mode['name']}**
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now()
    )
    stage2.set_image(url=xImages[1])
    stage2.set_thumbnail(url=thumbnails[mode['name']])
    stage2.set_author(
        name=f"CURRENT X BATTLE STAGES",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/3e/S3_Icon_X_Battle.svg/40px-S3_Icon_X_Battle.svg.png",
    )
    stage2.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    stageEmbeds = [stage1, stage2]

    return stageEmbeds


def getSalmon():
    json_data = reload()

    stage = json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["coopStage"]
    stageName, stageImage = stage["name"], stage["image"]["url"]
    wpn = json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"]

    weaponsArray = []

    for weapon in range(len(wpn)):
        weaponName = wpn[weapon]["name"]
        weaponImage = wpn[weapon]["image"]["url"]

        weaponsArray.append([weaponName, weaponImage])

    startTime = json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["startTime"]
    endTime = json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["endTime"]

    URL = "https://splatoon3.ink/salmonrun"

    colour = rndColour(True)

    stageEmbed = disnake.Embed(
        title=stageName,
        description=f"""
        `Started at: `<t:{iso2epoch(startTime)}>
        `Ends at:    `<t:{iso2epoch(endTime)}>""",
        colour=disnake.Colour(colour[0]),
        timestamp=datetime.datetime.now()
    )
    stageEmbed.set_image(url=stageImage)
    stageEmbed.set_thumbnail(
        url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f0/SplatNet_3_icon_Salmon_Run.svg/2048px-SplatNet_3_icon_Salmon_Run.svg.png")
    stageEmbed.set_author(
        name=f"CURRENT SALMON RUN STAGE",
        icon_url="https://cdn.wikimg.net/en/splatoonwiki/images/b/b3/S3_Icon_Mr_Grizz.png",
    )
    stageEmbed.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    weapon1 = disnake.Embed(
        title="WEAPONS",
        description=f"""
        {weaponsArray[0][0]}
        {weaponsArray[1][0]}
        {weaponsArray[2][0]}
        {weaponsArray[3][0]}""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now(),
        url=URL
    )
    weapon2 = disnake.Embed(
        title="WEAPONS",
        description=f"""
        {weaponsArray[0][0]}
        {weaponsArray[1][0]}
        {weaponsArray[2][0]}
        {weaponsArray[3][0]}""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now(),
        url=URL
    )
    weapon3 = disnake.Embed(
        title="WEAPONS",
        description=f"""
        {weaponsArray[0][0]}
        {weaponsArray[1][0]}
        {weaponsArray[2][0]}
        {weaponsArray[3][0]}""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now(),
        url=URL
    )
    weapon4 = disnake.Embed(
        title="WEAPONS",
        description=f"""
        {weaponsArray[0][0]}
        {weaponsArray[1][0]}
        {weaponsArray[2][0]}
        {weaponsArray[3][0]}""",
        colour=disnake.Colour(colour[1]),
        timestamp=datetime.datetime.now(),
        url=URL
    )
    weapon1.set_image(url=weaponsArray[0][1])
    weapon2.set_image(url=weaponsArray[1][1])
    weapon3.set_image(url=weaponsArray[2][1])
    weapon4.set_image(url=weaponsArray[3][1])

    embeds = [stageEmbed, weapon1, weapon2, weapon3, weapon4]

    return embeds


def getLeague():
    pass


def getSummary():
    json_data = reload()

    stageNames = {
        "turfStages": [json_data["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsStages"][0]["name"], json_data["data"]["regularSchedules"]["nodes"][0]["regularMatchSetting"]["vsStages"][1]["name"]],
        "openStages": [json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsStages"][0]["name"], json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsStages"][1]["name"]],
        "seriesStages": [json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsStages"][0]["name"], json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsStages"][1]["name"]],
        "xStages": [json_data["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsStages"][0]["name"], json_data["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsStages"][1]["name"]],
        "salmonStage": json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["coopStage"]["name"]
    }

    salmonGuns = [json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][0]["name"], json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][1]
                  ["name"], json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][2]["name"], json_data["data"]["coopGroupingSchedule"]["regularSchedules"]["nodes"][0]["setting"]["weapons"][3]["name"]]

    rankedModes = {
        "openMode": json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][1]["vsRule"]["name"],
        "seriesMode": json_data["data"]["bankaraSchedules"]["nodes"][0]["bankaraMatchSettings"][0]["vsRule"]["name"],
        "xMode": json_data["data"]["xSchedules"]["nodes"][0]["xMatchSetting"]["vsRule"]["name"]
    }

    colour = rndColour()

    embed = disnake.Embed(
        title="CURRENT SPLATOON ROTATION SUMMARY",
        colour=disnake.Colour(colour[random.randint(0, 1)]),
        timestamp=datetime.datetime.now()
    )

    embed.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )

    embed.add_field(name="TURF WAR",
                    value=f"""
**STAGES:**
- {stageNames['turfStages'][0]}
- {stageNames['turfStages'][1]}""",
                    inline=True)

    embed.add_field(name="ANARCHY OPEN",
                    value=f"""
**MODE:** {rankedModes['openMode']}
**STAGES:**
- {stageNames['openStages'][0]}
- {stageNames['openStages'][1]}""",
                    inline=True)

    embed.add_field(name="ANARCHY SERIES",
                    value=f"""
**MODE:** {rankedModes['seriesMode']}
**STAGES:**
- {stageNames['seriesStages'][0]}
- {stageNames['seriesStages'][1]}""",
                    inline=True)

    embed.add_field(name="X BATTLE",
                    value=f"""
**MODE:** {rankedModes['xMode']}
**STAGES:**
- {stageNames['xStages'][0]}
- {stageNames['xStages'][1]}""",
                    inline=True)

    embed.add_field(name="SALMON RUN",
                    value=f"""
**STAGE:** {stageNames['salmonStage']}
**WEAPONS:**
- {salmonGuns[0]}
- {salmonGuns[1]}
- {salmonGuns[2]}
- {salmonGuns[3]}""",
                    inline=True)

    embed.add_field(name='​',value='​',inline=True)

    return embed

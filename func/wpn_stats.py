import disnake
import json
import func.battles
import random

def shooter_stats(weapon):
    with open('weapons.json', 'r') as openfile:
        wpn_data = json.load(openfile)

    wpn_stats = wpn_data[weapon]
    colour = func.battles.rndColour()
    desc = f"""
    ```
Name:               {wpn_stats['name']}
Class:              {wpn_stats['class']}
Sub Weapon:         {wpn_stats['sub']}
Special Weapon:     {wpn_stats['special']}
Points for Special: {wpn_stats['specialPoints']}p
Range:              {int(wpn_stats['range']*100)}/100
Damage:             {int(wpn_stats['damage']*100)}/100
Base Damage:        {wpn_stats['baseDamage']}
Fire Rate:          {int(wpn_stats['fireRate']*100)}/100
Unlocked at Level:  {wpn_stats['levelNeeded']}
```"""

    weapon_embed = disnake.Embed(
        title="Weapon Stats",
        description=desc,
        colour=colour[random.randint(0,1)]
    )

    weapon_embed.set_image(url=wpn_stats['image']['url'])
    weapon_embed.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )
    
    return weapon_embed

def roller_stats(weapon):
    with open('weapons.json', 'r') as openfile:
        wpn_data = json.load(openfile)

    wpn_stats = wpn_data[weapon]
    colour = func.battles.rndColour()
    desc = f"""
    ```
Name:               {wpn_stats['name']}
Class:              {wpn_stats['class']}
Sub Weapon:         {wpn_stats['sub']}
Special Weapon:     {wpn_stats['special']}
Points for Special: {wpn_stats['specialPoints']}p
Range:              {int(wpn_stats['range']*100)}/100
Ink Speed:          {int(wpn_stats['inkSpeed']*100)}/100
Handling:           {int(wpn_stats['handling']*100)}/100
Unlocked at Level:  {wpn_stats['levelNeeded']}
```"""

    weapon_embed = disnake.Embed(
        title="Weapon Stats",
        description=desc,
        colour=colour[random.randint(0,1)]
    )

    weapon_embed.set_image(url=wpn_stats['image']['url'])
    weapon_embed.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )
    
    return weapon_embed

def charger_stats(weapon):
    with open('weapons.json', 'r') as openfile:
        wpn_data = json.load(openfile)

    wpn_stats = wpn_data[weapon]
    colour = func.battles.rndColour()
    desc = f"""
    ```
Name:               {wpn_stats['name']}
Class:              {wpn_stats['class']}
Sub Weapon:         {wpn_stats['sub']}
Special Weapon:     {wpn_stats['special']}
Points for Special: {wpn_stats['specialPoints']}p
Range:              {int(wpn_stats['range']*100)}/100
Charge Speed:       {int(wpn_stats['chargeSpd']*100)}/100
Mobility:           {int(wpn_stats['mobility']*100)}/100
Unlocked at Level:  {wpn_stats['levelNeeded']}
```"""

    weapon_embed = disnake.Embed(
        title="Weapon Stats",
        description=desc,
        colour=colour[random.randint(0,1)]
    )

    weapon_embed.set_image(url=wpn_stats['image']['url'])
    weapon_embed.set_footer(
        text="Brought to you by your Omniscient Recording Computer of Alterna",
        icon_url="https://static.wikia.nocookie.net/splatoon/images/e/e0/O.R.C.A._logo.png/revision/latest?cb=20221009143925"
    )
    
    return weapon_embed

# Copyright (C) 2020
# C O D E A Z - Samil

from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__cod")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.cod(?: |$)(.*)")
async def cod(event):

    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [list(CMD_HELP)[i:i + 5] for i in range(0, len(list(CMD_HELP)), 5)]
        
        for i in sayfa:
            string += f'`➤ `'
            for sira, a in enumerate(i):
                string += "__" + str(a)
                if sira == i.index(i[-1]):
                    string += "__"
                else:
                    string += "`, "
            string += "\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)

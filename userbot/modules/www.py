# U S Σ R Δ T O R / Ümüd


""" İnternet. """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.cmdtr import CmdTr

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("www")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ .speed. """
    await spd.edit(LANG['SPEED'])
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    result = test.results.dict()

    await spd.edit("`"
                   f"{LANG['STARTED_TIME']}"
                   f"{result['timestamp']} \n\n"
                   f"{LANG['DOWNLOAD_SPEED']}"
                   f"{speed_convert(result['download'])} \n"
                   f"{LANG['UPLOAD_SPEED']}"
                   f"{speed_convert(result['upload'])} \n"
                   "Pinginiz: "
                   f"{result['ping']} \n"
                   f"{LANG['ISP']}"
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Salam DTÖUserBot, baytları oxuya bilmirsən?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.dc$")
async def neardc(event):
    """ .dc """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Şəhər : `{result.country}`\n"
                     f"Ən yaxın datacenter : `{result.nearest_dc}`\n"
                     f"İndiki datacenter : `{result.this_dc}`")


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ .ping  """
    start = datetime.now()
    await pong.edit("`Pinginiz!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pinginiz!\n%sms`" % (duration))

CmdHelp('www').add_command(
    'speed', None, 'Bir speedtest edər və nəticəni göstərər.'
).add_command(
    'dc', None, 'Serverinizə ən yaxın datacenter\'ı göstərər.'
).add_command(
    'ping', None, 'Botun ping dəyərini göstərər.'
).add()

CmdTr('www').add_command(
    'speed', None, 'Bir speedtest uygular ve sonucu gösterir.'
).add_command(
    'dc', None, 'Sunucunuza en yakın datacenter\'ı gösterir.'
).add_command(
    'ping', None, 'Botun ping değerini gösterir.'
).add()


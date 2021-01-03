import os
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.cmdtr import CmdTr

chat = "@MissRose_bot"

@register(outgoing=True, pattern="^.fstat ?(.*)")
async def fstat(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        dtoub = event.pattern_match.group(1)
    else:
        dtoub = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        istifadeci = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + istifadeci + " " + codub)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + codub)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await event.client.send_message(event.chat_id, reply)
                else:
                    await event.client.send_message(event.chat_id, fedstat)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")


@register(outgoing=True, pattern="^.info ?(.*)")
async def info(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        dtoub = event.pattern_match.group(1)
    else:
        dtoub = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        istifadeci = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + istifadeci)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + codub)
                audio = await conv.get_response()
                await event.client.forward_messages(event.chat_id, audio)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")


@register(outgoing=True, pattern="^.fedinfo ?(.*)")
async def fedinfo(event):
    if event.fwd_from:
        return
    dtoub = event.pattern_match.group(1)
    if dtoub == "" and not event.reply_to_msg_id:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo")
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedinfo " + codub)
                fedinfo = await conv.get_response()
                await event.client.forward_messages(event.chat_id, fedinfo)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")


@register(outgoing=True, pattern="^.myfeds ?(.*)")
async def myfeds(event):
    if event.fwd_from:
        return
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/myfeds")
            myfed = await conv.get_response()
            if "file" in myfed.text:
                await fedstat.click(0)
                reply = await conv.get_response()
                await event.client.send_message(event.chat_id, reply)
            else:
                await event.client.send_message(event.chat_id, myfed)
                await event.delete()
        except YouBlockedUserError:
            await event.edit("@MissRose_bot'u blokdan çıxardıb yenidən cəhd edin.")
            
CmdHelp('rose').add_command(
    'fstat', '<tag/id>', 'Şəxsin hansı federasiyalardan fban olduğu haqda məlumat veər. \n Boş .fstat yazsanız sizin fban olduğunuz fed’ləri göstərər '
).add_command(
    'info', '<tag/id>', 'Verdiyiniz tag və ya id’ə əsasən məlumat verər. \n Boş .info yazsanız sizin haqda məlumat verər.'
).add_command(
    'fedinfo', '<fed id>', 'Federasiya haqda məlumat verər.'
).add_command(
    'myfeds', ' ', 'Sahib və ya səlahiyyətli olduğunuz fed’ləri göstərər.'
).add()

CmdTr('rose').add_command(
    'fstat', '<tag/id>', 'Kullanıcı hangi federasiyalardan fban olduğu hakkında bilgi verir. \n Boş .fstat yazarsanız sizin fban olduğunuz fed’leri gösterir '
).add_command(
    'info', '<tag/id>', 'Verdiyiniz tag ve ya id’e göre bilgi verir. \n Boş .info yazarsanız sizin bilgiler verir.'
).add_command(
    'fedinfo', '<fed id>', 'Federasiya hakkında bilgi verir.'
).add_command(
    'myfeds', ' ', 'Sahip ve ya admin olduğunuz fed’leri gösterir.'
).add()

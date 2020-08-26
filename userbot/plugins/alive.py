import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/108c73c3d62e3aa743dbd.png"
pm_caption = "`💠R.O.C.K.Y IS💠:` **ONLINE**\n\n"

pm_caption += "**🔖SYSTEM STATUS🔖**\n\n"
pm_caption += "`⚖️TELETHON VERSION⚖️:` **6.0.9**\n`Python:` **3.7.4**\n\n"
pm_caption += "`🎢DATABASE STATUS🎢:` **Functional**\n\n"
pm_caption += "**📬ROCKY OS📬** : `3.14`\n\n"
pm_caption += "**💡Current Sat💡** : `ROCKY-2.25`\n\n"
pm_caption += f"*💜*My Boss💜** : {DEFAULTUSER} \n\n"
pm_caption += "**💥Heroku Database💥** : `AWS - Working Properly`\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    

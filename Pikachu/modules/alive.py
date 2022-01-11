from telethon import events, Button, custom
import re, os
from Pikachu.events import register
from Pikachu import telethn as tbot
from Pikachu import telethn as tgbot
PHOTO = "https://telegra.ph/file/7b0e22a3629295f34988d.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m infernipe** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ infernipe: 2.2 LATEST**\n\n"
  PIKACHU += "**♡ My Master :** [harsha](@harshahero)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  PIKACHU += "**♡ Kali Linux : yes**\n\n"
  PIKACHU += "**♡ Python : 3.9.7**\n\n"
  PIKACHU += "**♡ Database status : Functional**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/NovusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/NovusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "Alive⚜️"

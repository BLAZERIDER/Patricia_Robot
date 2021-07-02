import os 
import glob
import random
from . import *

from ShasaBot.events import register
from ShasaBot import OWNER_ID
from ShasaBot import telethn as tbot

from PIL import Image, ImageDraw, ImageFont

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
 
  if not quew:
     await event.reply('Darling Listen! Provide Some Text To Draw!')
     return
 await event.reply('Tiana! Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    imgpath_ = glob.glob("ShasaBot/resources/logo/*")
    img = random.choice(imgpath_)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./ShasaBot/resources/font/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "LogobyTiana.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By Tianabot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @PrinceBotSupport, {e}')

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 • `/logo text`*:*  Create your logo with your name
 • `/alogo`*:*  Create your logo with your name
 """
__mod_name__ = "LOGO"

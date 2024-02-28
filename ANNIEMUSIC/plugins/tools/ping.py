from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ANNIEMUSIC import app
from ANNIEMUSIC.core.call import JARVIS
from ANNIEMUSIC.utils import bot_sys_stats
from ANNIEMUSIC.utils.decorators.language import language
from ANNIEMUSIC.utils.inline import supp_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance  # Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("toe", prefixes=["/", "!",]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://graph.org/file/684c07c8bfe921618aa1f.jpg"
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀Devil sᴛᴀʀᴛᴇᴅ ᴄᴏʟʟᴇᴄᴛɪɴɢ ᴅᴀᴛᴀ.**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀Devil ᴀɴᴀʟʏsɪɴɢ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs..**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**🥀Devil ᴜᴘɢʀᴀᴅᴇᴅ ᴛʜᴇ ᴊᴀʀᴠɪs ᴄᴏʀᴇ...**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**🥀Devil ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ....**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**Devil ʜᴀs sᴜᴄᴄᴇssғᴜʟʟʏ ᴀɴᴀʟʏsᴇᴅ sʏsᴛᴇᴍ ᴅᴀᴛᴀ !**")
    await asyncio.sleep(2)
    await response.edit_caption("**Devil 📩sᴇɴᴅɪɴɢ sʏsᴛᴇᴍ ᴀɴᴀʟʏsᴇᴅ ᴅᴀᴛᴀ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    start = datetime.now()
    pytgping = await JARVIS.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**🏓ᴀɴɴɪᴇ..ᴍᴇᴇɴʏ..ᴍɪɴʏ..ᴍᴏᴇ✨\nㅤ  🎸👀ᴄᴀᴛᴄʜ..ᴛʜᴇ..sᴛᴀᴛs..ʙʏ..ᴛʜᴇ..Devil🫣💞**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="✦ ɢʀᴏᴜᴘ ✦", url=f"https://t.me/your_devillok",
            ),
            InlineKeyboardButton(
                text="✧ ᴍᴏʀᴇ ✧", url=f"https://t.me/your_devil82",
            )
        ],
        [
            InlineKeyboardButton(
                text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
        )
    await response.delete()

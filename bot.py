# Made with Python3
# (C) Vivek-TP and FayasNoushad

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Info Bot",
        bot_token = os.environ["2086448980:AAG42Xtn33SyZQKo9um7xYN2EKtby-TqT2c"],
        api_id = int(os.environ["16117657"]),
        api_hash = os.environ["e166a2d1ffd5fff0c2db49bee23ec224"]
)


BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="SOURCE", url=f"https://github.com/vivek-tp/Info-Bot")
        ]]
    )


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="SOURCE", url=f"https://github.com/vivek-tp/Info-Bot")
        ]]
    )
                
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention) 
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**🙋🏻‍♂️ First Name :** {update.from_user.first_name}

**🧖‍♂️ Your Second Name :** {last_name}

**🧑🏻‍🎓 Your Username :** {update.from_user.username}

**🆔 Your Telegram ID :** {update.from_user.id}

**🔗 Your Profile Link :** {update.from_user.mention}
""" 
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    text = f"""
**Your Telegram ID :** {update.from_user.id}
"""
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

print(
    """
Bot Started!!! Now Join on @Vkprojects
"""
)

Bot.run()

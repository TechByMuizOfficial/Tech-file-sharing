# btn : about and close change here

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Tech Muiz</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Tech_Muiz_Official'>Channel</a>\n○ Bot ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Tech_Muiz_Official'>Tech Muiz</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Tech_Muiz_Official_Chat'>Chat</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                        InlineKeyboardButton('🍁 Channel', url='https://t.me/Tech_Muiz_Official')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

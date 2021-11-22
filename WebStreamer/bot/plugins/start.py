from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command('start')
async def start(_, m: Message):
    await m.reply_photo("https://file2onlinebot.herokuapp.com/92/20211117_220047.jpg",
    caption='**Hᴇʏ! {m.from_user.mention(style="md")} 😚\n\nI Aᴍ Fɪʟᴇ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇʀ Bᴏᴛ 🤖\n\nI Cᴀɴ Sᴛʀᴇᴀᴍ Yᴏᴜʀ Vɪᴅᴇᴏ Tᴏ! ⏯️\n\nSᴇɴᴅ Aɴʏ Fɪʟᴇ Tᴏ Gᴇᴛ Lɪɴᴋ 🔗**',
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton('🍿 Join Our Channel 🍿', url="https://t.me/iPopcornMovie")]
                                 ]))

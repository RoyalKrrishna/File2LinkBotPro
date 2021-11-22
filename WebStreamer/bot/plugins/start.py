from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start_handler(_, m: Message):
    await m.reply_photo("https://telegra.ph/file/901cae2e860fc46d97d5b.jpg",
    caption=f'**Hᴇʏ! {m.from_user.mention(style="md")} 😚\n\nI Aᴍ Fɪʟᴇ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇʀ Bᴏᴛ 🤖\n\nI Cᴀɴ Sᴛʀᴇᴀᴍ Yᴏᴜʀ Vɪᴅᴇᴏꜱ Tᴏ! ⏯️\n\nSᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ Tᴏ Gᴇᴛ Lɪɴᴋ 🔗**',
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("🔰 Join Our Channel 🔰", url="https://t.me/iPopcornMovie")]
                                 ]))

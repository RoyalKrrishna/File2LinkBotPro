from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start_handler(_, m: Message):
    await m.reply_photo("https://telegra.ph/file/f35d8b79281781574e6f4.jpg",
    caption="**Hey Dear! 😚\n\nWelcome to the largest movies and\nseries world on Telegram!🍿\n\nSend only movie name!**🎟️",
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("🍿 Join Our Channel 🍿", url="https://t.me/iPopcornMovie")],
                                     [InlineKeyboardButton("💬 Add Me To Your Groups 💬", url="http://t.me/iPopcornMovieSearchBot?startgroup=botstart")]
                                 ]))

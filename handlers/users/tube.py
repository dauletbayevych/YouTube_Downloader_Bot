from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube

@dp.message_handler(Text(startswith="http"))
async def myFunc(message:types.Message):
    link=message.text
    from io import BytesIO
    buffer=BytesIO()
    url=YouTube(link)
    if url.check_availability() is None:
        audio=url.streams.get_audio_only()
        audio.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        music_name=url.title 
        await message.answer_audio(audio=buffer, caption=music_name)
    
    else:
        await message.answer("Xatolik yuz berdi")

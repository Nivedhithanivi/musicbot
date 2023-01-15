import requests, time

from pyrogram import idle

from pyrogram import Client as Bot

from callsmusic.callsmusic import client as USER

from callsmusic import run

from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(

    ":memory:",

    API_ID,

    API_HASH,

    bot_token=BOT_TOKEN,

    plugins=dict(root="handlers")

)

lbda = time.time()

async def main():

    async with bot:

        try:

            await USER.join_chat("in your")

            await USER.join_chat("in your")

            await USER.join_chat("in your")

        except UserAlreadyParticipant:

            pass

        except Exception as e:

            print(e)

            pass

bot.start()

run()

idle()

__version__ = (1, 0, 0)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
# 2022

from .. import loader, utils

from asyncio import sleep

import random


from telethon.tl.types import Message


class CasinoRouletteMod(loader.Module):
    strings = {
        "name": "CasinoFruit",
        "lose": "😢 <b> Unfortunately you lost </b>",
        "jackpot": "💰 <b> It seems ... jackpoot! YOU TORE JACKPOT! </b>",
        "win": "😃 <b> Hmmm, you won something!</b>",
        "pocti": "😵‍💫 <b>You were close to win!</b>",
    }
    strings_ru = {
        "lose": "😢 <b>К сожалению вы проиграли</b>",
        "jackpot": "💰 <b>Кажется... ДЖЕКПОООТ! ВЫ СОРВАЛИ КУШ!</b>",
        "win": "😃 <b> Хммм, вы что-то выиграли!</b>",
        "pocti": "😵‍💫 <b>Ты был слишком близко к победе!</b>",
    }
    strings_ua = {
        "lose": "😢 <b>Нажаль, ви програли</b>",
        "jackpot": "💰 <b>Секунду... ДЖЕКПОООТ! ВИ СПІЙМАЛИ ДЖЕКПОТ!!!</b>",
        "win": "😃 <b> Хммм, ви щось виграли!</b>",
        "pocti": "😵‍💫 <b>Ти був дуже близько до виграшу!</b>",
    }

    async def rulcmd(self, message: Message):
        """Игра в рулетку!"""

        await message.delete()

        async def devnull(*args):

            ...

        message1 = await self.inline.form(
            message=utils.get_chat_id(message),
            text="<b>КРУЧУ РУЛЕТКУ</b>",
            reply_markup={"text": "...", "callback": devnull},
        )

        frukt = ["🍒", "🍌", "👑", "🍇", "💩"]
        fruit = random.choice(frukt)
        await message1.edit(f"{fruit}⠀")
        await sleep(1)
        fruit1 = random.choice(frukt)
        await message1.edit(f"<b>{fruit} | {fruit1}</b>")
        await sleep(1)
        fruit2 = random.choice(frukt)
        await message1.edit(f"<b>{fruit} | {fruit1} | {fruit2}</b>")
        win = self.strings("win")
        lose = self.strings("lose")
        jack = self.strings("jackpot")
        poc = self.strings("pocti")
        await sleep(1)

        if (fruit != fruit1) and (fruit != fruit2) and (fruit1 != fruit2):
            await message1.edit(f"{lose}\n      {fruit} | {fruit1} | {fruit2}")

        if fruit == fruit1 and fruit == fruit2 and fruit1 == fruit2:
            await message1.edit(f"{jack}\n      {fruit} | {fruit1} | {fruit2}")

        if (fruit != fruit1) and (fruit1 == fruit2):
            await message1.edit(f"{win}\n      {fruit} | {fruit1} | {fruit2}")

        if (fruit2 != fruit1) and (fruit2 != fruit) and (fruit == fruit1):
            await message1.edit(f"{win}\n      {fruit} | {fruit1} | {fruit2}")

        if (fruit == fruit2) and (fruit1 != fruit) and (fruit1 != fruit2):
            await message1.edit(f"{poc}\n      {fruit} | {fruit1} | {fruit2}")
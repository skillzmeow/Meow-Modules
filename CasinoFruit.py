__version__ = (1, 0, 0)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
# 2022
# meta developer: @skillzmeow

from .. import loader, utils

from asyncio import sleep

import random


from telethon.tl.types import Message


class FruitRouletteMod(loader.Module):
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
            text="<b>кручу барабаны</b>",
            reply_markup={"text": "...", "callback": devnull},
        )

        frukt = ["🍒", "🍌", "👑", "🍇", "🫐"]

        fruit1 = random.choice(frukt)

        await message1.edit(f"{fruit1}⠀")

        await sleep(1)

        fruit2 = random.choice(frukt)

        await message1.edit(f"<b>{fruit1} | {fruit2}</b>")

        await sleep(1)

        fruit3 = random.choice(frukt)

        await message1.edit(f"<b>{fruit1} | {fruit2} | {fruit3}</b>")

        await sleep(1)

        if (fruit1 != fruit2) and (fruit1 != fruit3) and (fruit2 != fruit3):
            await message1.edit(
                f'{self.strings("lose")}\n      {fruit1} | {fruit2} | {fruit3}'
            )

        if (fruit1 == fruit2) and (fruit1 == fruit3) and (fruit2 == fruit3):
            await message1.edit(
                f'{self.strings("jackpot")}\n      {fruit1} | {fruit2} | {fruit3}'
            )

        if (fruit1 != fruit2) and (fruit2 == fruit3):
            await message1.edit(
                f'{self.strings("win")}\n      {fruit1} | {fruit2} | {fruit3}'
            )

        if (fruit3 != fruit2) and (fruit3 != fruit1) and (fruit1 == fruit2):
            await message1.edit(
                f'{self.strings("win")}\n      {fruit1} | {fruit2} | {fruit3}'
            )

        if (fruit1 == fruit3) and (fruit2 != fruit1) and (fruit2 != fruit3):
            await message1.edit(
                f'{self.strings("pocti")}\n      {fruit1} | {fruit2} | {fruit3}'
            )
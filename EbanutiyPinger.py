__version__ = (2,0,0)
#module by:
#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 

#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
#2022

#scope: hikka_only
#meta developer: @skillzmeow

from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import Message
import random

class PingSexMod(loader.Module):
	strings = {
	"name": "EbanutiyPinger", 
	"hui": "Response time",
	"vagina": "Uptime:",
	}
	strings_ru = {
	"hui": "Скорость отклика",
	"vagina": "Прошло с проследней перезагрузки:",
	}
	"""Какой-то тупой модуль"""
	async def pigcmd(self, message:Message):
		"""Наеби своего друга!"""
		hui1 = self.strings("hui")
		vagina1 = self.strings("vagina")
		ebu = random.randint(1, 45000)
		pidr = random.randint(10, 999)
		pis = random.randint(0, 23)
		hiu = random.randint(10, 60)
		sex = random.randint(10, 60)
		await self.animate(
		message,
		[f"<code>🐻 Nofin...</code>"] + [f"⏱ <b>{hui1}</b>: <code>{ebu}.{pidr}</code> <b>ms</b>\n👩‍💼 <b>{vagina1} {pis}:{hiu}:{sex}</b>"],
		interval=0.3,
		inline=False,
	)
	
__version__ = (1,0,0)
#module by:
#  sss   k  k  i l     l     333
# s      k k     l     l        3
# ssss   kk    i l     l      33 
#     s  k k   i l     l        3
# ssss   k  k  i lllll lllll 333

# MEOW, 2022 (лень печатать MEOW)

#scope: hikka_only
#meta developer: @skillzmeow

from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import Message

class FirstInlineMod(loader.Module):
	strings = {
	"name": "InlinePentagon", 
	"hackd": "Pentagon was hacked.✅",
	"hackd1": "🥷🏼Hacking Pentagon\nCondition:",
	}
	strings_ru = {
	"hackd": "<b>Пентагон успешно взломан!✅</b>",
	"hackd1": "🥷🏼Взламываю Пентагон\nСостояние:",
	}
	"""Какой-то тупой модуль"""
	async def ipencmd(self, message:Message):
		"""Стань настоящим хакером!"""
		ebal = self.strings("hackd1")
		await self.animate(
		message,
		[f"<b>{ebal} {x}%</b>" for x in range(0, 100, 5)]
		+ [self.strings("hackd")],
		interval=1,
		inline=True,
	)
	
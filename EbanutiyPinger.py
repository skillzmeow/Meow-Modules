__version__ = (1,0,0)
#module by:
#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 

#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
#2022
from .. import loader, utils
from asyncio import sleep
import random
from telethon.tl.types import Message
#scope: hikka_only
#meta developer: @skillzmeow
@loader.tds
class PingerBlyaMod(loader.Module):
	strings = {"name": "EbanutiyPinger", "pinger": "<b>⏱ Ping:</b>" }
	strings_ru = {"pinger": "<b>⏱ Пинг:</b>"}
	
	async def pigcmd(self, message:Message) -> None:
	    pidor = self.strings("pinger")
	    pig = random.randint(30, 45000)
	    rofl = random.randint(100, 999)
	    await utils.answer(message, "🐻 <code>Bear with us while ping is checking...</code>")
	    await sleep (0.2)
	    await utils.answer(message, f"{pidor} <code>{pig}.{rofl}</code> <b>ms</b>")
	

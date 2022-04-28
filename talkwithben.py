__version__ = (2,0,0)
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

#meta developer: @skillzmeow, @gmdoruzhie
@loader.tds
class BenTalksMod(loader.Module):
	strings = {"name": "TalkWithBen"}
	
	async def bencmd(self, message:Message) -> None:
		"""Разговор с Бэном"""
		ban = ["yes", "no", "ho ho ho..."]
		loll = random.choice(ban)
		args = utils.get_args_raw(message)
		lol = (await utils.answer(message, "<b>Звонок Бэну...</b>"))
		await sleep (2)
		rand = ["1", "1", "Бэн занят"]
		rr = random.choice(rand)
		sex = (await utils.answer(message, "..."))
		if rr == rand[2]:
			await message.edit("<b>🔕Бэн занят, перезвоните позже.</b>")
		else:	
			await message.edit("☎️<b>Внимание! Бэн принял вызов.</b>")
			await sleep (1)
			if not args:
				await message.edit(f"<b>📞Ответ Бэна:\n-{loll}</b>")
			else:
				await message.edit(f"<b>❓Ваш вопрос:\n-{args}\n📞Ответ Бэна:\n-{loll}</b>")
				
		
			

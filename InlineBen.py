__version__ = (6,6,6)
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
#scope: inline
#scope: hikka_only
#meta developer: @skillzmeow
@loader.tds
class BenTalksMod(loader.Module):
	strings = {"name": "InlineBen"}
		
	async def ibencmd(self, message:Message) -> None:
		"""Поговори с Бэном"""
		async def devnull(*args):
			...
		args = utils.get_args_raw(message)
		lol = ["Yes.", "No.", "Ho ho ho..."]
		rand = random.choice(lol)
		fuckwar = await self.inline.form(message=utils.get_chat_id(message), text = "секунду...", reply_markup={"text": "BEN", "callback": devnull})
		await fuckwar.edit("📞 <b>Звоним Бэну...</b>")
		await sleep (1)
		war = ["1", "2", "3"]
		fuck = random.choice(war)
		ebal = ["дрочит", "спит", "ебёт подругу", "хочет уебать тебя тапком", "кинул тебя в чс", "набухался водки и лёг спать", "потерялся в мусорке", "шлепает твою дочку", "в мусарне", "ищет закладку", "вскрывает банку с шпротами", "кушает креветки", "сосет", "устанавливает хикку на хероку", "ждёт октето", "пишет модуль для группового секса", "пишет твоёй телке в PM", "курит кальян", "слушает мурчание твоей мамки в дискорде", "делает новый 🐖Pig Userbot", "взламывает лавхост", "курит на балконе", "помогает Скиллзу копать огород", "упал в гроб при походе на кладбище", "раскидывает распальцовки c Bushido Zho", "курит alpha pvp", "ебет руку", "говнокодит", "играет в майнкрафт", "слушает мияги эндшпиль", "пиздит чужие коды с лицензией", "забыл поставить скобку и фиксит это пол дня"]
		hz = random.choice(ebal)
		if fuck == war[0]:
			await fuckwar.edit(f"📩 <b>Бэн занят, перезвоните позже</b>\n<b>🤷‍♀️ Возможно он {hz}</b>")
		else:
			await fuckwar.edit("☎ <b>Внимание, Бэн принял вызов!</b>")
			await sleep (1)
			if args:	
				await fuckwar.edit(f"<b>Ваш вопрос:</b> <code>{args}</code>\n🧸 <b>Ответ Бэна:</b>\n- {rand}")
			else: await fuckwar.edit(f"🧸 <b>Ответ Бэна:</b>\n- {rand}")
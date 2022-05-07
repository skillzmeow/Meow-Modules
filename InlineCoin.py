__version__ = (1,0,0)
#module by:
#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 

#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
#2022

#scope: hikka_only
#meta developer: @skillzmeow
import logging

from .. import loader, utils
from telethon.tl.types import Message
import random

from ..inline.types import InlineQuery

logger = logging.getLogger(__name__)

class CoinSexMod(loader.Module):
	strings = {"name": "InlineCoin"}

	@loader.inline_everyone
	async def coin_inline_handler(self, query: InlineQuery):
		coin = ["🌚 Выпал орёл!", "🌝 Выпала решка!", "🙀 Чудо, монетка осталась на ребре!", "🌚 Выпал орёл!", "🌚 Выпал орёл!", "🌝 Выпала решка!", "🌝 Выпала решка!"]
		coinrand = random.choice(coin)
		return {
			"title" : "Орёл или решка?", 			"description": "Давай узнаем!",
			"message": f"<b>{coinrand}</b>",  		}
			
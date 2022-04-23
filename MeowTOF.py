""" 
MODULE BY:
S-K-I-L-L-Z    M-E-O-W
my official telegram - t.me/skillzmeow
hey
  """


__version__ = 1,0,2
from .. import loader, utils
import random 
from asyncio import sleep
#meta developers: @skillzmeow, @shadow_hika
@loader.tds
class TruOrFalseMod(loader.Module):
	strings = {"name":"MeowTOF"}
	"Модуль для игры в правду-ложь"
	async def tofcmd(self, msg):
		"""Узнай правда или ложь"""
		args = utils.get_args_raw(msg)
		tril = ["правда", "ложь", "правда", "ложь", "правда", "ложь", "правда", "ложь"]
		trill = random.choice(tril)
		if not args: 
			await msg.edit(f"<b>🔎Узнаём инфу🔍</b>")
			toff = (await msg.client.send_message(msg.to_id, "<b>...</b>"))
			await tofff(toff)
			await sleep (1)
			await msg.delete()
			await toff.delete()
			await msg.client.send_message(msg.to_id, f"<b>🔮Я знаю что это - {trill}🔮</b>")
			await sleep (5)
		else:
			await msg.edit(f"<b>🔎Узнаём инфу по: {args}🔍</b>")
			toff = (await msg.client.send_message(msg.to_id, "<b>...</b>"))
			await tofff(toff)
			await sleep (1)
			await toff.delete()
			await msg.delete()
			await msg.client.send_message(msg.to_id, f"<b>🔮️{args} - {trill}</b>🔮")

async def tofff(msg):
    for x in range(2):
            await msg.edit("<b>Процесс.</b>")
            await sleep (0.4)
            await msg.edit("<b>Процесс..</b>")
            await sleep (0.4)
            await msg.edit("<b>Процесс...</b>")
            await sleep (0.4)

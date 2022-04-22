""" 
MODULE BY:
         __    .__ .__   .__                                             
  ______|  | __|__||  |  |  |  ________  _____    ____    ____  __  _  __
 /  ___/|  |/ /|  ||  |  |  |  \___   / /     \ _/ __ \  /  _ \ \ \/ \/ /
 \___ \ |    < |  ||  |__|  |__ /    / |  Y Y  \\  ___/ (  <_> ) \     / 
/____  >|__|_ \|__||____/|____//_____ \|__|_|  / \___  > \____/   \/\_/  
     \/      \/                      \/      \/      \/                  
MY OFFICIAL TELEGRAM - t.me/skillzmeow
THIS MODULE IS FREE SOFTWARE
YOU CAN EDIT THIS MODULE.
  ____     ___    ____     ____  
 |___ \   / _ \  |___ `\  |___ `\
   __) | | | | |   __) |    __) |
  / __/  | |_| |  / __/    / __/ 
 |_____|  \___/  |_____|  |_____|

"""


__version__ = (1,0,0)
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
		tril = ["ПРАВДА", "ЛОЖЬ", "ПРАВДА", "ЛОЖЬ", "ПРАВДА", "ЛОЖЬ", "ПРАВДА", "ЛОЖЬ"]
		trill = random.choice(tril)
		if not args: 
			await msg.edit(f"<b>🥷🏻Узнаём инфу👇🏿</b>")
			toff = (await msg.client.send_message(msg.to_id, "<b>Процесс...</b>"))
			await toff.edit("<b>ВНИМАНИЕ!</b>")
			await sleep (1)
			await msg.client.send_message(msg.to_id, f"<b>👀Я знаю что это - {trill}👀</b>")
			await sleep (10)
			await toff.delete()
		else:
			await msg.edit(f"<b>🧚🏻‍♀️Узнаём инфу по: {args}👇🏿</b>")
			toff = (await msg.client.send_message(msg.to_id, "<b>Процесс...</b>"))
			await toff.edit("<b>ВНИМАНИЕ!</b>")
			await sleep (1)
			await msg.client.send_message(msg.to_id, f"<b>🦸🏼‍♂️{args} - {trill}</b>🦸🏼‍♂️")
			await sleep (10)
			await toff.delete()
		



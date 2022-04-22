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
from asyncio import sleep
#meta developer: @skillzmeow
@loader.tds 
class NameMod(loader.Module):
	"Модуль хелпер для BFG"
	strings = {'name':'BfgHelper'}
	async def matrcmd(self, msg):
	    """Копание материи"""
	    await msg.delete()
	    await msg.client.send_message(msg.to_id, "Ща покопаем материю, нахуй")
	    await sleep (2)
	    for _ in range (30):
	        msgg = (await msg.client.send_message(msg.to_id, "Копать материю"))
	        await sleep (1)
	        await msgg.edit("😺я котик😺")
	        await sleep (4)
	    await msg.client.send_message(msg.to_id, "мяу мяу, я пошел.")
	
	async def bchcmd(self, msg):
	    """Модуль для проверки зарплаты"""
	    await msg.delete()
	    await sleep (2)
	    business = ["Мой бизнес", "Мой генератор", "Мой сад", "Моя ферма"]
	    sleeplist = [3, 3, 3, 3, 0]
	    for x in business:
	        for i in sleeplist:
	            await msg.client.send_message(msg.to_id, (str(x)))
	            await sleep (i)
	            break 
	    await msg.client.send_message(msg.to_id, "😺муур мур, котики богатые😺")
	
	async def cascmd(self, msg):
	    """Игра в казик"""
	    await msg.delete()
	    ggg = (await msg.client.send_message(msg.to_id, "Котики выиграют бабок"))
	    await sleep (2)
	    await ggg.edit("Мур")
	    await sleep (2)
	    casino = ("Казино")
	    caslist = ['777ккк', '888ккк', '777ккк', '888ккк', '777ккк', '888ккк', '777ккк', '888ккк', '777ккк']
	    for x in range(len(caslist)):
	        for i in caslist:
	            sex = (await msg.client.send_message(msg.to_id, f"{casino} {str(i)}"))
	            await sleep (2)
	            await sex.edit("😺го х10😺")
	            await sleep (3)
	            break
	    await msg.client.send_message(msg.to_id, "пока")

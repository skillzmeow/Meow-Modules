from .. import loader, utils
from asyncio import sleep

@loader.tds 
class NameMod(loader.Module):
	"Модуль для копания материи"
	strings = {'name':'Bfg Helper'}
	async def matericmd(self, msg):
	    await msg.client.send_message(msg.to_id, "Ща покопаем материю, нахуй")
	    for _ in range (11):
	        msgg = (await msg.client.send_message(msg.to_id, "Копать материю"))
	        await sleep (1)
	        await msgg.edit("Я свинота")
	        await sleep (4)
	    await msg.client.send_message(msg.to_id, "А теперь - идите на хуй. И не просить у меня денег.")
	async def bchcmd(self, msg):
	    """Модуль для проверки зарплаты"""
	    business = ["Мой бизнес", "Мой генератор", "Мой сад", "Моя ферма"]
	    sleeplist = [3, 3, 3, 0]
    	    for x in business:
	        for i in sleeplist:
	            await msg.client.send_message(msg.to_id,(str(x)))
	            await sleep (i)
                    break 
	    await msg.client.send_message(msg.to_id, "Увидел дохуя денег? Можешь даже не просить у меня их.")

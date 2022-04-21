from .. import loader, utils
from asyncio import sleep

@loader.tds 
class NameMod(loader.Module):
	"Upd со списками мазефака by @skillzmew и @Y4sperMaglot"
	strings = {'name':'MeowMagicUPD'}
	async def client_ready(self, client, db):
		self.client = client 
	async def meowcmd(self, msg):
		"""Котоатака (спам 15месседжей)"""
		await msg.delete()
		sss = ['Мяуууу, пакажу тебе магию', 'Готова?', '3', '2', '1', 'КОТИКО АТАКААА ТВОЮ МАТЬ']
		sleeplist = [3, 3, 1, 1, 1, 0]
		for x in sss:
			for i in sleeplist:
				await msg.client.send_message(msg.to_id, (str(x)))
				await sleep(i)
				break 
		for x in range(15):
			await msg.client.send_message(msg.to_id, "😻МЯУУУ, КОТИКИ😸")
			await sleep (0.2)
		await msg.client.send_message(msg.to_id, "Module by @skillzmeow, это вам не ебанные ")

	async def flycmd(self, msg):
		"""Маленький отрывок из песни"""
		await msg.delete()
		sss = ['Так много парней...😻', 'Тебе так часто пишуут😻', 'Я могу всё это терпеть...😻', 'Но я это ненавижууу😻', 'Скажи, какой мне интерееес...😻','Встречаться с серой мышью😻', 'Если отправлюсь на тот свееет...😻', 'Меня вдруг все услышат😻', 'ДЕТКАААА, отправимся в полееет...😻', 'Бери бонг!😻', 'Когда ты смотришь горячо — меня влечёт😻', 'Если я влюблюсь глубоко - то я обречён😻', 'На мне столько колец, будто десять раз обручён😻', 'Полёт, Josodo part. Module by @skillzmeow']
		sleeplist = [4, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 5, 0]
		for x in sss: 
			for i in sleeplist:
				await msg.client.send_message(msg.to_id, (str(x)))
				await sleep(i)
				break

	async def zxccmd(self, msg):
		"""Ебануто продуманый модуль, не спам 1000-7"""
		await msg.edit("Я так соскучился...")
		await sleep(1)
		magaz = (await msg.client.send_message(msg.to_id, "Что делаешь?")) 
		await sleep(1)
		await magaz.edit("Ладно...")
		await sleep(2)
		await magaz.edit("Не буду мешать...")
		sound = (await msg.client.send_message(msg.to_id, "ЗАГРУЗКА ПЕСНИ НАХУЙ")) 
		await sleep (0.4)
		await meowww(sound)	
		await sleep(3)
		spisok = ["ZXC, забираешь мою душу...", "Почему ты режешь вдоль?", "Поперёк же было б лучше...", "ZXC, я разбитый как канеки...", "Твоё тело остывает, попрощаемся наве-е-ки..."]
		s = (await msg.client.send_message(msg.to_id, "аааа")) 
		for x in range(len(spisok)):
			await s.edit(str(x + 1) + "💙" +  str(spisok[x]))
			await sleep(3)
		await msg.client.send_message(msg.to_id, "Module by @Y4sperMaglot, реально ахуенный чувак")
			

async def meowww(msg): 	#вспомогательная функция для моего .zxc 
	number = 0
	while number <= 100:
		await msg.edit(f"ЗАРУЗКА ПЕСНИ {str(number)}%")
		number += 5
		await sleep(0.1)
	await msg.edit("ПЕСНЯ ЗАГРУЖЕНА")
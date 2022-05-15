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
import time
import datetime

class MyTimeMod(loader.Module):
    strings = {
        "name": "MyTime",
        "time": "⏳ <b>Accuracy time:</b> <code>{}</code>",
        "datetime": "📆 <b>Date:</b> <code>{}</code>\n⏳ <b>Accuracy time:</b> <code>{}</code>\n{} <code>{} days, {} hours, {} min</code>",
        }
    strings_ru = {
        "name": "MyTime",
        "time": "⏳ <b>Точное время:</b> <code>{}</code>",
        "datetime": "📆 <b>Дата:</b> <code>{}</code>\n⏳ <b>Точное время:</b> <code>{}</code>\n{} <code>{} дней, {} часа, {} мин</code>",
        }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "year",
                "2023",
                lambda: "Укажите год (пример - 2022)"
                ),
            loader.ConfigValue(
                "month",
                "1",
                lambda: "Укажите месяц (пример - 1 или 10, без 0)"
                ),
            loader.ConfigValue(
                "day",
                "1",
                lambda: "Введите день месяца"
                ),
            loader.ConfigValue(
                "datetext",
                "<b>До нового года осталось:</b>",
                lambda: "Укажите текст для для вашей даты (<b>До моего дня рождения осталось:</b>, <code>, <i> и т.д.)"),
            )
    
    @loader.unrestricted
    async def datecmd(self, message: Message):
        """Текущая дата и время"""
        year = int(self.config["year"])
        month = int(self.config["month"])
        day = int(self.config["day"])
        dt = datetime.datetime.now()
        date = dt.strftime("%x")
        time = dt.strftime("%H:%M:%S")
        now = datetime.datetime.today()
        NY = datetime.datetime(year, month, day)
        d = NY - now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        await self.inline.form(message=message, text=self.strings("datetime").format(
                date,
                time,
                self.config["datetext"],
                d.days,
                hh,
                mm,
                )
            )
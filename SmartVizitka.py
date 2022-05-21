__version__ = (2,0,0)

#module by:

#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 


#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀

# you can edit this module

#2022


from .. import loader, utils, main

from telethon.tl.types import Message


class MyInformationMod(loader.Module):

    strings = {"name": "SmartVizitka"}

    def __init__(self):

        self.config = loader.ModuleConfig(

            loader.ConfigValue(

                "message",

                "<b>I don't know where me.</b>",

                lambda: "Your custom message to business card"),

            loader.ConfigValue(

                "button",

                "🕊my best modules🕊|https://t.me/smeowcodes",

                lambda: "Your_text|https://link.com"

                ),

                loader.ConfigValue(

                    "photo_url",

                    "https://imgur.com/a/sxwTg25",

                    lambda: "Your photo url",

                ),

            )
      
    def _get_mark(self):

        return (

            None

            if not self.config["button"]

            else {

                "text": self.config["button"].split("|")[0],

                "url": self.config["button"].split("|")[1],

                }

            )
            
    @loader.unrestricted

    async def vizcmd(self, message: Message):

    	await self.inline.form(

            message=message,

            text = self.config["message"],

            reply_markup=self._get_mark(),

    		**(

    			{"photo": self.config["photo_url"]}

    		),

        )
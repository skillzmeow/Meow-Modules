__version__ = (2,0,0)
#module by:
#█▀ █▄▀ █ █░░ █░░ ▀█ 
#▄█ █░█ █ █▄▄ █▄▄ █▄ 

#█▀▄▀█ █▀▀ █▀█ █░█░█
#█░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
#2022

#scope: hikka_only
#meta developer: @skillzmeow

from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import Message

import logging

logger = logging.getLogger(__name__)

@loader.tds
class InlineSmilesMod(loader.Module):
    strings = {"name": "MagicSmilesInline"}
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue("dick", "👨‍🦲", lambda: "смайл для вашего пениса"),
            loader.ConfigValue("golovka", "👷", lambda: "смайл для головки пениса"),
            loader.ConfigValue("sperma", "💎",lambda: "жидкость члена"),
            loader.ConfigValue("police1", "🟡", lambda: "левая сторона мигалки"),
            loader.ConfigValue("police2", "🔵", lambda: "правая сторона мигалки")
            )
    async def heartscmd(self, message:Message):
        async def devnull(*args):
            ...
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>сердечки🥰</b>", reply_markup={"text": "...", "callback": devnull})
        for _ in range(10):
            for heart in ["❤", "🤎", "💛", "💚", "🤍", "💜"]:
                await msg.edit(heart)
                await sleep (1)

    async def moonscmd(self, message:Message):
        async def devnull(*args):
            ...
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>ты моя луна, я вою на луну👉👈</b>", reply_markup={"text": "...", "callback": devnull})
        for _ in range(10):
            for moon in ["🌝", "🌚"]:
                await msg.edit(moon)
                await sleep(1)

    async def moons2cmd(self, message:Message):
        async def devnull(*args):
            ...
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>ты моя луна, я вою на луну👉👈</b>", reply_markup={"text": "...", "callback": devnull})
        for _ in range(10):
            for moon2 in ["🌕", "🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔"]:
                await msg.edit(moon2)
                await sleep(1)

    async def clockscmd(self, message:Message):
        async def devnull(*args):
            ...
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>дзень дзелень</b>", reply_markup={"text": "...", "callback": devnull})
        for _ in range(12):
            for clock in ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]:
                await msg.edit(clock)
                await sleep(1)

    async def policecmd(self, message:Message):
        async def devnull(*args):
            ...
        m = self.config["police1"]
        n = self.config["police2"]
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>за нами едут палицаи</b>", reply_markup={"text": "...", "callback": devnull})
        for x in range(10):
            await msg.edit(f"{m}{m}{m}{m}⬜️⬜️⬜️{n}{n}{n}{n}\n{m}{m}{m}{m}⬜️⬜️⬜️{n}{n}{n}{n}\n{m}{m}{m}{m}⬜️⬜️⬜️{n}{n}{n}{n}")
            await sleep (1)
            await msg.edit(f"{n}{n}{n}{n}⬜️⬜️⬜️{m}{m}{m}{m}\n{n}{n}{n}{n}⬜️⬜️⬜️{m}{m}{m}{m}\n{n}{n}{n}{n}⬜️⬜️⬜️{m}{m}{m}{m}")
            await sleep (1)

    @loader.unrestricted
    async def dickcmd(self, message:Message):
        async def devnull(*args):
            ...
        d = self.config["dick"]
        g = self.config["golovka"]
        s = self.config["sperma"]
        msg = await self.inline.form(message=utils.get_chat_id(message), text = "<b>мой пиструн хочет секса</b>", reply_markup={"text": "...", "callback": devnull})
        await msg.edit(
            f"\u2060      {s}\n{g}{g}{g}\n{d}{d}{d}\n  {d}{d}{d}\n    {d}{d}{d}\n     {d}{d}{d}\n       {d}{d}{d}\n        {d}{d}{d}\n         {d}{d}{d}\n          {d}{d}{d}\n          {d}{d}{d}\n      {d}{d}{d}{d}\n {d}{d}{d}{d}{d}{d}\n {d}{d}{d}  {d}{d}{d}\n    {d}{d}       {d}{d}"
        )
        await sleep(1)
        await msg.edit(
            f"\u2060    {s}\n      {s}\n{g}{g}{g}\n{d}{d}{d}\n  {d}{d}{d}\n    {d}{d}{d}\n     {d}{d}{d}\n       {d}{d}{d}\n        {d}{d}{d}\n         {d}{d}{d}\n          {d}{d}{d}\n          {d}{d}{d}\n      {d}{d}{d}{d}\n {d}{d}{d}{d}{d}{d}\n {d}{d}{d}  {d}{d}{d}\n    {d}{d}       {d}{d}"
        )
        await sleep(1)
        await msg.edit(
            f"\u2060  {s}\n    {s}\n      {s}\n{g}{g}{g}\n{d}{d}{d}\n  {d}{d}{d}\n    {d}{d}{d}\n     "
            f"{d}{d}{d}\n       {d}{d}{d}\n        {d}{d}{d}\n         {d}{d}{d}\n          {d}{d}{d}\n          {d}{d}{d}\n      {d}{d}{d}{d}\n {d}{d}{d}{d}{d}{d}\n {d}{d}{d}  {d}{d}{d}\n    {d}{d}       {d}{d}"
        )
        await sleep(1)
        await msg.edit(
            f"\u2060{s}\n  {s}\n    {s}\n      {s}\n{g}{g}{g}\n{d}{d}{d}\n  {d}{d}{d}\n    "
            f"{d}{d}{d}\n     {d}{d}{d}\n       {d}{d}{d}\n        {d}{d}{d}\n         {d}{d}{d}\n          {d}{d}{d}\n          {d}{d}{d}\n      {d}{d}{d}{d}\n {d}{d}{d}{d}{d}{d}\n {d}{d}{d}  {d}{d}{d}\n    {d}{d}       {d}{d}"
        )
        await sleep(1)
        await msg.edit(
            f"\u2060{s}{s}\n{s}\n{s}\n  {s}\n    {s}\n      {s}\n{g}{g}{g}\n{d}{d}{d}\n  {d}{d}{d}\n    "
            f"{d}{d}{d}\n     {d}{d}{d}\n       {d}{d}{d}\n        {d}{d}{d}\n         {d}{d}{d}\n          {d}{d}{d}\n          {d}{d}{d}\n      {d}{d}{d}{d}\n {d}{d}{d}{d}{d}{d}\n {d}{d}{d}  {d}{d}{d}\n    {d}{d}       {d}{d}"
        )
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import asyncio
import lib.dpy_interaction_ui as dpyui

class setting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.ui=bot.ui

    @commands.command(name="setup")
    async def setup_cmd(self, ctx):
        ui = dpyui.interaction_menu("setup_menu", "初期設定はこちらから。", 1, 2)
        ui.add_option("メンションスパム","mentionspam","メンションスパム時の動作についての設定を行います。")
        ui.add_option("URLスパム","urlspam","URLスパム時の設定を行います。")
        msg = await self.bot.ui.send_with_ui(ctx.channel, f"> 初期設定",ui=ui)
        cb = await self.bot.wait_for("menu_select", check=lambda icb:icb.custom_id=="setup_menu" and icb.message.id==msg.id and icb.clicker_id == ctx.author.id)
        send_text = ""
        if "mentionspam" in cb.selected_value:
            send_text += f"> メンションスパム"
        if "urlspam" in cb.selected_value:
            send_text += f"> URLスパム"
        await cb.edit_with_ui(content=send_text, ui=[])

def setup(bot):
    bot.add_cog(setting(bot))
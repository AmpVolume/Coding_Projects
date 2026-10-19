import discord
from discord.ext import commands

# Multiple prefixes
COMMAND_PREFIXES = ["ulb.", "🛡️", "g!", "-", "'", "="]

def register_commands(bot):
    # ----------------- HELP COMMAND -----------------
    @bot.command(name="help", help="Shows this help message.")
    async def help_command(ctx):
        # Only respond to -help
        if not ctx.message.content.startswith("-help"):
            return

        embed = discord.Embed(
            title="🛡️ ULB Bot Commands",
            description="Use the prefixs to run commands. Pick a command to learn more!",
            color=discord.Color.blue()
        )

        # Dynamically list all commands
        for command in bot.commands:
            if command.hidden:
                continue
            # Show only the command name (no prefix)
            embed.add_field(
                name=f"-{command.name}",
                value=command.help or "No description provided.",
                inline=False
            )

        await ctx.send(embed=embed)
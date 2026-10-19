import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from Python.ULB.commands import register_commands
from Python.ULB.notify import setup_ulb  # <-- IMPORT YOUR TASK

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 🔴 SET YOUR CHANNEL ID HERE
CHANNEL_ID = 1486566913550057605

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Multiple prefixes
COMMAND_PREFIXES = ["ulb.", "🛡️", "g!", "-", "'", "="]

# Create bot
bot = commands.Bot(
    command_prefix=COMMAND_PREFIXES,
    intents=intents,
    help_command=None
)

# Register commands
register_commands(bot)

# 🔥 SETUP THE ULB TASK
ulb_task = setup_ulb(bot, CHANNEL_ID)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    
    # Start the task ONLY once
    if not ulb_task.is_running():
        ulb_task.start()

# Run the bot
bot.run(TOKEN)
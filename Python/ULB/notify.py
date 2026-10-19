from discord.ext import tasks
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Python 3.9+

# Timezone (handles DST automatically)
EST = ZoneInfo("America/New_York")

# Schedule A (EST times)
GUILD_BATTLE_TIMES = [
    {"name": "Match One", "time": "14:00"},
    {"name": "Match Two", "time": "19:00"},
    {"name": "Match Three", "time": "22:00"},
]

last_sent = set()

def setup_ulb(bot, channel_id):

    @tasks.loop(seconds=30)
    async def check_times():
        global last_sent

        now = datetime.now(EST)
        now_str = now.strftime("%H:%M")

        channel = bot.get_channel(channel_id)
        if not channel:
            return

        for match in GUILD_BATTLE_TIMES:
            name = match["name"]
            battle_time_str = match["time"]

            # Convert string → datetime (today, EST)
            battle_time = datetime.strptime(battle_time_str, "%H:%M").replace(
                year=now.year,
                month=now.month,
                day=now.day,
                tzinfo=EST
            )

            # 5-minute warning
            warning_time = (battle_time - timedelta(minutes=5)).strftime("%H:%M")

            # ⚠️ 5-minute warning
            if now_str == warning_time and f"warn_{battle_time_str}" not in last_sent:
                await channel.send(
                    f"⚠️ @everyone {name} starts in 5 minutes! Get ready!"
                )
                last_sent.add(f"warn_{battle_time_str}")

            # ⚔️ battle start
            if now_str == battle_time_str and f"start_{battle_time_str}" not in last_sent:
                await channel.send(
                    f"⚔️ @everyone {name} is starting now!"
                )
                last_sent.add(f"start_{battle_time_str}")

        # Reset daily
        if now_str == "00:00":
            last_sent.clear()

    return check_times
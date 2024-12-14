import discord
from discord import app_commands
import random
import string
import asyncio

class NitroBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = NitroBot()

@client.event
async def on_ready():
    print(f'Bot is ready! Logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="/help"))

@client.tree.command(name="ping", description="Check bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! 🏓 Latency: {round(client.latency * 1000)}ms")

@client.tree.command(name="gen", description="Generate fake Discord Nitro codes")
async def gen(interaction: discord.Interaction, amount: int):
    if amount > 10:
        await interaction.response.send_message("Maximum generation limit is 10 codes!")
        return
    
    await interaction.response.send_message("🎮 Generating Nitro codes...")
    
    codes = []
    for _ in range(amount):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        codes.append(f"https://discord.gift/{code}")
        await asyncio.sleep(0.5)  # Add small delay for effect
    
    formatted_codes = "\n".join(codes)
    embed = discord.Embed(
        title="🎉 Generated Nitro Codes",
        description=f"```{formatted_codes}```",
        color=discord.Color.purple()
    )
    embed.set_footer(text="Note: These are fake codes for entertainment purposes only!")
    
    await interaction.edit_original_response(content="", embed=embed)

@client.tree.command(name="help", description="Show all available commands")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 Bot Commands",
        description="Here are all available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(name="/ping", value="Check bot's latency", inline=False)
    embed.add_field(name="/gen [amount]", value="Generate fake Nitro codes", inline=False)
    embed.add_field(name="/help", value="Show this help message", inline=False)
    
    await interaction.response.send_message(embed=embed)

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
TOKEN = 'MTMxNzM5NDEwODU0NDg0Nzk1NQ.GAi1kk.dDyw6uBgT1W1_OSz7D6UpgaZ2mOlTh9fcvxAzU'
client.run(TOKEN)

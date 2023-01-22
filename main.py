from disnake.ext import commands
from dotenv import load_dotenv
import disnake
import os

load_dotenv()

intents = disnake.Intents.default()
bot = commands.InteractionBot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged as {bot.user} (ID: {bot.user.id})")


@bot.slash_command(
    name="ping",
    description="Pong"
)
async def ping(inter: disnake.ApplicationCommandInteraction):
    await inter.response.send_message("Pong!")


@bot.slash_command(
    name="say",
    description="Sends a message",
    options=[disnake.Option(name="message",
                            description="Message to send",
                            type=disnake.OptionType.string,
                            required=True)]
)
async def say(inter: disnake.ApplicationCommandInteraction,
              message: str):
    # Responds to interaction
    await inter.response.defer(ephemeral=True)

    # Sends a message in channel
    await inter.channel.send(message)
    
    # Sends a message in response to an interaction
    await inter.edit_original_response("Done")


if __name__ == "__main__":
    bot.run(os.getenv("BOT_TOKEN"))
    

from typing import Optional
import discord
import Levenshtein
from discord.interactions import Interaction
from data import GameGarden
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os



bot = commands.Bot(command_prefix="!", description="test waqim", intents=discord.Intents.all())

embed = None

def LEV(similar_word, parental_word, magnitude):
    distance = Levenshtein.distance(similar_word, parental_word)
    similar = 1 - (distance / max(len(similar_word), len(parental_word)))
    return similar >= magnitude

def GameSelector(nameofgame):

    pass


@bot.event
async def on_ready():
    print("OK !!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

class GameGardenModal(discord.ui.Modal, title="Chercher votre jeux"):
    nomdujeux = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Nom du jeux",
        required=True,
        placeholder="Diablo IV")

    async def on_submit(self, interaction: Interaction):
                
        nameofgame = self.nomdujeux.value

        print(nameofgame)

        nameofgame = nameofgame.replace(" ", "")
        nameofgame = nameofgame.lower()

        if LEV(nameofgame, "gettingoverit", 0.6):
            embed =  GameGarden.GOI
        if LEV(nameofgame, "fnaf1", 0.6):
            embed = GameGarden.FNAF
        if LEV(nameofgame, "satisfactory", 0.6):
            embed = GameGarden.SARY
        if LEV(nameofgame, "dokidokilittératureclubplus", 0.6):
            embed = GameGarden.DDLCP
        if LEV(nameofgame, "dokidoki", 0.6):
            embed = GameGarden.DDLCP
        if LEV(nameofgame, "devour", 0.6):
            embed = GameGarden.DEVOUR
        if LEV(nameofgame, "diablo4", 0.6):
            embed = GameGarden.DIA4
        if LEV(nameofgame, "diabloiv", 0.6):
            embed = GameGarden.DIA4
        if LEV(nameofgame, "darksoulsremastered", 0.6):
                embed = GameGarden.DSREM
        print(embed.title)

        await interaction.response.send_message(embed = embed, ephemeral=True)

      

@bot.tree.command(name="search", description="Type this command with a name of a game to search it")
async def embed(interaction: discord.Interaction):
    game_modal = GameGardenModal()
    await interaction.response.send_modal(game_modal)


@bot.tree.command(name="annonce")
@discord.app_commands.describe(nameofthegame="The name of the annonce game")
async def message_annonce(interaction: discord.Interaction, nameofthegame:str, imageurl:str):
    allowed_mentions = discord.AllowedMentions(everyone = True)
    annonce = discord.Embed(title="Un nouveau jeux débarque sur GameGarden !")
    annonce.set_image(url=imageurl)
    annonce.add_field(name="Salut tout le monde !,\n Le crack de " + nameofthegame + " est enfin disponible !!! \n Vous pouvez le télécharger dans le salon #bot-crack", value="")
    await interaction.response.send_message(content="@everyone", allowed_mentions = allowed_mentions, embed=annonce)
    

@bot.tree.command(name="description", description="The test of this embed")
async def discord_fivver(interaction: discord.Interaction):
    await interaction.response.send_message(embed=GameGarden.FVER)

load_dotenv()

bot.run(os.getenv('discord_apikey'))
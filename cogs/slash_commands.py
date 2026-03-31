import discord
from discord.ext import commands

class SlashCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tableau = []
        self.setup_complete = False
    """
    @discord.app_commands.command(name="setup_table", description="Initialiser le tableau avec des colonnes")
    async def setup_table(self, interaction: discord.Interaction, colonnes: str):
        self.tableau.append(colonnes.split(","))
        self.setup_complete = True
        await interaction.response.send_message(f"Tableau initialisé avec les colonnes : {colonnes}", ephemeral=True)
    
    @discord.app_commands.command(name="add_row", description="Ajouter une ligne au tableau")
    async def add_row(self, interaction: discord.Interaction, ligne: str):
        if not self.setup_complete:
            await interaction.response.send_message("Le tableau n'est pas encore configuré. Utilisez d'abord la commande /setup_table.", ephemeral=True)
            return
        
        self.tableau.append(ligne.split(","))
        tableau_str = "\n".join(["\t".join(row) for row in self.tableau])
        await interaction.response.send_message(f"Tableau mis à jour :\n```\n{tableau_str}\n```", ephemeral=True)

    @discord.app_commands.command(name="show_table", description="Afficher le tableau")
    async def show_table(self, interaction: discord.Interaction):
        if not self.tableau:
            await interaction.response.send_message("Le tableau est vide. Utilisez d'abord la commande /setup_table pour le configurer.", ephemeral=True)
            return
        
        tableau_str = "\n".join(["\t".join(row) for row in self.tableau])
        await interaction.response.send_message(f"Voici votre tableau :\n```\n{tableau_str}\n```", ephemeral=True)
        """
async def setup(bot):
    await bot.add_cog(SlashCommandsCog(bot))
from discord.ext import commands
import asyncio

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tableau = []
        self.setup_complete = False
    """
    @commands.command(name="setup_table")
    async def setup_table(self, ctx, *, colonnes: str):
        self.tableau.append(colonnes.split(","))
        self.setup_complete = True
        await ctx.send(f"Tableau initialisé avec les colonnes : {colonnes}")
    
    @commands.command(name="add_row")
    async def add_row(self, ctx, *, ligne: str):
        if not self.setup_complete:
            await ctx.send("Le tableau n'est pas encore configuré. Utilisez d'abord la commande !setup_table.")
            return
        
        self.tableau.append(ligne.split(","))
        tableau_str = "\n".join(["\t".join(row) for row in self.tableau])
        await ctx.send(f"Tableau mis à jour :\n```\n{tableau_str}\n```")

    @commands.command(name="show_table")
    async def show_table(self, ctx):
        if not self.tableau:
            await ctx.send("Le tableau est vide. Utilisez d'abord la commande !setup_table pour le configurer.")
            return
        
        tableau_str = "\n".join(["\t".join(row) for row in self.tableau])
        await ctx.send(f"Voici votre tableau :\n```\n{tableau_str}\n```")
    """
    
    @commands.command()
    async def commande(self,context):
        await context.send("- Voici toutes les commandes avec lesquelles je suis capable d'interagir :\n   - !bonjour --> Je réponds \"Salut !\"\n   - !ping --> Je réponds \"Pong !\"\n   - !pong --> Je réponds \"Tu as oublié \"Ping\" avant !\"\n   - repete n msg --> Je répète n fois le message \"msg\"\n   - !addition n1 n2 --> Je donne le résultat de l'addition de \"n1\" et de \"n2\"\n- D'autres sont à venir…")

    @commands.command()
    async def ping(self,context):
        await context.send("Pong !")

    @commands.command()
    async def repete(self,context,nb,*,msg):
        try:
            nb = int(nb)
            for i in range(1,nb+1):
                await context.send(f"{i}. {msg}")
                asyncio.sleep(0.5)
        except Exception as e:
            print(e)

    @commands.command()
    async def pong(self,context):
        await context.send("Tu as oublié \"Ping\" avant !")
    
    @commands.command()
    async def bonjour(self,context):
        await context.send("Salut !")

    @commands.command()
    async def hell_nah(self,context):
        await context.send("Hell YEAH!")
    
    @commands.command()
    async def addition(self,context,n1=None,n2=None):
        if n1 == None or n2 == None:
            await context.send("Tu n'as pas précisé tous les nombres !")
        else:
            try:
                n1,n2 = int(n1),int(n2)
                await context.send(f"{n1} + {n2} = {n1+n2} !\nSimple non ?")
            except Exception as e:
                await context.send("Erreur ! Réessaie...")
                print(e)

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))
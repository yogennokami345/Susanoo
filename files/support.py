import discord
from discord import app_commands
from discord.ext import commands

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="helpme", description="Exibe informações de ajuda e como obter suporte no servidor.")
    async def helpme(self, interaction: discord.Interaction):
        """Comando de barra /helpme. Exibe opções de suporte."""
        embed = discord.Embed(
            title="💡 Central de Ajuda do Servidor",
            description="Olá! Precisa de ajuda? Aqui estão algumas formas de obter suporte:",
            color=discord.Color.from_rgb(52, 152, 219) # Azul vibrante
        )
        embed.add_field(name="❓ Perguntas Frequentes (FAQ)", 
                        value="Use `/faq` para encontrar respostas rápidas para as dúvidas mais comuns.", 
                        inline=False)
        embed.add_field(name="🎫 Abrir um Ticket de Suporte", 
                        value="Procure pelo canal de tickets (ex: `#abrir-ticket`) para criar um chamado e falar com a equipe.", 
                        inline=False)
        embed.add_field(name="🗣️ Falar com a Equipe Diretamente", 
                        value="Se a situação for urgente, mencione um membro da equipe de suporte (ex: `@Moderador`, `@Admin`).", 
                        inline=False)
        embed.set_footer(text=f"Bot desenvolvido por {self.bot.user.name} | Estamos aqui para ajudar!")
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        
        await interaction.response.send_message(embed=embed, ephemeral=True) # ephemeral=True para que só o usuário veja

    @app_commands.command(name="faq", description="Exibe uma lista de perguntas frequentes do servidor.")
    async def faq(self, interaction: discord.Interaction):
        """Comando de barra /faq. Exibe a lista de FAQs."""
        embed = discord.Embed(
            title="📚 Perguntas Frequentes (FAQ) do Servidor",
            description="Encontre respostas para as perguntas mais comuns aqui:",
            color=discord.Color.from_rgb(46, 204, 113) # Verde esmeralda
        )
        embed.add_field(name="1. Como faço para me verificar?", 
                        value="R: Visite o canal `#verificação` e siga as instruções para ter acesso total ao servidor.", 
                        inline=False)
        embed.add_field(name="2. Posso divulgar meu servidor/conteúdo?", 
                        value="R: Apenas em canais específicos como `#parcerias` ou `#divulgação`, e sempre respeitando as regras do servidor.", 
                        inline=False)
        embed.add_field(name="3. Como entro em contato com a equipe de moderação?", 
                        value="R: Use o sistema de tickets ou mencione um membro da equipe (ex: `@Moderação`) em um canal apropriado.", 
                        inline=False)
        embed.add_field(name="4. Onde posso encontrar as regras do servidor?", 
                        value="R: As regras completas estão disponíveis no canal `#regras`.", 
                        inline=False)
        embed.set_footer(text=f"Bot desenvolvido por {self.bot.user.name} | Sua dúvida não está aqui? Use /helpme.")
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="ping", description="Verifica a latência do bot.")
    async def ping(self, interaction: discord.Interaction):
        """Comando de barra /ping. Mostra a latência do bot."""
        latency_ms = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Minha latência é de **{latency_ms}ms**.",
            color=discord.Color.from_rgb(241, 196, 15) # Amarelo
        )
        embed.set_footer(text=f"Bot desenvolvido por {self.bot.user.name}")
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Support(bot))


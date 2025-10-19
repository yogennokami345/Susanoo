import os
import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask
from threading import Thread

# Configuração do Flask para manter o bot online
app = Flask('')

@app.route('/')
def home():
    return "Bot do Discord está online!"

def run_flask_server():
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

# Configuração do Bot do Discord
# Intenções necessárias para o bot funcionar corretamente
intents = discord.Intents.default()
intents.message_content = True  # Permite que o bot leia o conteúdo das mensagens
intents.members = True # Necessário para algumas funcionalidades, como obter membros

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('/'), intents=intents)
        self.initial_extensions = ['cogs.support'] # Caminho para o cog

    async def setup_hook(self):
        for ext in self.initial_extensions:
            try:
                await self.load_extension(ext)
                print(f"Cog {ext} carregado com sucesso.")
            except Exception as e:
                print(f"Falha ao carregar cog {ext}: {e}")
        await self.tree.sync() # Sincroniza os comandos de barra
        print(f'Comandos de barra sincronizados para {self.user.name}')

    async def on_ready(self):
        print(f'Bot conectado como {self.user} (ID: {self.user.id})')
        print('------')

# Inicializa o bot
bot = MyBot()

# Inicia o servidor Flask em uma thread separada
def start_flask_thread():
    t = Thread(target=run_flask_server)
    t.daemon = True
    t.start()

if __name__ == '__main__':
    start_flask_thread()
    # Obtém o token do Discord das variáveis de ambiente
    discord_token = os.environ.get('DISCORD_TOKEN')
    if discord_token is None:
        print("Erro: A variável de ambiente 'DISCORD_TOKEN' não está configurada.")
        print("Por favor, defina seu token do bot do Discord nas variáveis de ambiente do Replit.")
    else:
        bot.run(discord_token)


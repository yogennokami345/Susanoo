# Guia para Hospedar seu Bot do Discord no Replit (24/7)

Este guia detalha como configurar seu bot do Discord no Replit, garantindo que ele permaneça online 24 horas por dia, 7 dias por semana, utilizando um servidor web Flask para o recurso de "keep-alive" e o UptimeRobot.

## 1. Estrutura do Projeto

Você deve organizar seu projeto no Replit com a seguinte estrutura de arquivos:

```
.replit
replit.nix
requirements.txt
main.py
cogs/
└── support.py
```

### `main.py`
Este é o arquivo principal que inicializa o bot do Discord e o servidor web Flask. Ele carrega os cogs (extensões) e gerencia a execução do bot.

### `cogs/support.py`
Este arquivo contém os comandos de suporte (`/helpme`, `/faq`, `/ping`) do seu bot, organizados como um cog. Cogs ajudam a modularizar o código do seu bot.

### `requirements.txt`
Lista as dependências Python necessárias para o seu projeto. O Replit as instalará automaticamente.

```
discord.py
Flask
```

### `.replit`
Este arquivo configura como o Replit deve executar seu projeto. Ele define o comando de execução e as dependências do sistema.

### `replit.nix`
Especifica as dependências do sistema operacional usando o gerenciador de pacotes Nix, garantindo que as bibliotecas necessárias estejam disponíveis no ambiente do Replit.

## 2. Configuração no Replit

Siga os passos abaixo para configurar seu projeto no Replit:

1.  **Crie um novo Repl:**
    *   Vá para [Replit](https://replit.com/) e faça login.
    *   Clique em `+ Create Repl`.
    *   Selecione `Python` como template.
    *   Dê um nome ao seu Repl (ex: `MeuBotDiscord`).
    *   Clique em `Create Repl`.

2.  **Transfira os arquivos:**
    *   No editor do Replit, você verá um arquivo `main.py` padrão. Apague o conteúdo dele e cole o conteúdo do `main.py` fornecido.
    *   Crie uma nova pasta chamada `cogs` (clique nos três pontos ao lado de `Files` -> `New Folder`).
    *   Dentro da pasta `cogs`, crie um novo arquivo chamado `support.py` e cole o conteúdo fornecido.
    *   Crie um novo arquivo chamado `requirements.txt` e cole o conteúdo fornecido.
    *   Crie um novo arquivo chamado `.replit` e cole o conteúdo fornecido.
    *   Crie um novo arquivo chamado `replit.nix` e cole o conteúdo fornecido.

3.  **Configure a Variável de Ambiente `DISCORD_TOKEN`:**
    *   No Replit, clique no ícone de `Secrets` (um cadeado) na barra lateral esquerda.
    *   Clique em `New Secret`.
    *   No campo `Key`, digite `DISCORD_TOKEN`.
    *   No campo `Value`, cole o token do seu bot do Discord.
    *   Clique em `Add new secret`.

    **Importante:** Nunca exponha seu token do bot diretamente no código. As variáveis de ambiente são a forma segura de armazená-lo.

4.  **Habilite as Intenções (Intents) no Portal do Desenvolvedor do Discord:**
    Para que seu bot possa ler mensagens e gerenciar membros, você precisa habilitar as intenções necessárias no [Portal do Desenvolvedor do Discord](https://discord.com/developers/applications):
    *   Vá para a URL do seu aplicativo.
    *   No menu lateral esquerdo, clique em `Bot`.
    *   Role para baixo até a seção `Privileged Gateway Intents`.
    *   Ative as opções `PRESENCE INTENT`, `SERVER MEMBERS INTENT` e `MESSAGE CONTENT INTENT`.
    *   Salve as alterações.

## 3. Mantendo o Bot Online 24/7 com UptimeRobot

O Replit hiberna projetos que não estão ativos. Para manter seu bot online 24/7, você pode usar um serviço de monitoramento como o UptimeRobot para "pingar" o servidor web Flask do seu bot regularmente.

1.  **Obtenha o URL do seu Repl:**
    *   Quando seu bot estiver rodando no Replit, você verá uma janela de `Webview` (ou `Browser`) exibindo a mensagem "Bot do Discord está online!".
    *   Copie o URL desta janela (ex: `https://meubotdiscord.kaualopesalves1.repl.co`). Este será o URL do seu servidor Flask.

2.  **Configure o UptimeRobot:**
    *   Vá para [UptimeRobot](https://uptimerobot.com/) e crie uma conta (é gratuito para o plano básico).
    *   No painel, clique em `Add New Monitor`.
    *   Selecione `Monitor Type` como `HTTP(s)`.
    *   Em `Friendly Name`, digite um nome para seu monitor (ex: `MeuBotDiscord-KeepAlive`).
    *   Em `URL (or IP)`, cole o URL do seu Repl que você copiou no passo anterior.
    *   Deixe `Monitoring Interval` em 5 minutos (ou o mínimo permitido pelo seu plano gratuito).
    *   Clique em `Create Monitor`.

O UptimeRobot irá "pingar" seu servidor Flask a cada 5 minutos, impedindo que o Replit hiberne seu projeto e mantendo seu bot online.

## 4. Executando o Bot

Após seguir todos os passos acima, clique no botão `Run` no Replit. O console deve mostrar as mensagens de inicialização do Flask e do bot do Discord, indicando que ele está online e pronto para uso.

Seu bot agora está configurado para rodar no Replit, com comandos melhorados e um sistema para mantê-lo ativo 24/7!


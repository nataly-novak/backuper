This is a bot you can use in your server to archive the history in the channel.
To use it, you need to run it locally. 
This is a python bot, requiring discord.py and python-dotenv to run. 

Running this bot will require you to go to Discord developer portal and create a bot.
The token goes to the .env file in the form of the line DISCORD_TOKEN=token_that_you_got
You will also need to enable Message Content Intent.

You will have to add this bot to your server with the widest permissions.

After you got this running, you go to the channel that you want to backup, run the command !copy.
It takes some time, you will get the message "done", when the archiving is done. The file will be saved in the bot folder, feel free to move it.

This bot acts locally and does not send anything to the third parties, but it takes some time to set up.
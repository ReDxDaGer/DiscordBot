
<img align = "centre" src = "https://cdn.dribbble.com/users/339280/screenshots/17754146/media/c6dad0457dc5f3ba9d248203318d831b.png?resize=1000x750&vertical=center" />


# DiscordBot
- This bot is made for ease to manage the server easily, it is a multi utility bot which can help you and your discord server in several ways .
# Features
- It can nuke a channel before nuking the channel it will create a new channel of the same name and same permissions and then will nuke or delete the previous channel.
- It can ban all the members of the server (but that piece of command can only be executed by thr person who is owner of the server.)
- It can kick all the members of the server (but that piece of command can only be executed by thr person who is owner of the server.)
- It can join vc as well as can leave the vc (voice chats) and can play multiple songs of your choice.
- It can display the avatar of the person who is mentioned.
- It can delete several messages as per your command



# How to use the Bot
- Prefix of the bot is ```!!```
- You can kick all by ```!!kickall```
- You can ban all by ```!!banall```
- You can make it join vc by ```!!join (copy the id of vc and paste here.)```
- You can play music by ```!!play (link of the song you want it to play from youtube.)```
- You can ask for help by ```!!help```
- You can ask for avatar pic of somebody by ```!!av @mention_the_user```
- You can delete several messages by ```!!clear (amount)```

# Installation
Clone the repo
```git clone https://github.com/ReDxDaGer/DiscordBot```

Setup: Add your `openai` API key and Discord bot token in a file named `.env` inside the directory

- Method-1: Python setup
```bash
cd DiscordBot
pip install -r requirements.txt
python3 main.py
```

- Method-2: Docker setup
```
docker build . -t discordbot
docker run -it discordbot
```

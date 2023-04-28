import requests
import dotenv
import os
import nextguild as ng
dotenv.loadenv()
bot = ng.Client(os.getenv("GUILDED_BOT_TOKEN"))
events = ng.Event(bot)


@events.on_ready
async def onready():
    print(f"Logged In As:  {bot.get_bot_user_id()}")


@events.on_message
async def pingcommand(message):
    if message.content == "ab!ping":
        bot.send_message(channel_id=message.channel_id, content="Pongyang!")


@events.on_message
async def bancommand(message):
    if message.content.startswith("ab!ban"):
        authorid = message.author_id
        if bot.is_server_owner(message.server_id, authorid):
            mysubstring = "ab!ban"
            words = message.content.split()
            index = words.index(mysubstring)
            result = ' '.join(words[index + 1:])
            try:
                bot.ban_member(result)
                bot.send_message(
                    channel_id=message.channel_id,
                    content=f"Banned {result}")
            except BaseException:
                bot.send_message(
                    channel_id=message.channel_id,
                    content=f"You Either Entered a wrong/invalid UserId or Something happened within guildeds api servers UserID: {result}")
        else:
            bot.send_message(
                channel_id=message.channel_id,
                content=f"Sam I wont allow you to use this command. sorry")


@events.on_message
async def kickcommand(message):
    if message.content.startswith("ab!kick"):
        authorid = message.author_id
        if bot.is_server_owner(message.server_id, authorid):
            mysubstring = "ab!kick"
            words = message.content.split()
            index = words.index(mysubstring)
            result = ' '.join(words[index:1:])
            try:
                bot.ban_member(result)
                bot.send_message(
                    channel_id=message.channel_id,
                    content=f"Kicked {result}")
            except BaseException:
                bot.send_message(
                    channel_id=message.channel_id,
                    content=f"You Either Entered a wrong/invalid UserId or Something happened within guildeds api servers UserID: {result}")
        else:
            bot.send_message(
                channel_id=message.channel_id,
                content=f"Sam i wont allow you to use this command. sorry")


@events.on_message
async def jokecommand(message):
    if message.content.startswith("ab!getjoke"):
        url = "https://icanhazdadjoke.com/"
        headers = {
            "Accept": "application/json",
            "User-agent": "Guilded General Purpose bot(https://github.com/LeontKing2/GuildedGeneralPurposeBot)"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            joke = response.json()["joke"]
            bot.send_message(
                channel_id=message.channel_id,
                content=f"Joke: {joke}")
        else:
            bot.send_message(
                channel_id=message.channel_id,
                content=f"Error Happened: {response.status_code}")


@events.on_member_join
async def memberjoin(user):
    member = user["user"]["name"]
    bot.send_message(
        channel_id="30550ef9-4028-41ce-a311-673a77a185c6",
        content=f"{member} joined the Server! Welcome him in #general")
events.run()

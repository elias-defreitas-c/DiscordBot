from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from sqlite.creating_tables import create_tables

load_dotenv()
Token: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


async def send_message(message: Message, user_message: str, user_id: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    is_private = user_message[0] == 'p'
    is_called = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, user_id)
        if is_private:
            await message.author.send(response)
        elif is_called:
            await message.channel.send(response)
    except Exception as e:
        print(e)
        e = 'Use ?help to get a list of the commands'
        await message.channel.send(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    create_tables()


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    user_id: str = str(message.author.id)
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {user_id}"{username}": "{user_message}"')
    await send_message(message, user_message, user_id)


def main() -> None:
    client.run(token=Token)


if __name__ == '__main__':
    main()

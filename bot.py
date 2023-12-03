import asyncio
import re
from rubpy import Client, models, handlers, Message

class MessageHandler:
    def __init__(self, gaps, forbidden_patterns):
        self.gaps = gaps
        self.forbidden_patterns = forbidden_patterns

    async def check_forwarded(self, message):
        return "message" in message.original_update and "forwarded_from" in message.original_update["message"]

    async def check_forbidden_patterns(self, text):
        return text and any(re.search(pattern, text) for pattern in self.forbidden_patterns)

    async def delete_message(self, client, msg, obguid):
        await client.delete_messages(message_ids=msg, object_guid=obguid)

    async def handle_updates(self, client, message):
        if message.object_guid in self.gaps:
            text = message.raw_text
            msg = message.message_id
            obguid = message.object_guid
            if await self.check_forwarded(message) or await self.check_forbidden_patterns(text):
                await self.delete_message(client, msg, obguid)

def test_check_forbidden_patterns():
    handler = MessageHandler("gap", [r".*@.*", r".*https://rubika\.ir.*"])
    assert asyncio.run(handler.check_forbidden_patterns("@")) == True
    assert asyncio.run(handler.check_forbidden_patterns("https://rubika.ir")) == True
    assert asyncio.run(handler.check_forbidden_patterns("hello")) == False
    print("Anti-link and forward was activated successfully!")

async def main():
    handler = MessageHandler(["guid1", "guid2"], [r".*@.*", r".*https://rubika\.ir.*"])
    async with Client(session="Self") as client:
        @client.on(handlers.MessageUpdates())
        async def updates(message: Message):
            await handler.handle_updates(client, message)
                
        await client.run_until_disconnected()

test_check_forbidden_patterns()
asyncio.run(main())

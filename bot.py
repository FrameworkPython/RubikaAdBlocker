import asyncio
import re
from typing import List
from rubpy import Client,Message ,markdown ,models



class MessageHandler:
    def __init__(self, forbidden_patterns: List[str], owner_guid: str):
        self.forbidden_patterns = forbidden_patterns
        self.owner_guid = owner_guid
        self.strict_mode = False
        self.warning_mode = False
        self.last_command = None
        self.last_warning_command = None
        self.warnings = {}
        self.max_warnings = 3
        
    async def get_admins(self, client: Client, group_guid: str) -> List[str]:
        admins = await client.get_group_admin_members(group_guid)
        return [admin.member_guid for admin in admins.in_chat_members]
    async def check_forwarded(self, message: Message) -> bool:
        return "message" in message.original_update and "forwarded_from" in message.original_update["message"]

    async def check_forbidden_patterns(self, text: str) -> bool:
        return text and any(re.search(pattern, text) for pattern in self.forbidden_patterns)

    async def delete_message(self, client: Client, msg: int, obguid: str) -> None:
        await client.delete_messages(message_ids=msg, object_guid=obguid)

    async def ban_group_member(self, client: Client, group_guid: str, member_guid: str) -> None:
        await client.ban_group_member(group_guid, member_guid)

    async def unban_group_member(self, client: Client, group_guid: str, member_guid: str) -> None:
        await client.unban_group_member(group_guid, member_guid)
    async def get_banned_members(self, client: Client, group_guid: str) -> List[models.InChatMember]:
        banned_members = await client.get_banned_group_members(group_guid)
        return banned_members.in_chat_members

    async def clear_ban_list(self, client: Client, group_guid: str, msg: int) -> None:
        banned_members = await self.get_banned_members(client, group_guid)
        if not banned_members:
            await client.send_message(group_guid, "لیست سیاه خالی است.", reply_to_message_id=msg,auto_delete=45)
        else:
            for member in banned_members:
                await self.unban_group_member(client, group_guid, member.member_guid)
            await client.send_message(group_guid, "لیست سیاه پاکسازی شد.", reply_to_message_id=msg,auto_delete=45)
    async def get_group_link(self, client: Client, group_guid: str, msg: int) -> None:
        try:
            group_link = await client.get_group_link(group_guid)
            await client.send_message(group_guid, f"لینک گروه:\n {group_link.join_link}", reply_to_message_id=msg,auto_delete=45)
        except Exception:
            await client.send_message(group_guid, "در دریافت لینک مشکلی پیش آمد.", reply_to_message_id=msg,auto_delete=45)

    async def handle_updates(self, client: Client, message: Message) -> None:
        text = message.raw_text
        msg = message.message_id
        obguid = message.object_guid
        author = message.author_guid
        admins = await self.get_admins(client, obguid)
        if author in admins and author != self.owner_guid:
                    if await self.check_forwarded(message) or await self.check_forbidden_patterns(text):
                        await self.delete_message(client, msg, obguid)
        else:
            if author == self.owner_guid:
                if text == "اخطار خاموش" and self.last_warning_command != "اخطار خاموش":
                    self.warning_mode = False
                    self.last_warning_command = "اخطار خاموش"
                    asyncio.create_task(client.send_message(obguid, "سیستم اخطار خاموش شد.", reply_to_message_id=msg,auto_delete=45))
                elif text.startswith("اخطار ") and self.last_warning_command != text:
                    self.max_warnings = int(text.split()[1])
                    self.warning_mode = True
                    self.last_warning_command = text
                    asyncio.create_task(client.send_message(obguid, f"حداکثر اخطار تنظیم شد به {self.max_warnings}.", reply_to_message_id=msg,auto_delete=45))
                elif text.startswith("راهنما"):
                    asyncio.create_task(client.send_message(obguid,"""راهنما\n1. 🚫 اخطار خاموش: با ارسال این دستور، فقط لینک‌ها و تبلیغات پاک می‌شوند و اخطاری داده نمی‌شود.\n
2. ⚠️ اخطار X: با جایگزینی X با یک عدد، می‌توانید تعداد اخطارهای مجاز را تنظیم کنید. به عنوان مثال، اخطار 4 .\n
3. 🛡️حالت سختگیر: با فعال کردن این حالت، هر کسی که لینک ارسال کند یا پیامی را فوروارد کند، بلافاصله از گروه حذف می‌شود.\n
4. 🔄 حالت سختگیر غیرفعال: با این دستور، فقط پیام‌ها و فورواردها پاک می‌شوند.\n
5. 📝 لیست سیاه: با این دستور، می‌توانید لیست کاربران مسدود شده را مشاهده کنید.\n
6. 🗑️ پاکسازی لیست سیاه: با این دستور، تمام کاربران مسدود شده از لیست سیاه حذف می‌شوند.\n
7. 🔗 لینک: با این دستور، می‌توانید لینک گروه را دریافت کنید.\n
8. 🚷 بن: با ریپلی کردن یک کاربر و ارسال این دستور، کاربر مورد نظر از گروه حذف می‌شود.\n
9.❗اخطار: با ریپلی کردن یک کاربر و ارسال این دستور، یک اخطار به کاربر مورد نظر داده می‌شود.\n
10. 🧹 پاک کردن اخطار: با ریپلی کردن یک کاربر و ارسال این دستور، تمام اخطارهای کاربر مورد نظر پاک می‌شوند.\n
11. 📊 وضعیت اخطار: با ریپلی کردن یک کاربر و ارسال این دستور، می‌توانید تعداد اخطارهای کاربر مورد نظر را ببینید.\n
❌ توجه:تمامی پیام هایی که ربات ارسال میکند، اعم از اجرای دستورات و ... بعد از ۱ دقیقه پاک خواهند شد       
            """, reply_to_message_id=msg,auto_delete=45))
                elif text == "حالت سختگیر" and self.last_command != "حالت سختگیر":
                    self.strict_mode = True
                    self.last_command = "حالت سختگیر"
                    asyncio.create_task(client.send_message(obguid, "حالت سخت گیر فعال شد. لینک ها و پیام های فوروارد شده حذف خواهند شد و کاربرانی که این کار را انجام می دهند از گروه حذف خواهند شد.", reply_to_message_id=msg,auto_delete=45))
                elif text == "حالت سختگیر غیرفعال" and self.last_command != "حالت سختگیر غیرفعال":
                    self.strict_mode = False
                    self.last_command = "حالت سختگیر غیرفعال"
                    asyncio.create_task(client.send_message(obguid, "حالت سخت گیر غیرفعال شد. فقط لینک ها و پیام های فوروارد شده حذف خواهند شد.", reply_to_message_id=msg,auto_delete=45))
                elif text == "لیست سیاه":
                    banned_members = await self.get_banned_members(client, obguid)
                    if not banned_members:
                        await client.send_message(obguid, "لیست سیاه خالی است.", reply_to_message_id=msg,auto_delete=45)
                    else:
                        message_text = "\n".join([f"User Name: {member.first_name}\nGuid: {member.member_guid}\nRemover(Remove By): {member.removed_by_object_guid}\n\n" for member in banned_members])
                        await client.send_message(obguid, message_text, reply_to_message_id=msg,auto_delete=45)
                elif text == "پاکسازی لیست سیاه":
                    await self.clear_ban_list(client, obguid, msg)
                elif text.startswith("پاک کردن اخطار") and message.reply_to_message_id:
                    reply_message = await client.get_messages_by_ID(obguid, [message.reply_to_message_id])
                    reply_author_guid = reply_message.messages[0].author_object_guid
                    if reply_author_guid in self.warnings:
                        del self.warnings[reply_author_guid]
                        await client.send_message(obguid, "اخطارهای کاربر پاک شدند.", reply_to_message_id=message.reply_to_message_id,auto_delete=45)
                elif text.startswith("وضعیت اخطار") and message.reply_to_message_id:
                    reply_message = await client.get_messages_by_ID(obguid, [message.reply_to_message_id])
                    reply_author_guid = reply_message.messages[0].author_object_guid
                    warnings = self.warnings.get(reply_author_guid, 0)
                    if warnings == 0:
                        await client.send_message(obguid, "این کاربر اخطار ندارد.", reply_to_message_id=message.reply_to_message_id,auto_delete=45)
                    else:
                        warning_status_message = f"تعداد اخطارهای کاربر: {warnings}/{self.max_warnings}"
                        asyncio.create_task(client.send_message(obguid, warning_status_message, reply_to_message_id=message.reply_to_message_id,auto_delete=45))
                elif text == "لینک":
                    await self.get_group_link(client, obguid, msg)
                elif text == "بن" and message.reply_to_message_id:
                        reply_message = await client.get_messages_by_ID(obguid, [message.reply_to_message_id])
                        reply_author_guid = reply_message.messages[0].author_object_guid
                        if reply_author_guid not in admins:
                            await self.ban_group_member(client, obguid, reply_author_guid)
                        else:
                           return 
                elif text.startswith("اخطار") and message.reply_to_message_id:
                    reply_message = await client.get_messages_by_ID(obguid, [message.reply_to_message_id])
                    reply_author_guid = reply_message.messages[0].author_object_guid
                    if reply_author_guid not in admins:
                        self.warnings.setdefault(reply_author_guid, 0)
                        self.warnings[reply_author_guid] += 1
                        warning_message = f"کاربر گرامی شما اخطار دریافت کردید، پس از تکمیل اخطار از گروه حذف خواهید شد.اخطار شما:{self.warnings[reply_author_guid]}/{self.max_warnings}"
                        asyncio.create_task(client.send_message(obguid, warning_message, reply_to_message_id=message.reply_to_message_id,auto_delete=45))
                        if self.warnings[reply_author_guid] >= self.max_warnings:
                            await self.ban_group_member(client, obguid, reply_author_guid)
                            del self.warnings[reply_author_guid]
                    else:
                          return 
            elif author != self.owner_guid and (await self.check_forwarded(message) or await self.check_forbidden_patterns(text)):
                await self.delete_message(client, msg, obguid)
                if self.strict_mode:
                    await self.ban_group_member(client, obguid, message.author_guid)
                elif self.warning_mode:
                    self.warnings.setdefault(message.author_guid, 0)
                    self.warnings[message.author_guid] += 1
                    warning_message = f"کاربر گرامی تبلیغات ممنوع است، در صورت تکمیل اخطار،از گروه حذف خواهید شد، اخطار شما :{self.warnings[message.author_guid]}/{self.max_warnings}"
                    asyncio.create_task(client.send_message(obguid, warning_message, reply_to_message_id=message.message_id,auto_delete=45))
                    if self.warnings[message.author_guid] >= self.max_warnings:
                        await self.ban_group_member(client, obguid, message.author_guid)
                        del self.warnings[message.author_guid]


async def main() -> None:
    gaps = ["g0DhOML041a0db4e67ede35a1bcb515f","g0DvCmj0f14c6752e554bd9e4aeab040","g0DQVcs06895f970201487d0ea1fdd97"]
    handlers = {gap: MessageHandler([r".*@.*", r".*https://.*",r".*http://.*", r".*Https://.*", r".*Http://.*"], "u0Ez69m073020b4ae5027950259a2cd2") for gap in gaps}
    async with Client(session="Self") as client:
        @client.on_message()
        async def updates(message: Message) -> None:
            if message.object_guid in handlers:
                await handlers[message.object_guid].handle_updates(client, message)

        await client.run_until_disconnected()
try:
    asyncio.run(main())
except Exception as e:
    print(f"An error occurred: {e}")

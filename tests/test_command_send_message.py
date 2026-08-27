import asyncio
from types import SimpleNamespace
from unittest import TestCase

from main import bartender_crawler


class BareCommandEvent:
    message_str = "酒"
    message_obj = SimpleNamespace(self_id="bot")

    def get_group_id(self):
        return "test-group"

    def get_sender_id(self):
        return "test-user"

    def plain_result(self, text):
        return text


class CommandSendMessageTests(TestCase):
    def test_bare_command_is_rejected_before_browser_use(self):
        instance = object.__new__(bartender_crawler)
        instance.allowed_group_ids = {"test-group"}
        instance.admin_ids = set()
        instance.status_running = True

        async def collect_results():
            return [
                result
                async for result in instance.command_send_message(BareCommandEvent())
            ]

        self.assertEqual(asyncio.run(collect_results()), ["禁止输入为空"])
        self.assertTrue(instance.status_running)


if __name__ == "__main__":
    import unittest

    unittest.main()

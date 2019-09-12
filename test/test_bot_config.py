import unittest

from config.bot_config import BotConfig


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.bot_config = BotConfig()
        self.bot_config.initialize()

    def test_get_property_value(self):
        sleep_time = self.bot_config.get_property_value('BOT_SLEEP_TIME')
        self.assertIsNotNone(sleep_time)

    def test_get_property_values(self):
        bot_queries = self.bot_config.get_property_value('BOT_QUERIES')
        self.assertIsNotNone(bot_queries)
        self.assertTrue(len(bot_queries) > 0)


if __name__ == '__main__':
    unittest.main()

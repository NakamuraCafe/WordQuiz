from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from unittest.mock import patch

class CommandTestCase(TestCase):

    def test_game_clear(self):
        food = "apple"
        user_inputs = list(food)
        with patch('random.choice', return_value=food), patch('getpass.getpass', side_effect=user_inputs):
            out = StringIO()
            with patch('sys.stdout', out):
                call_command('word_quiz')
                output = out.getvalue()

            self.assertIn(f'ゲームクリア! 答え: {food}', output)
            self.assertNotIn(f'ゲームオーバー 答え: {food}', output)

    def test_game_over(self):
        food = "apple"
        user_inputs = ["x", "y", "z", "u", "v"]
        with patch('random.choice', return_value=food), patch('getpass.getpass', side_effect=user_inputs):
            out = StringIO()
            with patch('sys.stdout', out):
                call_command('word_quiz')
                output = out.getvalue()

            self.assertIn('ゲームオーバー 答え: apple', output)
            self.assertNotIn('ゲームクリア! 答え: apple', output)

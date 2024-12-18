from django.core.management.base import BaseCommand
from ...modules.custom_validation import CustomVaridation
import getpass
import random

class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.foods = ["apple", "bread", "grape", "honey", "lemon", "mango", "melon", "onion", "peach", "plum", "prune", "radish", "sugar", "wheat", "yogurt"]
        self.answer = random.choice(self.foods)
        self.display = "_" * len(self.answer)
        self.attempts = 0
        self.max_attempts = 5

    def handle(self, *args, **kwargs):
        while self.attempts < self.max_attempts and "_" in self.display:
            self.stdout.write(self.display)
            self.stdout.write(str(self.max_attempts - self.attempts))
            # user_input = input().lower()
            user_input = getpass.getpass("").lower()

            if len(user_input) != 1 or not CustomVaridation.is_single_alphabet(user_input):
                self.stdout.write(self.style.ERROR('アルファベット一文字だけを入力してください'))
                continue

            self.attempts += 1
            new_display = list(self.display)

            for i, char in enumerate(self.answer):
                if char == user_input:
                    new_display[i] = user_input

            self.display = "".join(new_display)

        if "_" not in self.display:
            self.stdout.write(self.style.SUCCESS(f'ゲームクリア! 答え: {self.answer}'))
        else:
            self.stdout.write(self.style.ERROR(f'ゲームオーバー 答え: {self.answer}'))
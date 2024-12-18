import re

class CustomVaridation:

    def is_single_alphabet(text):
        pattern = r'^[A-Za-z]$'
        if re.match(pattern, text):
            return True
        else:
            return False
import random
from string import ascii_lowercase


class NameGenerator:
    @classmethod
    def random_name(cls):
        random_ID_list = random.choices(ascii_lowercase, k=20)
        random_ID = "".join(random_ID_list)
        return random_ID

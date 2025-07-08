#sloth.py
from .animal import Animal


class Sloth(Animal):
    def __init__(self, name="Sid"):
        super().__init__(name, species="Sloth")

    def sound(self):
        return "zzzzzzzzzz"

    def action(self):
        return "Has a gentle snooze in a tree"

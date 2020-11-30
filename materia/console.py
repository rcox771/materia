from rich.console import Console
from pydantic import BaseModel
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from typing import List

console = Console(color_system="auto")


def style_squares(text, style):
    return f"[{style}]{text}[/{style}]"


def first_letter_highlight(word, style="bold red"):
    a, b = word[0].upper(), word[1:]
    a = style_squares(a, style)
    return f"{a}{b}"


def first_letter(word):
    return word[0].upper()


class Menu(BaseModel):
    question: str
    choices: List[str]

    def interact(self):
        # for i, choice in enumerate(self.choices):
        console.print(Columns([Panel(first_letter_highlight(c)) for c in self.choices]))
        response = ask(self.question, list(map(first_letter, self.choices)))
        return response


class Character(BaseModel):
    name: str
    color_ref: "str" = "orange1"

    def __str__(self):
        return style_squares(self.name, self.color_ref)


def greet(player):
    console.print(f"Hello, {player}! :smile:")


def ask(question, choices, default=None):
    return Prompt.ask(question, choices=choices, default=default)


p = Character(name="Moz")
greet(p)

shopmenu = Menu(question="So what'll it be?", choices=["buy", "sell", "talk", "exit"])
shopmenu.interact()
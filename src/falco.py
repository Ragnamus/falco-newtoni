# coding=utf-8

"""
FALCO NEWTONI: A machine learning based chat bot for use in kestrel-bot.

Author: Akharis Ren
"""

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r'hi',
        ['hello', 'greetings', 'aloha']
    ],
]


def falco_bot():
    """Bot function."""
    print("Hi")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == '__main__':
    falco_bot()

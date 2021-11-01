"""
function search
"""

import requests


def most_common_word_in_web_page(words, url, user_agent=requests):
    """
    Находит наиболее распространённое слово из списка лов на странице,
    идентифицируемой по ее url
    """
    responce = user_agent.get(url)
    return most_common_word(words, responce.text)


def most_common_word(words, text):
    """
    Ищет слово в фрагменте текста
    """
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

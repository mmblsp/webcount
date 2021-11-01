"""
tests
"""
from unittest.mock import Mock, patch
from pytest import raises

from webcount import most_common_word_in_web_page, most_common_word


def test_with_test_mock():
    """
    Внедрение зависимостей.
    использование user_agent
    """
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'

    result = most_common_word_in_web_page(
        ['a', 'b', 'c'],
        'https://python.org/',
        user_agent=mock_requests
    )
    assert result == 'b', \
        'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] \
        == 'https://python.org/', 'called with right URL'


def test_with_patch():
    """
    Подмена пути, если внедрение зависимостей нецелесообразна.
    применяем динамическую природу Python и менеджер контента
    с фиктивным path
    """
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    with patch('webcount.functions.requests', mock_requests):
        result = most_common_word_in_web_page(
            ['a', 'b', 'c'],
            'https://python.org/',
            user_agent=mock_requests
        )
    assert result == 'b', \
        'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] \
        == 'https://python.org/', 'called with right URL'


def test_with_test_double():
    """with test double"""
    class TestResponse():
        """tests"""
        text = 'aa bbb c'

    class TestUserAgent():
        """tests"""

        def __init__(self) -> None:
            self.url = None

        def get(self, url):
            """tests"""
            self.url = url
            return TestResponse()

    result = most_common_word_in_web_page(
        ['a', 'b', 'c'],
        'https://python.org/',
        user_agent=TestUserAgent()
    )
    assert result == 'b', \
        'most_common_word_in_web_page tested with test double'


def test_most_common_word():
    """tests"""
    assert most_common_word(['a', 'b', 'c'], 'abbbcc') \
        == 'b', 'most_common_word whith unique aswer'


def test_most_common_word_empty_candidate():
    """tests"""
    with raises(IndexError):
        most_common_word([], 'abc')


def test_most_common_ambiquous_result():
    """tests"""
    assert most_common_word(['a', 'b', 'c'], 'ab') \
        in ('a', 'b'), "themight be a tie"

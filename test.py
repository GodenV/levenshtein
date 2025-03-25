import pytest

from src.levenshtein_count import levenshtein_count


@pytest.mark.parametrize(
    "string1, string2, expected",
    [
        ("Recontrutcvoin", "Reconstruction", 5),
        ("sittin", "sitting", 1),
        ("", "", 0),
        ("abadadadc", "", 9),
        ("", "abadadadc", 9),
        ("rmvnjdhebkvd", "rmvnjdhebkvd", 0),
        ("a", "b", 1),
        ("abcdef", "azced", 3),
        ("apple", "aple", 1),
    ]
)
def test_levenshtein_count(string1, string2, expected):
    assert levenshtein_count(string1, string2) == expected
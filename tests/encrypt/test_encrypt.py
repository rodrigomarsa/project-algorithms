import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_message_only_can_be_string():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)


def test_message_is_none():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(None, 1)


def test_key_only_can_be_number():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcd", "a")


def test_key_is_none():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcd", None)


def test_key_is_greater_than_string_and_odd():
    assert encrypt_message("abcdef", 8) == "fedcba"


def test_key_is_greater_than_string_and_even():
    assert encrypt_message("abcdef", 9) == "fedcba"


def test_key_when_is_zero():
    assert encrypt_message("abcdef", 0) == "fedcba"


def test_key_when_is_odd():
    assert encrypt_message("abcdef", 4) == "fe_dcba"


def test_key_when_is_even():
    assert encrypt_message("abcdef", 3) == "cba_fed"


def test_key_when_is_equal_to_message():
    assert encrypt_message("abcdef", 6) == "fedcba"


def test_key_when_less_than_1():
    assert encrypt_message("abcdef", 5) == "edcba_f"


def test_key_when_less_than_2():
    assert encrypt_message("abcdef", 4) == "fe_dcba"


def test_key_when_less_than_3():
    assert encrypt_message("abcdef", 3) == "cba_fed"


def test_key_when_less_than_4():
    assert encrypt_message("abcdef", 2) == "fedc_ba"


def test_key_when_less_than_5():
    assert encrypt_message("abcdef", 1) == "a_fedcb"

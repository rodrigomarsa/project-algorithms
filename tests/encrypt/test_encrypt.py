import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcd", "a")

    assert encrypt_message("qualquer", 0) == "reuqlauq"

    assert encrypt_message("qualquer", 1) == "q_reuqlau"

    assert encrypt_message("qualquer", 3) == "auq_reuql"

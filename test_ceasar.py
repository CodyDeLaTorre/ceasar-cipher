from caesar_cipher import cipher
import pytest

def test_encrypt_shift_1():
    actual = cipher.encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected

# @pytest.mark.skip()
def test_encrypt_shift_10():
    actual = cipher.encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected

# @pytest.mark.skip()
def test_encrypt_shift_20():
    actual = cipher.encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected

# @pytest.mark.skip()
def test_uppercase():
    actual = cipher.encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected

# @pytest.mark.skip()
def test_with_whitespace():
    actual = cipher.encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected

# @pytest.mark.skip()
def test_with_non_alpha():
    actual = cipher.encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected

# @pytest.mark.skip()
def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = cipher.encrypt(original, shift)
    actual = cipher.decrypt(encrypted, shift)
    expected = original
    assert actual == expected

# @pytest.mark.skip()
def test_crack_phrase():
    phrase = "It was the best of times, it was the worst of times."
    encrypted = cipher.encrypt(phrase, 10)
    actual = cipher.crack(encrypted)
    expected = phrase
    assert actual == expected

@pytest.mark.skip()
def test_crack_nonsense():
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = cipher.encrypt(phrase, 10)
    actual = cipher.crack(encrypted)
    expected = ""
    assert actual == expected

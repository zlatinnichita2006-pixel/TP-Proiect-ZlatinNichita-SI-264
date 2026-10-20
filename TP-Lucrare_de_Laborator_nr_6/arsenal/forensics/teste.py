# teste/test_decode.py
from arsenal import *
import arsenal.forensics.decode

def test_base64():
    strat, b = arsenal.forensics.decode.main().desfa("U2FsdXQ=")
    assert strat == "base64"
    assert b == b"Salut"

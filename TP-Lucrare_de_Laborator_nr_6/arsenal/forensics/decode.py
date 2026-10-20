import re
import base64
import hashlib
import argparse
import json
from urllib.parse import unquote

def main():

    print("=" * 90)
    # A1
    print("A1")
    s = "Salut"
    b = s.encode()
    print(b, b[0])
    print(b.hex())
    c = bytes.fromhex(b.hex())
    print(c)
    print("=" * 90)

    # A2
    print("A2")

    def ghici_strat(s):
        if re.search(r"%[0-9a-fA-F]{2}", s):
            return "url"
        elif re.fullmatch(r"[0-9a-fA-F]+", s) and (len(s) % 2 == 0):
            return "hex"
        elif re.fullmatch(r"[0-9a-zA-Z+/=]+", s):
            return "base64"
        else:
            return "necunoscut"

    print(ghici_strat("%2Fetc"))  # url
    print(ghici_strat("48656c6c6f"))  # hex
    print("=" * 90)

    # A3
    print("A3")

    def desfa(s):
        strat = ghici_strat(s)
        if strat.startswith("u"):
            return strat, unquote(s).encode()
        elif strat.startswith("h"):
            return strat, bytes.fromhex(s)
        elif strat.startswith("b"):
            return strat, base64.b64decode(s)
        else:
            return strat, s.encode()

    print(desfa("%2Fetc"))
    print(desfa("48656c6c6f"))
    print("=" * 90)

    # A4
    print("A4")

    def citibil(b):
        return all(32 <= c < 127 for c in b)

    val = "NTM1OTU3NTk="
    for _ in range(8):
        strat, b = desfa(val)
        if citibil(b):
            print(strat, b.decode())
            break
        val = b.decode()
    print("=" * 90)

    # A5
    print("A5")
    date = open("../../xor.bin", "rb").read()
    for k in range(256):
        clar = bytes(b ^ k for b in date)
        # TODO: daca citibil(clar):
        #       print("cheie:", k, clar.decode())
        if citibil(clar):
            print("cheie:", k, clar.decode())

    print("=" * 90)

    # A6
    print("A6")
    tinta = open("../../hashuri.txt").readline().strip()
    print(len(tinta))  # 32 md5 / 40 sha1 / 64 sha256
    for cuv in open("../../wordlist.txt", encoding="latin1"):
        cuv = cuv.strip()
        # TODO: daca hashlib.md5(cuv.encode()).hexdigest()
        #       == tinta: print("gasit:", cuv); break
        if hashlib.md5(cuv.encode()).hexdigest() == tinta:
            print("gasit:", cuv)
            break

    print("=" * 90)

    # A7
    print("A7")
    import argparse, json
    p = argparse.ArgumentParser()
    p.add_argument("intrare")  # sir sau cale
    p.add_argument("--fisier", action="store_true")
    a = p.parse_args()
    if a.fisier:
        my_file = open(a.intrare, "r", encoding="utf-8").read().strip()
    else:
        my_file = a.intrare

    strat_json, decode_json = desfa(my_file)
    date_fisa = {
        "strat": strat_json,
        "rezultat": decode_json.decode()
    }

    import json
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent
    fisa_path = BASE_DIR / "fisa.json"

    with open(fisa_path, "w", encoding="utf-8") as fisa:
        json.dump(date_fisa, fisa, indent=4)

    print(f"[+] Fișier salvat cu succes în: {fisa_path}")

    print("=" * 90)






if __name__ == "__main__":
    main()
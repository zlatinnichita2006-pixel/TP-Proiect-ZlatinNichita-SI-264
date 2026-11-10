# A1

import argparse, json, os

def citeste_linii(cale):
    result = []
    with open(cale, encoding="utf-8") as f:
        # TODO: intoarce lista liniilor .strip(), fara cele goale si fara cele cu #
        for i in f:
            linie_curata = i.strip()
            if linie_curata and not linie_curata.startswith("#"):
                result.append(linie_curata)

    return result

# A2

def nume(cale):
    # TODO: intoarce ce e dupa ultimul "/"  (vezi rsplit)
    return cale.rsplit('/', 1)[-1]


# A3

GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
            "less", "awk", "python3", "perl"}

def suid_constatari(cale):
    result = []
    cai = citeste_linii(cale)
    # TODO: pentru fiecare cale UNICA, in ordine sortata, un dict:
    #   {"cale": c, "nume": nume(c),
    #    "risc": "mare" daca nume(c) in GTFO, altfel "normal"}
    for i in sorted(set(cai)):
        cale = i
        nume_cale = nume(cale)
        if nume_cale in GTFO:
            risc = "mare"
        else:
            risc = "normal"
        result.append({"cale": cale, "nume": nume_cale, "risc": risc})

    return result

# A4

def sudo_constatari(cale):
    out = []
    for ln in citeste_linii(cale):
        user, drept = ln.split(" : ", 1)  # despachetare in tuplu
        # TODO: adauga {"user": user.strip(), "drept": drept.strip(),
        #   "risc": "mare" daca "NOPASSWD" in drept, altfel "normal"}
        if "NOPASSWD" in drept:
            risc = "mare"
        else:
            risc = "normal"
        out.append({"user": user.strip(), "drept": drept.strip(), "risc": risc})

    return out

def cron_constatari(cale):
    # TODO: campuri = ln.split(); user = campuri[5];
    #   comanda = " ".join(campuri[6:]); dict cu user si comanda
    out = []
    for ln in citeste_linii(cale):
        campuri = ln.split()
        user = campuri[5]
        commanda = " ".join(campuri[6:])
        out.append({"user": user.strip(), "commanda": commanda})

    return out

def enumereaza(d):
    return {
        "suid": suid_constatari(os.path.join(d, "suid.txt")),
        "sudo": sudo_constatari(os.path.join(d, "sudo.txt")),
        "cron": cron_constatari(os.path.join(d, "crontab.txt")),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    raport = enumereaza(a.capturi)
    sudo_users = {u['user'] for u in raport["sudo"]}
    cron_users = {u['user'] for u in raport["cron"]}
    all_users = sudo_users | cron_users
    if a.json:
        print(json.dumps(raport, indent=2, ensure_ascii=False)); return
    for categorie, lista in raport.items():
        mari = [c for c in lista if c.get("risc") == "mare"]
        print(f"{categorie}: {len(lista)} gasite, {len(mari)} cu risc mare")
    # TODO: utilizatorii implicati = multimea userilor din sudo REUNITA cu cei din cron
    print(f"utilizatorii implicati: {", ".join(sorted(all_users))}")
    with open("enum.json", "w", encoding="utf-8") as f:
        json.dump(raport, f, indent=2, ensure_ascii=False)
    print("Raport salvat in enum.json")


if __name__ == "__main__":
    main()
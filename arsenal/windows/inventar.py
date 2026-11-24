from dataclasses import dataclass, asdict
import json
import argparse

CAI_SUSPECTE = ("\\Temp\\", "\\Roaming\\")
SUSPECTE_ID = {4625, 1102, 7045}


# A1
@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str

# A2

    def e_suspect(self) -> bool:
        return any(zona in self.cale for zona in CAI_SUSPECTE)

# A3

@dataclass
class Eveniment:
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

    def e_suspect(self) -> bool:
        return self.id in SUSPECTE_ID or self.nivel == "critical"

# A4

def procese_din_json(cale: str) -> list[Proces]:
    with open(cale, encoding="utf-8") as f:
        return [Proces(**d) for d in json.load(f)]


def evenimente_din_json(cale: str) -> list[Eveniment]:
    with open(cale, encoding="utf-8") as f:
        return [Eveniment(**d) for d in json.load(f)]

# B1

@dataclass
class Inventar:
    procese: list[Proces]

    @classmethod
    def din_json(cls, cale: str) -> "Inventar":
        with open(cale, encoding="utf-8") as f:
            return cls([Proces(**d) for d in json.load(f)])

    def __len__(self) -> int:
        return len(self.procese)

# B2

    def suspecte(self) -> list[Proces]:
        return [p for p in self.procese if p.e_suspect()]

    def pe_user(self) -> dict[str, list[str]]:
        rezultat: dict[str, list[str]] = {}
        for p in self.procese:
            rezultat.setdefault(p.user, []).append(p.nume)
        return rezultat

    def scor(self, evenimente: list[Eveniment] | None = None) -> int:
        alarme_ev = sum(1 for e in (evenimente or []) if e.e_suspect())
        return len(self.suspecte()) + alarme_ev


# B3

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    inv = Inventar.din_json(a.capturi + "/procese.json")
    ev = evenimente_din_json(a.capturi + "/evenimente.json")
    alarma = [e for e in ev if e.e_suspect()]
    proc_suspecte = inv.suspecte()

    if a.json:
        raport = {
            "suspecte": [asdict(proc) for proc in proc_suspecte],
            "alarma": [asdict(e) for e in alarma],
        }
        print(json.dumps(raport, indent=2, ensure_ascii=False))
    else:
        print(f"Procese: {len(inv)} | suspecte: {len(proc_suspecte)}")
        for proc in proc_suspecte:
            print(f"  [{proc.pid}] {proc.nume}  ({proc.user})  {proc.cale}")

        print(f"Evenimente: {len(ev)} | alarma: {len(alarma)}")
        for e in alarma:
            print(f"  {e.id} [{e.nivel}] {e.cont}: {e.mesaj}")


if __name__ == "__main__":
    main()
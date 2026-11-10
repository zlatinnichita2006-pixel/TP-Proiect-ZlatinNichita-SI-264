from arsenal.privesc.enum import citeste_linii, nume, GTFO

# B1

def cai(fisier):
    # TODO: intoarce MULTIMEA cailor din fisier (foloseste citeste_linii din enum)
    return set(citeste_linii(fisier))


baza = cai("arsenal/privesc/start/baza_suid.txt")
acum = cai("arsenal/privesc/start/suid.txt")
print("baza:", len(baza), " acum:", len(acum))

# B2

noi = acum - baza
print(len(noi), "SUID noi fata de sistemul curat")
for c in sorted(noi):
    print(" ", c)

# B3

risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
print("periculoase NOI:", periculoase)

# B4





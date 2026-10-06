# Laborator: funcții, metode și importuri pe web
# Student: <Zlatin Nichita>

import time
import requests
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def main():
    # Exercitiul 9
    print("EXERCITIUL 9")
    time.sleep(1)
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    print(response.status_code)  # ATRIBUT
    print(response.ok)  # ATRIBUT
    print(response.url)  # ATRIBUT
    print(response.encoding)  # ATRIBUT

    # Exercitiul 10
    print("EXERCITIUL 10")
    time.sleep(1)
    try:
        response = requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
        response.raise_for_status()
    except requests.HTTPError:
        print("A avut loc o eroare in scrierea a url")

    # Exercitiul 11
    print("EXERCITIUL 11")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    for i, j in r.headers.items():
        print("{name}: {valoare}".format(name=i, valoare=j))

    # Exercitiul 12
    print("EXERCITIUL 12")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print("serverul:", r.headers.get("Server", "lipseste"))
    print("content_type:", r.headers.get("Content-type", "lipseste"))
    print("content_type (litere mici):", r.headers.get("content-type", "lipseste"))
    # Observam ca tot se printeaza acelasi rezultat, deoarece dictionarul
    # headers ignora prezenta majusculelor si minusculelor, din cauza
    # standardului web HTTP care specifica ca antetele nu sunt sensibile la
    # la majuscule si minuscule.

    # Exercitiul 13
    print("EXERCITIUL 13")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print(r.text.lower().count("cyber"))
    # Functiile lower si count au putut fi inlantuite deoarece .lower() returneaza tot text doar ca scris tot cu litere mici (string)
    # si deacee se pot inlantui alte metode precum count split si altele

    # Exercitiul 14
    print("EXERCITIUL 14")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    start = r.text.find("<title>") + len("<title>")
    end = r.text.find("</title>")
    print(r.text[start:end].strip())

    # Exercitiul 15
    print("EXERCITIUL 15")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    lines = r.text.splitlines()
    print("Numarul de linii in text:", len(lines))
    print("Linia cea mai mare este:", max(lines, key=len))

    # Exercitiul 16
    print("EXERCITIUL 16")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    if r.url.startswith("https://"):
        print("Conexiune securizată")
    else:
        print("Conexiune nesecurizată ")

    # Exercitiul 17
    print("EXERCITIUL 17")
    time.sleep(1)
    r = requests.get("http://cybercor.org", timeout=TIMEOUT)
    for i in r.history:
        print("suntem in:", i.url)
        print("codul de stare:", i.status_code)
    print("URL-ul final:", r.url)

    # Exercitiul 18
    print("EXERCITIUL 18")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    time.sleep(1)
    r2 = requests.head(BASE_URL, timeout=TIMEOUT)
    print("Lungimea la prima cerere:", len(r.content))
    print("Lungimea la a doua cerere:", len(r2.content))
    # Diferenta intre head() si get() este ca get() returneaza tot raspunsul serverului impreuna cu antetele, corpul paginii si codul html
    # Deaceea head() este gol avand doar antetele, aceasta face head() mult mai rapida daca e nevoie de verificat ceva setari a serverului

    # Exercitiul 19
    print("EXERCITIUL 19")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    if r.cookies:
        for cookie in r.cookies:
            print(f"{cookie.name}: {cookie.secure}")
    else:
        print("Niciun cookie setat")

    # Exercitiul 20
    print("EXERCITIUL 20")
    time.sleep(1)
    session = requests.Session()
    session.headers.update({"User-Agent": "WebLab-<Zlatin Nichita>"})
    r = session.get(ECHO_URL + "/headers")
    print(r.text)
    print(r.json())
    # json() are paranteze pentru ca acesta este un metoda, sau o functie in interiorul clasei Response care indeplineste un cod
    # Iar .text este un atribut sau o variabila initializata in interiorul clasei Response care contine text si nu indeplineste cod

if __name__ == "__main__":
    main()
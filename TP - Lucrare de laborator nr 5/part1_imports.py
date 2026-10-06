# Laborator: funcții, metode și importuri pe web
# Student: <Zlatin Nichita>

import time
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def main():

    # PARTEA 1

    # Exercitiul 1

    print("EXERCITIUL 1")
    import requests
    print(requests.__version__)
    import urllib.request
    # Modulul "requests" este o bibliotecă externă creată de comunitate, deacea avem nevoie de pip install.
    # Dar biblioteca urllib este o biblioteca standarta a limbajului python

    # Exercitiul 2
    print("EXERCITIUL 2")
    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print(r.status_code)

    time.sleep(1)
    from requests import get
    r2 = get(BASE_URL, timeout=TIMEOUT)
    print(r2.status_code)
    # Avantaj "import requests": Este clar de unde provine funcția și previne confuzia dacă ai o altă funcție numită get() în cod.
    # Avantaj "from requests import get": Codul devine mai scurt și mai simplu de citit dacă apelezi acea funcție de foarte multe ori.

    # Exercitiul 3
    print("EXERCITIUL 3")
    time.sleep(1)
    import requests as rq
    r = rq.get(BASE_URL, timeout=TIMEOUT)
    print(r.status_code)
    # Un alias face codul mai ușor de citit când numele original al bibliotecii este foarte lung sau folosit excesiv.
    # Îl face mai greu de citit dacă folosești un alias neobișnuit sau obscur (ex. "import requests as x"), deoarece alți programatori nu vor înțelege imediat ce modul folosești.

    # Exercitiul 4
    print("EXERCITIUL 4")
    time.sleep(1)
    try:
        r = urllib.request.urlopen(BASE_URL, timeout=TIMEOUT)
        print(r.status)
        text = r.read().decode("utf-8")
        print(text[:200])
    except urllib.error.HTTPError as e:
        print("Eroare, codul:", e.code)

    # Exercitiul 5
    print("EXERCITIUL 5")
    print(dir(requests))
    # get - este o functie care ne permite sa facem o cerere catre un anumit url
    # Session -  este o clasa folosită pentru a păstra "memoria" și anumite setări între mai multe cereri consecutive trimise către același site web.
    # exceptions - este un modul care contine erorile specifice bibliotecii request

    # Exercitiul 6
    print("EXERCITIUL 6")
    time.sleep(1)
    #print(help(requests.get))
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print(r.status_code)

    # Exercitiul 7
    print("EXERCITIUL 7")
    time.sleep(1)
    start = time.perf_counter()
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    end = time.perf_counter()
    measure_time = end - start
    measure_get_func = r.elapsed.total_seconds()
    print(f"Timpul masurat de biblioteca time: {measure_time}")
    print(f"Timpul masurat de functia elapsed: {measure_get_func}")

    # Exercitiul 8
    print("EXERCITIUL 8")
    try:
        import bs4
    except ImportError:
        print("Instalați modulul cu: pip install beautifulsoup4")


if __name__ == "__main__":
    main()
# Laborator: funcții, metode și importuri pe web
# Student: <numele vostru>
import time
import requests

import webtools
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def main():

    # PARTEA 5

    # Exercitiul 44
    print("EXERCITIUL 44")
    title = webtools.get_title(webtools.fetch(BASE_URL).text)
    print(title)

    # Exercitiul 45
    print("EXERCITIUL 45")
    from webtools import get_title, security_headers
    def get_title():
        return 1 + 5
    a = get_title()
    print(a)

    # Daca sar initializa inca o functie cu numele get_title aceasta o va
    # suprascrie pe aceea importata din webtools, deci in concluzie se va
    # executa aceeae initializata in cod

    # Exercitiul 46
    print("EXERCITIUL 46")
    # Mesajul "Autotest" nu apare deoarece acesta apare doar atunci cand fisierul webtools este rulat direct,
    # datorita faptului ca la importarea în main.py, variabila internă __name__ devine "webtools", condiția din
    # if este falsă, iar codul de test este ignorat.

    # Exercitiul 47
    print("EXERCITIUL 47")
    from webtools import DEFAULT_HEADERS

    r = webtools.fetch(BASE_URL)
    print("constanta:", DEFAULT_HEADERS)
    print("functia fetch:", r.status_code)

    # Exercitiul 48
    print("EXERCITIUL 48")
    import argparse
    from webtools import get_status
    parser = argparse.ArgumentParser(description="Laborator webtools - Argumente din linia de comandă")
    parser.add_argument("url", type=str, help="URL-ul care va fi accesat")
    args = parser.parse_args()
    status = get_status(args.url)
    print(status)

    # Exercitiul 49
    print("EXERCITIUL 49")
    from datetime import datetime
    import csv
    paths = ["/", "/robots.txt", "/sitemap.xml"]
    res_dict = webtools.check_paths(args.url, paths)
    with open("report.csv", "w", newline="", encoding="utf-8") as rep:
        writer = csv.writer(rep)
        writer.writerow(["path", "status", "checked_at"])
        for path, status in res_dict.items():
            current_time = datetime.now().isoformat()
            writer.writerow([path, status, current_time])

    print("Raportul a fost generat cu succes")

    # Exercitiul 50
    print("EXERCITIUL 50")
    rap = webtools.site_report(BASE_URL)


if __name__ == "__main__":
    main()

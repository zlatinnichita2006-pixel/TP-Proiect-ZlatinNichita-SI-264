# Laborator: funcții, metode și importuri pe web
# Student: <Zlatin Nichita>

import time
import requests
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def main():
    # Exercitiul 21
    print("EXERCITIUL 21")

    def fetch(url, timeout=10):
        response = requests.get(url, timeout=timeout)
        return response

    time.sleep(1)
    r = fetch(BASE_URL)
    print(r.status_code)

    # Exercitiul 22
    print("EXERCITIUL 22")

    def get_status(url: str) -> int:
        response = requests.get(url, timeout=TIMEOUT)
        return response.status_code

    time.sleep(1)
    r = get_status(BASE_URL + "/")
    time.sleep(1)
    r2 = get_status(BASE_URL + "/robots.txt")
    time.sleep(1)
    r3 = get_status(BASE_URL + "/sitemap.xml")
    time.sleep(1)
    print(f"Primul r: {r}\nAl doilea r: {r2}\nAl treilea r: {r3}")

    # Exercitiul 23
    print("EXERCITIUL 23")
    time.sleep(1)
    r = fetch(BASE_URL)
    time.sleep(1)
    r2 = fetch(BASE_URL, timeout=3)
    print(r.status_code)
    print(r2.status_code)

    # Exercitiul 24
    print("EXERCITIUL 24")

    def get_title(html):
        """
        Extrage și returnează titlul dintr-un text HTML.
        Folosește metoda .find() pentru a decupa textul dintre tag-urile <title>.
        :param html:
        :return: html[start:end].strip()
        """
        start = html.find("<title>") + len("<title>")
        end = html.find("</title>")
        return html[start:end].strip()

    time.sleep(1)
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    title = get_title(r.text)
    print(title)

    # Exercitiul 25
    print("EXERCITIUL 25")
    help(get_title)

    # Exercitiul 26
    print("EXERCITIUL 26")
    try:
        r = get_status(123)
        print(r)
    except requests.exceptions.MissingSchema:
        print("Eroare: sa introdus url inexistent")
    # Nu, adnotarile de tip nu dau o eroare de tip requests.exceptions.MissingSchema, aceasta eroare este cauzata de faptul
    # ca functia get se asteapta sa intalneasca o schema valida (https:// sau http://). in concluzie adnotarile sunt pur informative
    # si nu incurca nicicum la rularea functiei

    # Exercitiul 27
    print("EXERCITIUL 27")

    def page_exists(url: str) -> bool:
        try:
            r = requests.get(url, timeout=TIMEOUT)
            if r:
                return True
            else:
                return False
        except requests.RequestException:
            return False

    time.sleep(1)
    if page_exists("https://this-domain-does-not-exist.invalid"):
        print("pagina exista")
    else:
        print("pagina nu exista")

    # Exercitiul 28
    print("EXERCITIUL 28")

    def check_paths(base: str, paths: list[str]) -> dict[str, int]:
        dir_path = {}
        for path in paths:
            time.sleep(1)
            r = requests.get(base + path, timeout=TIMEOUT)
            dir_path[base + path] = r.status_code
        return dir_path

    my_path_dict = check_paths(base=BASE_URL, paths=["/", "/robots.txt", "/sitemap.xml"])
    print(my_path_dict)

    # Exercitiul 29
    print("EXERCITIUL 29")

    def get_header(url: str, name: str, default="lipseste") -> str:
        r = requests.get(url, timeout=TIMEOUT)
        my_header = r.headers.get(name, default)
        return my_header

    time.sleep(1)
    a = get_header(BASE_URL, name="server")
    print(a)

    # Exercitiul 30
    print("EXERCITIUL 30")

    def security_headers(url: str, headers: list[str]):
        dir_headers = {}
        r = requests.get(url, timeout=TIMEOUT)
        for i in headers:
            if i in r.headers:
                dir_headers[i] = True
            else:
                dir_headers[i] = False
        return dir_headers

    time.sleep(1)
    my_headers_dict = security_headers(BASE_URL, headers=["Strict-Transport-Security", "Content-Security-Policy",
                                                          "X-Frame-Options", "X-Content-Type-Options",
                                                          "Referrer-Policy"])
    print(my_headers_dict)

    # Exercitiul 31
    print("EXERCITIUL 31")

    def score_headers(results: dict[str, bool]):
        scor = 0
        for valoare in results.values():
            if valoare:
                scor += 1
        return f"{scor}/5"

    my_scored_string = score_headers(my_headers_dict)
    print(my_scored_string)

    # Exercitiul 32
    print("EXERCITIUL 32")

    def fetch_robots(base: str):
        r = requests.get(base + "/robots.txt", timeout=TIMEOUT)
        if r:
            return r.text
        else:
            return None

    def disallowed_paths(robots_text):
        if robots_text is None:
            return []
        values = []
        for line in robots_text.splitlines():
            if line.startswith("Disallow"):
                values.append(line.split(":")[1].strip())

        return values

    time.sleep(1)
    robot_txt = fetch_robots(BASE_URL)
    disallowed_list = disallowed_paths(robot_txt)
    print(disallowed_list)

    # Exercitiul 33
    print("EXERCITIUL 33")

    def response_times(*urls):
        url_dict = {}
        for url in urls:
            time.sleep(1)
            r = requests.get(url, timeout=TIMEOUT)
            total_time = r.elapsed.total_seconds()
            url_dict[url] = total_time
        return url_dict

    my_get_url = response_times("https://cybercor.org", "https://httpbin.org")
    print(my_get_url)

    # Exercitiul 34
    print("EXERCITIUL 34")

    def log(message, **details):
        final_message = message
        for key, value in details.items():
            final_message += " | {k}={v}".format(k=key, v=value)

        print(final_message)

    log("Verificat", url=BASE_URL, status_code=200)

    # Diferenta dintre print() si return este ca print() pur si simplu afiseaza pe ecran un anumit text, variabila sau functii,
    # iar rezultatul lui print() nu poate fi accesat
    # Dar return intoarce rezultatul inapoi in program, permitand astfel salvarea acestuia intro variabila care mai apoi
    # poate fi utilizata



if __name__ == "__main__":
    main()
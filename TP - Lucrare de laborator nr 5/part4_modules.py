# Laborator: funcții, metode și importuri pe web
# Student: <Zlatin Nichita>
import time
import requests
import urllib.parse
import re
import hashlib
import json
import socket
import ssl
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def main():

    # Exercitul 35
    print("EXERCITIUL 35")
    r = urllib.parse.urlparse("https://cybercor.org/path?x=1#top")
    print(r.scheme, r.netloc, r.path, r.query, r.fragment)

    # Exercitiul 36
    print("EXERCITIUL 36")
    r = urllib.parse.urljoin(BASE_URL, "/about")
    r2 = urllib.parse.urljoin(BASE_URL, "contact.html")
    r3 = urllib.parse.urljoin(BASE_URL, "../index.html")
    print(r)
    print(r2)
    print(r3)

    # Exercitiul 37
    print("EXERCITIUL 37")
    def extract_links(html):
        links = set(re.findall(r'href="([^"]+)"', html))
        return links

    r = requests.get(BASE_URL)
    href_links = extract_links(r.text)
    print(href_links)

    # Exercitiul 38
    print("EXERCITIUL 38")
    def split_links(links, domain):
        extern_links = []
        intern_links = []
        for link in links:
            parsed_link = urllib.parse.urljoin(BASE_URL, link)
            get_domain = urllib.parse.urlparse(parsed_link).netloc
            if get_domain == domain:
                intern_links.append(parsed_link)
            else:
                extern_links.append(parsed_link)

        return extern_links, intern_links

    # Exercitiul 39
    print("EXERCITIUL 39")
    from html.parser import HTMLParser

    class ImageFinder(HTMLParser):
        def __init__(self):
            super().__init__()
            self.images = []

        def handle_starttag(self, tag, attrs):
            if tag == "img":
                tag_dict = dict(attrs)
                res = tag_dict.get("src")
                if res is not None:
                    self.images.append(res)

    response = requests.get(BASE_URL, timeout=TIMEOUT)
    finder = ImageFinder()
    finder.feed(response.text)
    print(len(finder.images), "imagini găsite")
    for src in finder.images:
        print(src)
    print("Verificarea:", len(finder.images) == response.text.lower().count("<img"))

    # Exercitiul 40
    print("EXERCITIUL 40")
    def page_fingerprint(url):
        r = requests.get(url, timeout=TIMEOUT)
        return hashlib.sha256(r.content).hexdigest()

    a = page_fingerprint(BASE_URL)
    b = page_fingerprint(BASE_URL)
    print(f"{a}\n{b}\n{a==b}")
    # Amprentele vor fi diferite dacă serverul îți trimite un cod HTML ușor modificat la a doua cerere. La fiecare refresh
    # unele elemente ale paginii poate fi modificata precum ora, banner publicitar diferit etc.

    # Exercitiul 41
    print("EXERCITIUL 41")
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    with open("json_data.txt", "w") as f:
        json_data = json.dump(dict(r.headers), f, indent=2)

    with open("json_data.txt", "r") as f:
        python_data = json.load(f)
        print(python_data)

    # Exercitiul 42
    print("EXERCITIUL 42")
    def resolve(hostname):
        return socket.gethostbyname(hostname)

    aip = resolve("cybercor.org")
    print(aip)

    # Exercitiul 43
    print("EXERCITIUL43")
    def cert_days_left(hostname):
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expire_date_str = cert["notAfter"]
                expire_seconds = ssl.cert_time_to_seconds(expire_date_str)
                days_left = int((expire_seconds - time.time()) / 86400)
                return days_left


    d = cert_days_left("cybercor.org")
    print("zile ramase inainte de expirare:", d)

if __name__ == "__main__":
    main()
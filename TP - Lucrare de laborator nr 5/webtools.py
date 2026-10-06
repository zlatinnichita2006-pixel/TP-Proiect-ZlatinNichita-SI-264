import socket
import ssl
import requests
import time
import urllib.parse
import re
import json

BASE_URL = "https://cybercor.org"
TIMEOUT = 10


DEFAULT_HEADERS = {"User-Agent": "WebLab-Zlatin Nichita"}


def fetch(url, timeout=10):
    response = requests.get(url, timeout=timeout, headers=DEFAULT_HEADERS)
    return response

def get_status(url: str) -> int:
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

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


def security_headers(url: str, headers: list[str]):
    dir_headers = {}
    r = requests.get(url, timeout=TIMEOUT)
    for i in headers:
        if i in r.headers:
            dir_headers[i] = True
        else:
            dir_headers[i] = False
    return dir_headers

def score_headers(results: dict[str, bool]):
    scor = 0
    for valoare in results.values():
        if valoare:
            scor += 1
    return f"{scor}/5"

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

def extract_links(html):
    links = set(re.findall(r'href="([^"]+)"', html))
    return links

def check_paths(base: str, paths: list[str]) -> dict[str, int]:
    dir_path = {}
    for path in paths:
        time.sleep(1)
        r = requests.get(base + path, timeout=TIMEOUT)
        dir_path[base + path] = r.status_code
    return dir_path

def redir_paths(base):
    hostname = urllib.parse.urlparse(base).netloc
    http_url = "http://" + hostname
    r = requests.get(http_url, timeout=TIMEOUT)
    if r.history:
        return f"{r.history[0].status_code} -> {r.url}"
    else:
        return "Nicio redirecționare"

def cert_days_left(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expire_date_str = cert["notAfter"]
            expire_seconds = ssl.cert_time_to_seconds(expire_date_str)
            days_left = int((expire_seconds - time.time()) / 86400)
            return days_left

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


def site_report(url):
    hostname = urllib.parse.urlparse(url).netloc
    # 1
    status_code = get_status(url)
    # 2
    code_html = requests.get(url, timeout=TIMEOUT).text
    title = get_title(code_html)
    # 3
    ip = socket.gethostbyname(hostname)
    # 4
    redirect_chain = redir_paths(url)
    # 5
    my_headers_dict = security_headers(url, headers=["Strict-Transport-Security", "Content-Security-Policy",
                                                          "X-Frame-Options", "X-Content-Type-Options",
                                                          "Referrer-Policy"])
    scored_string = score_headers(my_headers_dict)
    # 6
    days_left = cert_days_left(hostname)
    # 7
    total_links = extract_links(code_html)
    ext_links, int_links = split_links(total_links, hostname)
    nr_extern_links = len(ext_links)
    nr_int_links = len(int_links)
    # 8
    text_robots = fetch_robots(url)
    dis_paths = disallowed_paths(text_robots)

    raport = {
        "Cod de stare": status_code,
        "Titlu": title,
        "Adresă IP": ip,
        "Redirecționări": redirect_chain,
        "Scor securitate": scored_string,
        "Certificat": f"{days_left} de zile rămase",
        "Legături": f"{nr_int_links} interne, {nr_extern_links} externe",
        "Căi interzise": dis_paths
    }
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(raport, file, indent=2, ensure_ascii=False)

    print("raportul a fost salvat in raport.json")



if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))



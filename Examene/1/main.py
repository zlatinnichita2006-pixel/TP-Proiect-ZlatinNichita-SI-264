from checker import SITES, SECURITY_HEADERS, build_url, is_https, show_response, check_site,scan_sites, check_headers, retry_check

# Partea 1: apeluri pentru build_url și is_https
fst_path = build_url("httpbin.org", "/json")
sec_path = build_url("httpbin.org", "html")
print(fst_path, "\n", sec_path)
# Partea 2: apeluri pentru show_response
is_fst_path = is_https("https://httpbin.org/status/200")
is_sec_path = is_https("https://httpbin.org/redirect/1")
print(is_fst_path, "\n", is_sec_path)
# Partea 3: apeluri pentru check_site
for site in SITES:
    vari = check_site(site)
    print(vari)
# Partea 4: apelul scan_sites()
scan_sites()
# Partea 5: apeluri pentru check_headers
dictio = check_headers()
# Partea 6: apeluri pentru retry_check

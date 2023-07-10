import requests

__endpoint__ = "forces"
def get_all_forces():
    print("CALL for FORCES")
    x = requests.get('https://data.police.uk/api/'+__endpoint__)
    print(x.status_code)
    print(x.json())


def get_force_by_id(force_id):
    print("CALL for one FORCE")
    x = requests.get('https://data.police.uk/api/'+__endpoint__+"/"+force_id)
    print(x.status_code)
    print(x.json())

def open_force_site(url):
    print("CALL for one force SITE")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    x = requests.get(url, headers)
    print(x.status_code)
    print(x.json())


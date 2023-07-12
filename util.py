from urllib.parse import urlparse
import requests

def fix_url_schema(url):
    # add schema if absent
    parsed = urlparse(url)
    if parsed.scheme not in ['http', 'https']:
        url = "http://" + url
    return url


def site_available(url):
    try:
        h = requests.head(fix_url_schema(url))
        if h.status_code < 500:
            return True
    except:
        return False

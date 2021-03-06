import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    print("*" * 20)
    if method == "POST":
        response = requests.post(url, data=data, headers=headers, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


if __name__ == "__main__":
    url = "www.baidu.com"
    print(parse_url(url))

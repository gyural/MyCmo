import requests
from requestURL import basic_url
import json

res = requests.get(basic_url)

def get_crawl_data():
    res_json = res.json()
    return res_json['data']

if __name__ == "__main__":
    print(get_crawl_data())

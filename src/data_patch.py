import requests
from requestURL import getURL
import json



def get_crawl_data(page):
    res = requests.get(getURL(page))
    res_json = res.json()
    return res_json['data']

if __name__ == "__main__":
    print(get_crawl_data())

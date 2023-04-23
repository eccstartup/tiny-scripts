import os.path
from datetime import datetime, timedelta
import requests
import time
import json


today = datetime.today()
first_day = today-timedelta(days=91)
if not os.path.exists('past'):
    os.makedirs('past')

for i in range(92):
    day = first_day + timedelta(days=i)
    date_str = day.strftime('%Y-%m-%d')
    print(f'getting {date_str}')
    if os.path.exists(f'past/past_{date_str}.json'):
        continue
    headers = {
        'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7'
    }
    api_str = f'https://www.hongkongairport.com/flightinfo-rest/rest/flights/past?date={date_str}&lang=en&cargo=false&arrival=false'
    print(api_str)
    req = requests.get(api_str, headers=headers)
    with open(f'past/past_{date_str}.json', 'w', encoding='utf-8') as f:
        json.dump(req.json(), f)
    time.sleep(1)

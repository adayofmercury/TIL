# Schedule의 사용
###### 210929


##### get_data_eth.py
```python

import pandas as pd
import requests
import time
import schedule
import csv

def get_data(symbol, term, cnt) :


    url = "https://api.upbit.com/v1/candles/" + term

    querystring = {"market":"KRW-"+symbol,"count":cnt} #카운트는 데이터의 갯수

    response = requests.request("GET", url, params=querystring)
    result = response.json()

    for i in result:
        print(i)
        OHLC={}
        OHLC["Date"] = i['candle_date_time_kst']
        OHLC["Price"] = i['trade_price']
        OHLC["Open"] = i['opening_price']
        OHLC["High"] = i['high_price']
        OHLC["Low"] = i['low_price']

        with open(symbol + '_' + str(term).replace('/','_') + '.csv', 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow([OHLC["Date"],OHLC["Price"],OHLC["Open"],OHLC["High"],OHLC["Low"]])


schedule.every(1).hours.do(get_data,'ETH', 'minutes/60', 1)

## symbol -> 업비트 기준 심볼 확인
## term ->
## days - 일
## minutes/1, 3, 5, 10, 15, 30, 60 240 - 분
## weeks - 주
## months - 월

while True :
    schedule.run_pending()
    time.sleep(1)

```

맨 아래행에 데이터를 축적하며 시계열 데이터를 구성하도록 하였다.

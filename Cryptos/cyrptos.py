import requests
import apikey as api
from time import sleep
import time
from pushbullet import Pushbullet


def crypt():
    response = requests.get('https://api.bitso.com/v3/order_book/?book=mana_mxn')
    json_response = response.json()

    price = float(json_response['payload']['bids'][0]['price'])
    amount = float(json_response['payload']['bids'][0]['amount'])
    updt = str(json_response['payload']['updated_at'])

    hr = (int(updt[11:13]))
    mn = int(updt[14:16])
    s = int(updt[17:19])

    if hr < 0:
        hr = hr + 7

    time = [hr, mn, s]

    print(f"Precio: {price}")
    print(f"Hora: {time[0]} Minutos: {time[1]} Segundos: {time[2]}")

    print("--------")


pb = Pushbullet(api.pkey)
'''test = ['1', '2', '3']

for i in range(len(test)):
    push = pb.push_note('Hola!', test[i])

pb.push_link("Link P", 'https://www.youtube.com/watch?v=TLdwBqDTF5g')'''
pb.delete_pushes()

while True:
    crypt()
    sleep(5)

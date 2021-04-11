import requests, json, time, re, pandas as pd
from decimal import Decimal

def return_auctions(lookup=None):

    base_url = 'https://api.hypixel.net/skyblock/auctions'
    base_response = requests.get(base_url)
    base_content = base_response.content
    base_info = json.loads(base_content)
    
    auctions = []
    for i in range(base_info['totalPages']):
        target_url = f'https://api.hypixel.net/skyblock/auctions?page={i}'
        target_response = requests.get(target_url)
        target_content = target_response.content
        target_info = json.loads(target_content)
        auctions += [i for i in target_info['auctions']]
        print(target_response.url)

    print(f"\n{len(auctions)}\n")

    n = 0
    for i in auctions:
        if lookup == None:
            print(f"Item: {i['item_name']}\nPrice: {i['starting_bid']}\nTime Left: {time.strftime('%H:%M:%S', time.gmtime(int(i['end'] / 1000 - time.time())))}\n")
        else:
            if lookup in i['item_name']:
                print(f"Item: {i['item_name']}\nPrice: {i['starting_bid']}\nTime Left: {time.strftime('%H:%M:%S', time.gmtime(int(i['end'] / 1000 - time.time())))}\n")
                n += 1

    print(f'Count: {n}')

# return_auctions("Hyperion")
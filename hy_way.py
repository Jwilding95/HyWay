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

def return_bazaar(lookup=None):
    
    base_url = 'https://api.hypixel.net/skyblock/bazaar'
    base_response = requests.get(base_url)
    base_content = base_response.content
    base_info = json.loads(base_content)
    products = base_info["products"]
    
    bazaar = [i for i in products]
    
    bazaar_parse = [
        {
            "Product": re.sub('_', ' ', products[i]['quick_status']['productId']).lower().title(),
            "Buy Price": Decimal(products[i]['quick_status']['buyPrice']).quantize(Decimal('.01')),
            "Buy Volume": products[i]['quick_status']['buyVolume'],
            "Bought/Week": products[i]['quick_status']['buyMovingWeek'],
            "Buy Orders": products[i]['quick_status']['buyOrders'],
            "Sell Price": Decimal(products[i]['quick_status']['sellPrice']).quantize(Decimal('.01')),
            "Sell Volume": products[i]['quick_status']['sellVolume'],
            "Sold/Week": products[i]['quick_status']['sellMovingWeek'],
            "Sell Orders": products[i]['quick_status']['sellOrders'],
            "ROI": Decimal(products[i]['quick_status']['buyPrice'] - products[i]['quick_status']['sellPrice']).quantize(Decimal('.01'))
        } for i in bazaar]
    
    df = pd.DataFrame(bazaar_parse)
    
    pd.set_option('display.max_rows', 500)
    
    print(df.sort_values(by='ROI', ascending=False))

# return_auctions("Hyperion")
return_bazaar()

# TODO:
# Get input of available funds
# Divide funds by price, multiply ROI by ans, return dataframe by multiplied return (Repeat until depleted or cutoff)
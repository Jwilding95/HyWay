def return_bazaar(funds=None, tax=1.25):
    
    base_url = 'https://api.hypixel.net/skyblock/bazaar'
    base_response = requests.get(base_url)
    base_content = base_response.content
    base_info = json.loads(base_content)
    products = base_info["products"]
    
    bazaar = [i for i in products]
    
    bazaar_parse = [
        {
            "Product": re.sub('_', ' ', products[i]['quick_status']['productId']).lower().title(),
            "Sell Price": Decimal(products[i]['quick_status']['sellPrice']).quantize(Decimal('.01')),
            "Sell Volume": products[i]['quick_status']['sellVolume'],
            "Sold/Week": products[i]['quick_status']['sellMovingWeek'],
            "Sell Orders": products[i]['quick_status']['sellOrders'],
            "Buy Price": Decimal(products[i]['quick_status']['buyPrice']).quantize(Decimal('.01')),
            "Buy Volume": products[i]['quick_status']['buyVolume'],
            "Bought/Week": products[i]['quick_status']['buyMovingWeek'],
            "Buy Orders": products[i]['quick_status']['buyOrders'],
            "ROI": Decimal((products[i]['quick_status']['buyPrice'] - products[i]['quick_status']['sellPrice']) - ((products[i]['quick_status']['buyPrice'] - products[i]['quick_status']['sellPrice']) * (tax / 100))).quantize(Decimal('.01'))
        } for i in bazaar]
    
    # df = pd.DataFrame(bazaar_parse)
    
    # if funds != None:
        # df = df[df["Buy Price"] <= funds]
    
    # pd.set_option('display.max_rows', 500)
    
    # print(df.sort_values(by='ROI', ascending=False))

return_bazaar(50000)

# TODO:
# Divide funds by price, multiply ROI by ans, return dataframe by newly multiplied ROI (Repeat until depleted or cutoff)
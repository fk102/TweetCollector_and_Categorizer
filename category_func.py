import pandas as pd

import pandas as pd
df = pd.read_csv('stuff.csv')

keywords1 = ['MSI', 'Gaming', 'EVGA', 'AMD', 'ASUS', 'Intel', 'ZOTAC', 'NVIDIA', 'ASTRO', 'GIGABYTE',
             'Acer', 'Dell', 'Lenovo', 'Hp', 'Panasonic', 'keyboard', 'mouse', 'headset', 'monitor', 'processor', 'Ram', 'chromebook', 'gaming laptop', 'laptop', 'windows 10']
keywords2 = ['Song', 'Spotify', 'iTunes', 'album', 'Cassettes',
             'film', 'mp3', 'netflix', 'amazon prime', 'twitch', 'live on', 'youtube', 'ebook']
keywords3 = ['Dishwasher',
             ' DVD player', 'Adapter', 'TV', 'Tablet', 'smart tv', 'android tv', 'apple tv']
keywords4 = ['Jewellery', '#Beauty', '#rings', 'skincare', 'facewash',
             'shampoo', 'conditioner', 'lipstick', 'oils', 'cosmetics', 'makeup', 'Jacket', '#Sports', '#Outdoors', 'adidas', 'Nike', 'Air Jordan', 'Shirt', 'underwear', 'sweaters', 'jackets', 'loafers']
keywords5 = ['Funko Pop!', 'Funko Pop', 'PopFigures', 'Funko'
             'Vinyl Figure', 'toys', 'figure', '#modeltrains', 'LEGO']
keywords6 = ['xbox', 'playstation', 'ps4', 'ps5', 'pcgaming',
             'esports', 'e-sports', 'twitch rivals', 'valorant', 'overwatch', 'war hammer']
keywords7 = ['#art', '#craft']
keywords8 = ['Car Insurance', 'cars',
             '#motorcycle', '#motorbike', 'Toyota', 'Ford']
keywords9 = ['Furnitures', 'Curtain', 'Wall', 'carpet'
             'Mug', '#decor', 'homedecor', 'decoration', 'kitchen', 'Kitchen Knife', 'kitchen knives']
keywords10 = ['tea', 'corn', 'Gfuel', 'Pistachios', 'Tomato Salsa', 'almonds',
              'treats', 'bread', 'diet', 'meat', 'food', 'noodle', 'soup', 'Waffles', 'Coca cola']
keywords11 = ['NFT', 'token', 'BinanceChain',
              'crypto', 'bitcoin', '#freecrypto']
keywords12 = ['discount']

val1 = 'Computers'
val2 = 'Media and Music'
val3 = 'Electronics'
val4 = 'Fashion and Beauty'
val5 = 'Toys'
val6 = 'Games'
val7 = 'Art and Crafts'
val8 = 'Automotive'
val9 = 'Household and Kitchen'
val10 = 'Food'
val11 = 'Crypto'
val12 = 'Business'

keywords = [keywords1, keywords2, keywords3, keywords4,
            keywords5, keywords6, keywords7, keywords8, keywords9, keywords10, keywords11, keywords12]
values = [val1, val2, val3, val4, val5, val6,
          val7, val8, val9, val10, val11, val12]


def word_check(description):
    for i in range(0, len(keywords)):
        for word in keywords[i]:
            if word in description:
                if word in keywords[i]:
                    df.at[index, 'category'] = values[i]
                else:
                    for word in keywords[i+1]:
                        if word in description:
                            df.at[index, 'category'] = values[i+1]


df['category'] = ''

for index, row in df.iterrows():
    description = row['fulltext']
    word_check(description)


print(df.head())
# and/or
df.to_csv('categorized_test.csv')

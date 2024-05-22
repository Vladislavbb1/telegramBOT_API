import requests

def get_bitcoin_prices(api_key):
    url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,BCH,EOS,BNB,BSV,XLM,ADA&tsyms=RUB&api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    bitcoin_prices = {}
    for symbol, price in data.items():
        if symbol == 'BTC':
            name = 'Bitcoin'
        elif symbol == 'ETH':
            name = 'Ethereum'
        elif symbol == 'LTC':
            name = 'Litecoin'
        elif symbol == 'XRP':
            name = 'Ripple'
        elif symbol == 'BCH':
            name = 'Bitcoin Cash'
        elif symbol == 'EOS':
            name = 'EOS'
        elif symbol == 'BNB':
            name = 'Binance Coin'
        elif symbol == 'BSV':
            name = 'Bitcoin SV'
        elif symbol == 'XLM':
            name = 'Stellar'
        elif symbol == 'ADA':
            name = 'Cardano'
        bitcoin_prices[name] = price['RUB']

    return bitcoin_prices


# Ваш ключ API
api_key = "68be2293c8af0f8d8868c9c47c07d77a6d7952eab6e74f5b3fef2abaf163ed21"

# Получение и вывод курсов биткойна, эфириума, лайткойна и других криптовалют в рублях
bitcoin_prices = get_bitcoin_prices(api_key)

for name, price in bitcoin_prices.items():
    print(f"Текущий курс {name} в рублях: {price:.2f} ₽")
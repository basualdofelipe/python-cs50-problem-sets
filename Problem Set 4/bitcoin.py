#https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests, sys, json

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_price = response.json()["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    pass

def main():

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
    except IndexError:
        print("Missing command-line argument")
    else:
        res = bitcoins * bitcoin_price
        print(f"${res:,}")


main()
import sys
from cviceni6 import download_rates 

def convert_amount(amount, currency):
    rates = download_rates()
    if currency not in rates:
        raise ValueError(f"Currency {currency} not found in rates")
    rate=rates[currency]
    return amount / rate

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} amount currency")
        sys.exit()

    amount = int(sys.argv[1])
    currency = sys.argv[2]
    try:
        print(convert_amount(amount, currency))
    except ValueError as e:
        print(e)
        sys.exit()
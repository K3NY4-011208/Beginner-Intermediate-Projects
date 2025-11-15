rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "KES": 153.5
}

amount = float(input("Enter amount: "))
from_currency = input("From (USD/EUR/KES): ").upper()
to_currency = input("To (USD/EUR/KES): ").upper()

usd_amount = amount / rates[from_currency]
converted = usd_amount * rates[to_currency]

print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")

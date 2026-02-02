"""
f-strings are available from Python 3.6.
"""

from datetime import datetime


name = "Axell"
age = 25
greetings = f"Hello {name}, you are {age} years old."

print(greetings)

greetings = f"Hello {name.upper()}, you are {age} years old."
print(greetings)

bank_balance = 30000000000
formatted_balance = f"Youre balance is ${bank_balance:,}"
print(formatted_balance)

stock_price = 145.38
formatted_price = f"The stock price is ${stock_price:.1f}"
print(formatted_price)

user_id = 25
formatted_user_id = f"User ID: {user_id:06d}"
print(formatted_user_id)

date = datetime(2024, 9, 10, 10)
formatted_date = f"Formatted date: {date:%A %d %B %Y %I:%M %p}"
print(formatted_date)

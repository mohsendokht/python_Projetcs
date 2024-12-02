"""Gets coin price. 
"""


import datetime
import requests
import click
import sqlite3


def get_coin_price(coin_id, currency):
    """get coin price(coin_id,currency)"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    data = requests.get(url, timeout=60).json()
    coin_price = data[coin_id][currency]
    return coin_price


@click.group()
def cli():
    """ cli """
    # pass


@click.command()
@click.option("--coin_id", default="bitcoin")
@click.option("--currency", default="usd")
def show_coin_price(coin_id, currency) -> None:
    """Show the coin price"""
    coin_price = get_coin_price(coin_id, currency)
    print(f"The price of {coin_id} is {coin_price: .2f} {currency.upper()}")


@click.command()
@click.option("--coin_id")
@click.option("--currency")
@click.option("--amount", type=float)
@click.option("--sell", is_flag=True)
def add_investment(coin_id, currency, amount, sell):
    """Insert investment """
    # SQL_QUERY= "INSERT INTO investment VALUES (?, ?, ?, ?, ?);"
    values = (coin_id, currency, sell, amount, datetime.datetime.now())
    cursor.execute("INSERT INTO investment VALUES (?, ?, ?, ?, ?);",values)
    database.commit()

    if sell:
        print(f"Added sell of {amount} {coin_id}")
    else:
        print(f"Added buy of {amount} {coin_id}")


@click.command()
@click.option("--coin_id")
@click.option("--currency")
def get_investment_value(coin_id, currency):
    """Get the coin investment value  """
    SQL_QUERY= "SELECT amount FROM investment WHERE coin_id = ? AND currency = ? AND sell = ?;"
    
    buy_result = cursor.execute(SQL_QUERY, (coin_id, currency, False)).fetchall()
    sell_result = cursor.execute(SQL_QUERY, (coin_id, currency, True)).fetchall()
    buy_amount = sum([row[0] for row in buy_result])
    sell_amount = sum([row[0] for row in sell_result])
    total = buy_amount - sell_amount

    print(f"You own a total of {total} {coin_id} worth {total * 10} {currency.upper()}")
    

cli.add_command(show_coin_price)
cli.add_command(add_investment)
cli.add_command(get_investment_value)

CREATE_INVESTMENT_SQL = """
    CREATE TABLE investment (
           coin_id TEXT, 
           currency TEXT, 
           sell INT,
           amount REAL, 
           transactionDate TIMESTAMP);
"""


if __name__ == "__main__":
   database = sqlite3.connect("portfolio.db")
   cursor = database.cursor()
   # cursor.execute(CREATE_INVESTMENT_SQL)
   cli()


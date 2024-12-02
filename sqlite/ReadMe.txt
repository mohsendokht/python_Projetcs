# Create a venv:
> python -m venv .venv

# To install request package in your venv. 
> pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org requests 

# use sqlite in powershell terminal
#  enter sqlite3 in command line
> sqlite3

#create a file (database) if not exists
> .open test1.db

# create a table with name Investments
> CREATE TABLE Investments (coin_id TEXT, currency TEXT, amount REAL);

# get table list
> .tables
#
# Tell SQLite to display the column headers, Tell SQLite to format using columns, then show the table information
> .headers on
> .mode column
> pragma table_info('investments');

# Insert statement
> INSERT INTO investments VALUES('bitcoin','usd', 1.0);
> SELECT * FROM investments;

# exit command
> .exit
=======================================
# How to create a command line application:
  - import click
  - add the command decorator : @click.command()
  - add command line option: @click.option()
  - add command cli.add_command(show_coin_price)
  - call command , replace _ with - .
  example:
  - python main.py show-coin-price --coin_id=bitcoin --currency=gbp
  - python main.py add-investment --coin_id=bitcoin --currency=gbp --amount=10.0
  - python main.py add-investment --coin_id=bitcoin --currency=gbp --amount=5.0 --sell  
from gcapi import GCapiClient  # From https://github.com/rickykim93/gcapi-python
from gcapi.gcapi_tools import format_date  # From https://github.com/rickykim93/gcapi-python
from datetime import datetime
from time import sleep
import numpy


def check_sell_criteria(prices):
    # TODO: Write your algorithm to detect sell condition here
    return False


def check_buy_criteria(prices):
    # TODO: Write your algorithm to detect buy condition here
    return False


# Current time
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
print("Program started at:", dt_string)

print("Authenticating...")
api = GCapiClient(username='YOUR_USERNAME', password='YOUR_PASSWORD',
                  appkey='YOUR_APP_KEY', proxies=None)
print("Authenticated successfully...")

print("Getting account information...")
response = api.get_account_info(get=None)
account_id = response['TradingAccounts'][0]['TradingAccountId']
print(response)

print("Requesting information on currency pair...")
currency_pair = 'USD/CNH'  # Currency pair to be traded
market_id = api.get_market_info(currency_pair, get=None)['Markets'][0]['MarketId']
print("Trading %s of id %s" % (currency_pair, market_id))

# Trading loop
while 1:
    # API endpoints may fail
    try:
        # Period of trading loop. In this case, runs every 10 seconds
        sleep(10)

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        print("Starting loop at:", dt_string)

        # No trading on weekends
        if now.weekday() not in [0, 1, 2, 3]:
            print("Not a trading day. Restarting loop...")
            continue

        # Get a specified number of past price points
        response = api.get_prices(market_id=market_id, num_ticks=50)

        # Extract price points from response
        price_data = list(map(lambda p: p['Price'], response['PriceTicks']))
        price_current = price_data[-1]
        price_mean = numpy.mean(price_data)
        price_std = numpy.std(price_data)

        print('Current price is %s with mean %1.5f and std %1.5f. Timestamp from request %s.' % (
            price_current, price_mean, price_std, response['PriceTicks'][-1]))

        # Check open positions
        response = api.list_open_positions(trading_acc_id=account_id)
        open_positions = response['OpenPositions']

        # This code is made to work with a single open position at a time.
        # If there is more than one open position
        if len(open_positions) > 1:
            print("ERROR! We have more than one open position...")
            continue

        elif len(open_positions) == 1:
            price_open_position = open_positions[0]['Price']
            # ONLY 1 open position at a time
            print(response['OpenPositions'][0])
            print(
                "Already have open position. Checking if sell criteria has been met...")

            # Place a SELL order if criteria is met
            if check_sell_criteria(price_data):
                response = api.trade_order(1000, price_current, 'sell', trading_acc_id=account_id,
                                           market_id=market_id, market_name=currency_pair)

                print('SELL order has been placed!')
                print(response)

        # Place a BUY order if criteria is met
        elif check_buy_criteria(price_data):
            # Set acceptable bounds for take profit (automatic sell if price exceeds threshold)
            # and stop loss (automatic sell if price drops below threshold).
            price_stop_loss = price_current * 0.995
            price_take_profit = price_current * 1.005

            response = api.trade_order(1000, price_current, 'buy', trading_acc_id=account_id, market_id=market_id,
                                       market_name=currency_pair, stop_loss=price_stop_loss,
                                       take_profit=price_take_profit)

            print('BUY order has been placed!')
            print(response)
    except Exception as e:
        print(e)










